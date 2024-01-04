import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


csv_file1 = "E:\\new_roi1107\\sixfish\\output_pc 1112_final.csv"
df1 = pd.read_csv(csv_file1)

csv_file2 = "E:\\new_roi1107\\sixfish\\outputstrike1112.csv"
df2 = pd.read_csv(csv_file2)


tif_file = "E:\\Atlas\\final\\xz5.tif"
img = Image.open(tif_file)
img = np.array(img.rotate(180))

unique_categories1 = df1['G'].unique()
unique_categories2 = df2['G'].unique()

plt.figure(figsize=(8, 8))
plt.imshow(img, cmap='gray')

colors1 = '#1f77b4'
for i, category in enumerate(unique_categories1):
    subset = df1[df1['G'] == category]
    #label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['reg_x']
    y = img.shape[0] - subset['reg_z']
    plt.scatter(x, y, c=colors1, marker='o', s=3, label="Hunting Initiation",alpha=0.5)


# colors2 = ['magenta'] * len(unique_categories2)
color2='magenta'
for i, category in enumerate(unique_categories2):
    subset = df2[df2['G'] == category]
    #label = category.replace('.tif', '').replace("_", " ")
    x = img.shape[1] - subset['reg_x']
    y = img.shape[0] - subset['reg_z']
    plt.scatter(x, y, c=color2, marker='o', s=3, label='Strike',alpha=0.5)

plt.title('Coronal View')

plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.1)

plt.gca().set_xticks([])
plt.gca().set_yticks([])
legend = plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.25))
for handle in legend.legendHandles:
    handle.set_sizes([30.0])
plt.subplots_adjust(left=0.1, right=0.65, top=0.95, bottom=0.1)
# plt.margins(660, 180, marker='s', color='red')
# plt.text(600,80,"■",fontsize=32, va='center',color='yellow',alpha=0.23)
# plt.text(680,80,"tectum" ,fontsize=12, va='center',color='black')

plt.text(600,140,"■",fontsize=32, va='center',color='cyan',alpha=0.23)
plt.text(680,140,"pretectum" ,fontsize=12, va='center',color='black')

plt.text(600,200,"■",fontsize=32, va='center',color='green',alpha=0.23)
plt.text(680,200,"dorsal thalamus" ,fontsize=12, va='center',color='black')

plt.text(600,260,"■",fontsize=32, va='center',color='red',alpha=0.23)
plt.text(680,260,"nucleus isthmi" ,fontsize=12, va='center',color='black')

plt.savefig('E:\\Atlas\\final\\plot.png', dpi=300)
plt.show()