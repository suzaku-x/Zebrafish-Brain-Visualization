import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

csv_file1 = "E:\\new_roi1107\\sixfish\\output_pc 1112_final.csv"
df1 = pd.read_csv(csv_file1)

csv_file2 = "E:\\new_roi1107\\sixfish\\outputstrike1112.csv"
df2 = pd.read_csv(csv_file2)

tif_file = "E:\\Atlas\\final\\yz5.tif"
img = Image.open(tif_file)
img = img.transpose(Image.ROTATE_90)

# unique_categories1 = df1['Mask'].unique()
# unique_categories2 = df2['Mask'].unique()
unique_categories1 = df1['G'].unique()
unique_categories2 = df2['G'].unique()
plt.figure(figsize=(8, 8))
plt.imshow(np.array(img), cmap='gray')

colors1 = '#1f77b4'

for i, category in enumerate(unique_categories1):
    subset = df1[df1['G'] == category]
    # label = category.replace('.tif', '').replace("_", " ")
    x = subset['reg_y']  # 注意：这里x和y轴的坐标互换，因为图像旋转了90度
    y = img.size[1] - subset['reg_z']
    plt.scatter(x, y, c=colors1, marker='o', s=3, label='Hunting Initiation',alpha=0.5)


colors2 = 'magenta'

for i, category in enumerate(unique_categories2):
    subset = df2[df2['G'] == category]
    # label = category.replace('.tif', '').replace("_", " ")
    x = subset['reg_y']
    y = img.size[1] - subset['reg_z']
    plt.scatter(x, y, c=colors2, marker='o', s=3, label='Strike',alpha=0.5)

plt.title('Sagittal View')

legend = plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.35))
for handle in legend.legendHandles:
    handle.set_sizes([30.0])

plt.subplots_adjust(left=0.2, right=0.75, top=0.8, bottom=0.1)

# plt.text(1000,80,"■",fontsize=32, va='center',color='yellow',alpha=0.15)
# plt.text(1100,80,"tectum" ,fontsize=12, va='center',color='black')

plt.text(1000,80,"■",fontsize=32, va='center',color='cyan',alpha=0.15)
plt.text(1100,80,"pretectum" ,fontsize=12, va='center',color='black')

plt.text(1000,180,"■",fontsize=32, va='center',color='green',alpha=0.15)
plt.text(1100,180,"dorsal thalamus" ,fontsize=12, va='center',color='black')

plt.text(1000,280,"■",fontsize=32, va='center',color='red',alpha=0.15)
plt.text(1100,280,"nucleus isthmi" ,fontsize=12, va='center',color='black')

plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.savefig('E:\\Atlas\\final\\plot2.png', dpi=300)
plt.show()
#

