
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

csv_file = "E:\\new_roi1107\\sixfish\\output_pc11123_copy.csv"
df = pd.read_csv(csv_file)

tif_file = "E:\\Atlas\\xy_test10.tif"
# tif_file="E:\\maskaver\\AVG_pretectum.tif"
img = Image.open(tif_file)

# unique_categories = df['Mask'].unique()
unique_categories = df['Mask'].unique()
plt.figure(figsize=(8, 8))
plt.imshow(np.array(img), cmap='gray')
print(unique_categories)

colors = ['blue', 'red', 'green', 'purple', 'orange','pink']
# colors=['magenta']
# colors=['#1f77b4']
for i, category in enumerate(unique_categories[0:7]):
    subset = df[df['fish'] == category]
    label = category.replace('.tif', '').replace("_", " ")
    plt.scatter(subset['Point_X'], subset['Point_Y'], c=colors[i % len(colors)], marker='o', s=3, label=label)
    plt.scatter(subset['reg_x'],subset['reg_y'],c=colors[i % len(colors)], marker='o', s=3, label=category)
plt.title('Horizontal View')
plt.legend(loc='upper right', bbox_to_anchor=(1.45, 1.2))

legend = plt.legend(loc='upper right', bbox_to_anchor=(1.64, 1.29))
for handle in legend.legendHandles:
    handle.set_sizes([20.0])

plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.1)

plt.gca().set_xticks([])
plt.gca().set_yticks([])
plt.show()
#
#
