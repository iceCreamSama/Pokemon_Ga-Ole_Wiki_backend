import os

# 指定文件夹路径  
folder_path = r'D:\Code\images\pending'  # 请将'your_folder_path'更改为实际的文件夹路径

# 获取文件夹下所有文件的文件名  
file_names = os.listdir(folder_path)

for file_name in file_names:
    # 检查文件名是否符合"aaa_bbb_ccc.png"的格式  
    # if file_name.startswith('Spr_') and file_name.endswith('.png'):
    #     # 分割文件名获取"bbb"和"ccc"的部分
    #     parts = file_name.split('_')
    #     if len(parts) == 3:
    #         bbb = parts[1]
    #         ccc = parts[2][:-4]  # 去掉.png后缀获取文件名
    #         # 重命名文件
    #         new_file_name = f'{ccc}.png'
    #         os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))

    if len(file_name.split('!')) == 2 and file_name.endswith('.png'):
        new_name = file_name.split('!')[1]
    else:
        new_name = file_name
    if 'Mega' in new_name:
        new_name = new_name[:3] + 'M'
    else:
        new_name = new_name[:3]
    new_file_name = f'{new_name}.png'
    print('old name: {}, new name: {}'.format(file_name, new_name))
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_file_name))
