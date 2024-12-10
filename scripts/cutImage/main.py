import cv2
import os
import glob


def process_image(image_path, output_folder, crop_x=0, crop_y=0, crop_width=0, crop_height=0):
    # 读取图片（保留透明通道）
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # 如果未指定裁剪区域，则使用自动裁剪
    if crop_width == 0 or crop_height == 0:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 可调整thresh值来优化效果
        _, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        # _, thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 可调整参数(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
        max_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(max_contour)
        crop_x = x
        crop_y = y
        crop_width = w
        crop_height = h

        # 裁剪图片
    cropped_img = img[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]

    # 保存裁剪后的图片到输出文件夹（保留透明通道）
    output_path = os.path.join(output_folder, os.path.basename(image_path))
    # cv2.imwrite(output_path, cropped_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
    cv2.imwrite(output_path, cropped_img, [cv2.IMWRITE_PNG_COMPRESSION, 0])


def batch_process(input_folder, output_folder, crop_x=0, crop_y=0, crop_width=0, crop_height=0):
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".png") or filename.endswith(".jpg"):  # 只处理png和jpg图片
            image_path = os.path.join(input_folder, filename)
            process_image(image_path, output_folder, crop_x, crop_y, crop_width, crop_height)


if __name__ == '__main__':
    input_folder = r"D:\Code\images\Pending"  # 输入文件夹路径
    output_folder = r"D:\Code\images\output"  # 输出文件夹路径
    files = glob.glob(os.path.join(output_folder, '*'))
    for file in files:
        os.remove(file)
    batch_process(input_folder, output_folder)
