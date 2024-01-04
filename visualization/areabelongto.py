import pandas as pd

a="E:\\registration\\roiresult\\RGB_Valuesroi.csv"
df = pd.read_csv(a)
filtered_df = df[df['RGB_Value'] == 255]
result = filtered_df.groupby(['Frame', 'Point_X', 'Point_Y'])['Mask'].unique().reset_index()
result['Mask'] = result['Mask'].apply(list)


result.to_csv('ROIcheck.csv', index=False)
