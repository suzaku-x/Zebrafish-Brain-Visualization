import csv
import matplotlib.pyplot as plt
import tifffile
import os
import numpy as np

folder_path = "E:\\new_roi1107\\sixfish\\0811F8"
mask_path = "E:\\newmasks"
# mask_path="E:\\atlasmask"
plane_num = ["2","3","4","5","6","7","8","9","10"]
brain_area = []  # four files: fore, mid, hind, pns
mask_files = []  # tif files downloaded from mapzebrain
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

print(brain_area)
i=0

for i in range(5,9):
    csv_file ="E:\\new_roi1107\\sixfish\\0811F8\\Plane"+plane_num[i]+"_roi_coordinates_0.5_reg.csv" # Path of registered coordinates
    # create a dictionary to save masks' tif files
    # output_folder = "D:\\zfish\\output_tif_files"  # only run once, you can skip this step
    # os.makedirs(output_folder, exist_ok=True)
    points = []  # save coordinates

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip title
        for row in csv_reader:
            x, y, z = map(float, row[3:6])  # read reg_x,reg_y,reg_z
            points.append((int(round(x)), int(round(y)), int(round(z))))  # approximity
    print(points[0])



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

    # Create a CSV file to write RGB values
    csv_output_file = os.path.join(folder_path, "RGB_Values" + plane_num[i] + ".csv")

    with open(csv_output_file, mode='w', newline='') as csv_file:
        fieldnames = ['Mask', 'Frame', 'Point_X', 'Point_Y', 'RGB_Value','label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        i=-1
        for point in points:
            x, y, z = point
            i = i + 1
            for mask_filename, mask_data in point_to_mask.items():
                if mask_data.shape[0] > z:
                    frame = mask_data[z]
                    rgb_value = frame[y, x]
                    writer.writerow({'Mask': mask_filename, 'Frame': z, 'Point_X': x, 'Point_Y': y, 'RGB_Value': rgb_value,'label':i})

                    # if rgb_value != 0:  # Only save rows where RGB value is not 0
                    #     writer.writerow(
                    #         {'Mask': mask_filename, 'Frame': z, 'Point_X': x, 'Point_Y': y, 'RGB_Value': rgb_value})
    print(f"RGB values have been saved to {csv_output_file}")

    # # check path
    # csv_file_path = os.path.join(folder_path, "RGB_Values" + plane_num[i] + ".csv")
    #
    # # create a dictionary to store the counts
    # tif_file_counts = {}
    #
    # with open(csv_file_path, 'r') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     next(csv_reader)
    #     for row in csv_reader:
    #         # get RGB
    #         last_column_value = int(row[-1])
    #         tif_filename = os.path.splitext(row[0])[0]
    #
    #         if last_column_value != 0:
    #             if tif_filename in tif_file_counts:
    #                 tif_file_counts[tif_filename] += 1
    #             else:
    #                 tif_file_counts[tif_filename] = 1
    #
    # output_csv_file = os.path.join(folder_path, "TIF_File_Counts" + plane_num[i] + ".csv")
    #
    # with open(output_csv_file, mode='w', newline='') as csv_file:
    #     fieldnames = ['TIF_File', plane_num[i], 'Count']
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     writer.writeheader()
    #
    #     for tif_filename, count in tif_file_counts.items():
    #         writer.writerow({'TIF_File': tif_filename, 'Count': count})
    #
    # print(f"Results have been saved to {output_csv_file}")