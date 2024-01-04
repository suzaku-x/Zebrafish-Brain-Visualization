import pandas as pd


df = pd.read_csv("E:\\new_roi1107\\sixfish\\0705F2\\RGB_Values3_1.csv")
df.drop_duplicates(inplace=True)

output_path = "E:\\new_roi1107\\sixfish\\0705F2\\RGB_Values3_2.csv"
df.to_csv(output_path, index=False)