import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Input csv
csv_file = "E:\\new_roi1107\\result1107\\RGB_Values_pc.csv"
df = pd.read_csv(csv_file)

# filter one mask
filtered_df = df[df['Mask'].isin([ 'tectal_neuropil.tif'])]  # 请将'ColumnName'替换为实际的列名

# Input tif
tif_file = "E:\\AVG_tectal_neuropil.tif"
img = Image.open(tif_file)

plt.figure(figsize=(8, 8))
plt.imshow(np.array(img), cmap='gray')

# plot
plt.scatter(filtered_df['Point_X'], filtered_df['Point_Y'], c='blue', marker='o', s=3)
plt.title('tectal_neuropil')
plt.show()
