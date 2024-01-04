import csv
import matplotlib.pyplot as plt
import tifffile
import os
import numpy as np

mask_path="D:\\zfish\\masks"
csv_file = "D:\\zfish\\13reg\\0705F7low\\Plane4_roi_coordinates_reg.csv"  # Path of registered coordinates
points = []  # save coordinates

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip title
    for row in csv_reader:
        x, y, z= map(float, row[3:6])  # read reg_x,reg_y,reg_z
        points.append((int(round(x)), int(round(y)), int(round(z))))#approximity
print(points[0])

image_width = 597
image_height = 974

brain_area=[] # four files: fore, mid, hind, pns
mask_files=[]   #tif files downloaded from mapzebrain
for root, dirs, files in os.walk(mask_path):
    for dir in dirs:
        subfolder_path = os.path.join(root, dir)
        brain_area.append(subfolder_path)
        # iterate
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if os.path.isfile(file_path) and file.endswith('.tif'):
                # read and save tif file
                tif_data = tifffile.imread(file_path)
                mask_files.append(tif_data)
                x=np.average(tif_data,axis=0)
                plt.figure(figsize=(image_width / 200, image_height / 200))
                plt.imshow(x, cmap='gray')  # show masks
                plt.title(f"Mask: {os.path.basename(file_path)}")
                plt.show()

# print(mask_files[2])
print(brain_area)

point_to_mask={}
# Create a mapping of points to the corresponding mask files
point_to_mask = {}
for root, dirs, files in os.walk(mask_path):
    for dir in dirs:
        subfolder_path = os.path.join(root, dir)
        brain_area.append(subfolder_path)
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if os.path.isfile(file_path) and file.endswith('.tif'):
                mask_data = tifffile.imread(file_path)
                mask_files.append(mask_data)
                point_to_mask[os.path.basename(file_path)] = mask_data

# # Map points to the corresponding mask frames with matching z coordinates
# for point in points:
#     x, y, z = point
#     for mask_filename, mask_data in point_to_mask.items():
#         if mask_data.shape[0] > z:
#             frame = mask_data[z]
#             plt.figure(figsize=(image_width / 200, image_height / 200))
#             plt.imshow(frame, cmap='gray')
#             plt.scatter(x, y, color='red', marker='o', s=10)  # Mark the point on the frame
#             plt.title(f"Mask: {mask_filename}, Frame: {z}")
#             plt.show()

# Create a CSV file to write RGB values
csv_output_file = "RGB_Values.csv"

with open(csv_output_file, mode='w', newline='') as csv_file:
    fieldnames = ['Mask', 'Frame', 'Point_X', 'Point_Y', 'RGB_Value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    for point in points:
        x, y, z = point
        for mask_filename, mask_data in point_to_mask.items():
            if mask_data.shape[0] > z:
                frame = mask_data[z]
                rgb_value = frame[y, x]
                writer.writerow({'Mask': mask_filename, 'Frame': z, 'Point_X': x, 'Point_Y': y, 'RGB_Value': rgb_value})

print(f"RGB values have been saved to {csv_output_file}")

# # Create a CSV file to store the results
# csv_output_file = "Point_to_TIF_Mapping.csv"
#
# with open(csv_output_file, mode='w', newline='') as csv_file:
#     fieldnames = ['Point_X', 'Point_Y', 'Point_Z'] + [os.path.basename(mask_file) for mask_file in point_to_mask.keys()]
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#
#     writer.writeheader()
#
#     for point in points:
#         x, y, z = point
#         result_row = {'Point_X': x, 'Point_Y': y, 'Point_Z': z}
#         for mask_filename, mask_data in point_to_mask.items():
#             if mask_data.shape[0] > z:
#                 frame = mask_data[z]
#                 rgb_value = frame[y, x]
#                 if any(rgb_value):  # Check if any RGB channel is non-zero
#                     result_row[mask_filename] = 'TRUE'
#                 else:
#                     result_row[mask_filename] = 'FALSE'
#         writer.writerow(result_row)
#
# print(f"Point-to-TIF mapping results have been saved to {csv_output_file}")

import csv
import os

# 指定要检查的CSV文件的路径
csv_file_path = "RGB_Values.csv"

# 创建一个字典来存储每个.tif文件的出现次数
tif_file_counts = {}

# 打开CSV文件进行读取
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    # 遍历每一行
    for row in csv_reader:
        # 获取最后一列的值，并将其转换为整数
        last_column_value = int(row[-1])

        # 获取当前行的.tif文件名（假设它在倒数第二列）
        tif_filename = os.path.splitext(row[0])[0]  # 去除扩展名

        if last_column_value != 0:
            # 增加.tif文件的出现次数计数，如果它已经在字典中，则加1，否则设置为1
            if tif_filename in tif_file_counts:
                tif_file_counts[tif_filename] += 1
            else:
                tif_file_counts[tif_filename] = 1

# 创建一个CSV文件来保存结果
output_csv_file = "TIF_File_Counts.csv"

with open(output_csv_file, mode='w', newline='') as csv_file:
    fieldnames = ['TIF_File', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    # 将结果写入CSV文件
    for tif_filename, count in tif_file_counts.items():
        writer.writerow({'TIF_File': tif_filename, 'Count': count})

print(f"Results have been saved to {output_csv_file}")

