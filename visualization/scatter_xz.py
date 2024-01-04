import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

csv_file = "E:\\registration\\newresult\\RGB_Values_pc.csv"
df = pd.read_csv(csv_file)

tif_file = "E:\\Atlas\\AVGxz_HSA.tif"
img = Image.open(tif_file)

img = np.array(img.rotate(180))
unique_categories = df['Mask'].unique()

plt.figure(figsize=(8, 8))
plt.imshow(img, cmap='gray')

colors = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'yellow']
colors=['#1f77b4']*21
for i, category in enumerate(unique_categories):
    subset = df[df['Mask'] == category]

    x = img.shape[1] - subset['Point_X']
    y = img.shape[0] - subset['Frame']
    label = category.replace('.tif', '').replace("_", " ")
    plt.scatter(x, y, c=colors[i % len(colors)], marker='o', s=3, label=label)

plt.title('Coronal View')

# legend = plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.44))
# for handle in legend.legendHandles:
#     handle.set_sizes([20.0])  # 设置圆点大小为20.0

plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.show()