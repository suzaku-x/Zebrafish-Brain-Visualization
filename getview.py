import csv
import matplotlib.pyplot as plt
import tifffile
import os
import numpy as np

image_width = 597
image_height = 974
mask_path="E:\\Atlas\\HSA.tif"
# mask_path="E:\\newmasks\HSA_Masks\\tectum.tif"
# "E:\newmasks\HSA_Masks\nucleus_isthmi.tif"
# "E:\newmasks\HSA_Masks\dorsal_thalamus_proper.tif"
# "E:\Atlas\HSA.tif"

tif_data = tifffile.imread(mask_path)
average_xy = np.mean(tif_data, axis=1)
max_intensity_xy = np.max(tif_data, axis=1)
mode_intensity_xy = np.median(tif_data, axis=2)
plt.imshow(average_xy.astype(np.uint8))


plt.gca().set_xticks([])
plt.gca().set_yticks([])

tifffile.imsave("E:\\Atlas\\HSA_xznew.tif", average_xy.astype(np.uint8))
plt.show()