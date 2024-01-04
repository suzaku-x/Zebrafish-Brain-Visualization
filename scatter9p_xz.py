import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Input csv
csv_file1 = "E:\\new_roi1107\\result1107\\RGB_Values_plane2.csv"
df1 = pd.read_csv(csv_file1)

csv_file2 = "E:\\new_roi1107\\result1107\\RGB_Values_plane3.csv"
df2 = pd.read_csv(csv_file2)

csv_file3 = "E:\\new_roi1107\\result1107\\RGB_Values_plane4.csv"
df3 = pd.read_csv(csv_file3)
csv_file4 = "E:\\new_roi1107\\result1107\\RGB_Values_plane5.csv"
df4 = pd.read_csv(csv_file4)
csv_file5 = "E:\\new_roi1107\\result1107\\RGB_Values_plane6.csv"
df5 = pd.read_csv(csv_file5)
csv_file6 = "E:\\new_roi1107\\result1107\\RGB_Values_plane7.csv"
df6 = pd.read_csv(csv_file6)
csv_file7 = "E:\\new_roi1107\\result1107\\RGB_Values_plane8.csv"
df7 = pd.read_csv(csv_file7)
csv_file8 = "E:\\new_roi1107\\result1107\\RGB_Values_plane9.csv"
df8 = pd.read_csv(csv_file8)
csv_file9 = "E:\\new_roi1107\\result1107\\RGB_Values_plane10.csv"
df9 = pd.read_csv(csv_file9)

# Input tif
tif_file = "E:\\Atlas\\AVGxz_HSA.tif"
img = Image.open(tif_file)
img = np.array(img.rotate(180))  # Rotate image
# Get different categories
unique_categories1 = df1['Mask'].unique()
unique_categories2 = df2['Mask'].unique()
unique_categories3 = df3['Mask'].unique()
unique_categories4 = df4['Mask'].unique()
unique_categories5 = df5['Mask'].unique()
unique_categories6 = df6['Mask'].unique()
unique_categories7 = df7['Mask'].unique()
unique_categories8 = df8['Mask'].unique()
unique_categories9 = df9['Mask'].unique()

plt.figure(figsize=(8, 8))
plt.imshow(np.array(img), cmap='gray')
color="red"
s=0.1
alp=0.2

for i, category in enumerate(unique_categories1):
    subset = df1[df1['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)

for i, category in enumerate(unique_categories2):
    subset = df2[df2['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)
# for i, category in enumerate(unique_categories3):
#     subset = df3[df3['Mask'] == category]
#     label = category.replace('.tif', '').replace("_", " ")
#     x = img.shape[1] - subset['Point_X']
#     y = img.shape[0] - subset['Frame']
#     plt.scatter(x, y, c=color, marker='o', s=s, label=label)
for i, category in enumerate(unique_categories4):
    subset = df4[df4['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)
for i, category in enumerate(unique_categories5):
    subset = df5[df5['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)
for i, category in enumerate(unique_categories6):
    subset = df6[df6['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)
for i, category in enumerate(unique_categories7):
    subset = df7[df7['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)
for i, category in enumerate(unique_categories8):
    subset = df8[df8['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)
for i, category in enumerate(unique_categories9):
    subset = df9[df9['Mask'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    plt.scatter(x, y, c=color, marker='o', s=s, label=label,alpha=alp)

plt.title('Coronal View')
# plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1.2))

# 调整图的边距以增加空白部分
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.1)

# 移除XY轴刻度
plt.gca().set_xticks([])
plt.gca().set_yticks([])

plt.show()