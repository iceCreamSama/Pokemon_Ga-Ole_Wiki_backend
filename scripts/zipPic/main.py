import cv2
import os
import glob


def process_image(image_path, output_folder):
    # 读取图片（保留透明通道）
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    h, w, _ = img.shape
    max_size = (40, 40)
    scale_factor = min(max_size[0] / w, max_size[1] / h)
    resized_img = cv2.resize(img, (int(w * scale_factor), int(h * scale_factor)))

    # 保存裁剪后的图片到输出文件夹（保留透明通道）
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_path, resized_img, [cv2.IMWRITE_PNG_COMPRESSION, 30])


def batch_process(input_folder, output_folder):
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):  # 只处理png和jpg图片
            image_path = os.path.join(input_folder, filename)
            process_image(image_path, output_folder)


if __name__ == '__main__':
    input_folder = r"D:\Code\images\Pending"  # 输入文件夹路径
    output_folder = r"D:\Code\images\output"  # 输出文件夹路径
    files = glob.glob(os.path.join(output_folder, '*'))
    for file in files:
        os.remove(file)
    batch_process(input_folder, output_folder)
