import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Input csv
csv_file = "E:\\new_roi1107\\sixfish\\output_pc1110.csv"
df = pd.read_csv(csv_file)

# Input tif
tif_file = "E:\\Atlas\\AVGxy_HSA.tif"
img = Image.open(tif_file)

# Get different categories
unique_categories = df['Combined_Label'].unique()

plt.figure(figsize=(8, 8))
plt.imshow(np.array(img), cmap='gray')


# colors = ['blue', 'red', 'green', 'purple', 'orange','pink','yellow']  # 8 colors
colors=['magenta']
colors=['#1f77b4']
for i, category in enumerate(unique_categories):
    subset = df[df['Combined_Label'] == category]
    # label = category.replace('.tif', '').replace("_", " ")
    plt.scatter(subset['reg_x'], subset['reg_y'], c=colors[i % len(colors)], marker='o', s=0.01,alpha=1)

plt.title('Horizontal View')
# plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1.2))

# legend = plt.legend(loc='upper right', bbox_to_anchor=(1.64, 1.29))
# for handle in legend.legendHandles:
#     handle.set_sizes([20.0])  # Set dot size 20.0

plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.1)
# Remove xy scale
plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.show()
#
#
