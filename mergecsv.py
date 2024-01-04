import pandas as pd

file1 = "E:\\new_roi1107\\2023-07-05_F2_highintensity\\Plane2_roi_coordinates_0.5_reg.csv"
file2 = "E:\\new_roi1107\\transformation\\2023-07-13_F5_lowintensity\\Plane2_roi_coordinates_0.5_reg.csv"
file3 = "E:\\new_roi1107\\transformation\\2023-08-04_F5_highintensity\\Plane2_roi_coordinates_0.5_reg.csv"
file4 = "E:\\new_roi1107\\transformation\\2023-08-11_F2_lowintensity_2\\Plane2_roi_coordinates_0.5_reg.csv"
file5 = "E:\\new_roi1107\\transformation\\2023-08-11_F5_lowintensity_2\\Plane2_roi_coordinates_0.5_reg.csv"
file6 = "E:\\new_roi1107\\transformation\\2023-08-11_F8_lowintensity\\Plane2_roi_coordinates_0.5_reg.csv"
file7 = "E:\\new_roi1107\\transformation\\2023-09-21_F3_2deg\\Plane2_roi_coordinates_0.5_reg.csv"
file8 = "E:\\new_roi1107\\transformation\\2023-09-22_F1_2deg_2\\Plane2_roi_coordinates_0.5_reg.csv"
file9 = "E:\\new_roi1107\\transformation\\2023-09-22_F6_2deg\\Plane2_roi_coordinates_0.5_reg.csv"
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)
df4 = pd.read_csv(file4)
df5 = pd.read_csv(file5)
df6 = pd.read_csv(file6)
df7 = pd.read_csv(file7)
df8 = pd.read_csv(file8)
df9 = pd.read_csv(file9)
merged_df = pd.concat([df1, df2, df4, df5, df6], ignore_index=True)


output_directory = "E:\\new_roi1107\\fivefish\\"
output_file_name = "merged_plane2.csv"
output_path = output_directory + output_file_name


import os

os.makedirs(output_directory, exist_ok=True)


merged_df.to_csv(output_path, index=False)

print(f"合并完成，数据已保存到 {output_path}。")
