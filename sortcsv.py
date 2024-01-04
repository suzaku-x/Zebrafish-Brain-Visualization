import pandas as pd

df = pd.read_csv("E:\\new_roi1107\\sixfish\\0811F8\\RGB_Values10.csv")

# grouped = df.groupby(['Point_X', 'Point_Y', 'Frame'])
grouped=df.groupby(['label'])

def combine_labels(group):
    if (group['RGB_Value'] == 0).all():
        group['Combined_Label'] = 'None'
    elif (group['RGB_Value'] != 0).any():
        non_zero_labels = group.loc[group['RGB_Value'] != 0, 'Mask'].tolist()
        group['Combined_Label'] = ','.join(non_zero_labels)
    return group

df = grouped.apply(combine_labels)


df.reset_index(drop=True, inplace=True)
df.drop(df.columns[0], axis=1, inplace=True)
df.drop(df.columns[3], axis=1, inplace=True)
df.drop_duplicates(inplace=True)


output_path = "E:\\new_roi1107\\sixfish\\0811F8\\RGB_Values10_1.csv" # Replace this with your own path
df.to_csv(output_path, index=False)



