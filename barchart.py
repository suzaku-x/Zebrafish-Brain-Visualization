import csv
import matplotlib.pyplot as plt

data = []
group_names = []
width=0.5

with open("E:\\new_roi1107\\sixfish\\TIF_File_Counts_pc1112_2.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)

    next(reader)
    for row in reader:
        label = row[0].replace("_", " ")
        group_names.append(label)
        data.append(int(row[2]))

plt.bar(group_names, data,width=width,color='#1f77b4')
##1f77b4
plt.title('PC Distribution')
plt.xlabel('brain areas')
plt.ylabel('# of neurons')


plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pc.png', bbox_inches='tight')
plt.show()
