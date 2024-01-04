
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


csv_file1 = "E:\\new_roi1107\\sixfish\\output_pc_final111.csv"
df1 = pd.read_csv(csv_file1)


csv_file2 = "E:\\new_roi1107\\sixfish\\outputstrike1112.csv"
df2 = pd.read_csv(csv_file2)


tif_file = "E:\\Atlas\\final\\xy8.tif"
img = Image.open(tif_file)


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
    plt.scatter(subset['reg_x'], subset['reg_y'], c=colors1, marker='o', s=3, label='Hunting Initiation',alpha=0.5)


colors2 = 'magenta'
for i, category in enumerate(unique_categories2):
    subset = df2[df2['G'] == category]
    # label = category.replace('.tif', '').replace("_", " ")
    plt.scatter(subset['reg_x'], subset['reg_y'], c=colors2, marker='o', s=3, label='Strike',alpha=0.5)

plt.title('Horizontal View')
legend = plt.legend(loc='upper right', bbox_to_anchor=(1.5, 1.1))
for handle in legend.legendHandles:
    handle.set_sizes([30.0])

# plt.xlim(0, 800)
# plt.ylim(0, 1000)

plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.1)
# plt.margins(660, 180, marker='s', color='red')
# plt.text(600,180,"■",fontsize=32, va='center',color='yellow',alpha=0.23)
# plt.text(680,180,"tectum" ,fontsize=12, va='center',color='black')

plt.text(600,260,"■",fontsize=32, va='center',color='cyan',alpha=0.23)
plt.text(680,260,"pretectum" ,fontsize=12, va='center',color='black')

plt.text(600,340,"■",fontsize=32, va='center',color='green',alpha=0.23)
plt.text(680,340,"dorsal thalamus" ,fontsize=12, va='center',color='black')

plt.text(600,420,"■",fontsize=32, va='center',color='red',alpha=0.23)
plt.text(680,420,"nucleus isthmi" ,fontsize=12, va='center',color='black')

plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.savefig('E:\\Atlas\\final\\plot1.png', dpi=300)
plt.show()