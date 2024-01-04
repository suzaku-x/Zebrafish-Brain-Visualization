import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

csv_file = "E:\\registration\\newresult\\RGB_Values_pc.csv"
df = pd.read_csv(csv_file)

tif_file = "E:\\Atlas\\AVGyz_HSA.tif"
img = Image.open(tif_file)

img = img.transpose(Image.ROTATE_90)

unique_categories = df['Mask'].unique()

plt.figure(figsize=(8, 8))
plt.imshow(np.array(img), cmap='gray')

colors = ['blue', 'red', 'green', 'purple', 'orange', 'pink','yellow']
colors=['#1f77b4']*21
for i, category in enumerate(unique_categories):
    subset = df[df['Mask'] == category]

    x = subset['Point_Y']
    y = img.size[1] - subset['Frame']
    label = category.replace('.tif', '').replace("_", " ")
    plt.scatter(x, y, c=colors[i % len(colors)], marker='o', s=3, label=label)

plt.title('Sagittal View')

# legend = plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.72))
# for handle in legend.legendHandles:
#     handle.set_sizes([20.0])  # 设置圆点大小为20.0

plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.show()
