import csv
import fileinput

input_file = "E:\\new_roi1107\\2023-09-22_F6_2deg\\Plane10_roi_coordinates_0.5.csv"
new_fieldnames = ["label", "y", "x"]

for line in fileinput.input(input_file, inplace=True):
    if fileinput.isfirstline():

        print(",".join(new_fieldnames))
    else:

        print(line, end='')

print(f'Title row of "{input_file}" has been updated to "label", "y", "x".')
