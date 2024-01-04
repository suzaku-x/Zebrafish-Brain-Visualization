import csv
import matplotlib.pyplot as plt
import tifffile
import os
import numpy as np
folder_path = "E:\\new_roi1107\\sixfish"
mask_path = "E:\\newmasks"
# mask_path="E:\\atlasmask"
# save_mask_path='E:\\maskaver'
#csv_file ="E:\\new_roi1107\\output_pc11082.csv" # Path of registered coordinates
# create a dictionary to save masks' tif files
# output_folder = "D:\\zfish\\output_tif_files"  # only run once, you can skip this step
# os.makedirs(output_folder, exist_ok=True)
points = []  # save coordinates
plane_num = "_pc_final111"  # remember to change this!
# check path
#csv_file_path = os.path.join(folder_path, "RGB_Values" + plane_num + ".csv")
csv_file_path="E:\\new_roi1107\\sixfish\\output_pc_final111.csv"
# create a dictionary to store the counts
tif_file_counts = {}

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        # get RGB
        last_column_value = 255
        tif_filename = os.path.splitext(row[7])[0]

        if last_column_value != 0:
            if tif_filename in tif_file_counts:
                tif_file_counts[tif_filename] += 1
            else:
                tif_file_counts[tif_filename] = 1

output_csv_file = os.path.join(folder_path, "TIF_File_Counts" + plane_num + ".csv")

with open(output_csv_file, mode='w', newline='') as csv_file:
    fieldnames = ['TIF_File', plane_num, 'Count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for tif_filename, count in tif_file_counts.items():
        writer.writerow({'TIF_File': tif_filename, 'Count': count})

print(f"Results have been saved to {output_csv_file}")