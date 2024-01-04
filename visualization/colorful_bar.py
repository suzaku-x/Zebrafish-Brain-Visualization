import csv
import matplotlib.pyplot as plt

data = []
group_names = []
width = 0.5

# 颜色列表，每个柱子对应一个颜色
# colors = ['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'pink','maroon', 'yellow']
# colors = ['blue', 'red', 'green', 'purple', 'orange', 'pink', 'yellow']
colors=['yellow','orange','red','pink','blue','green','purple']
# colors=['#1f77b4']*9
colors='magenta'
# 打开CSV文件
with open("E:\\registration\\update1107\\result\\TIF_File_Counts_strike.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过标题行

    for row in reader:
        label = row[0].replace("_", " ")
        group_names.append(label)
        data.append(int(row[2]))
        print(label)

# 绘制柱状图时为每个柱子分配颜色
plt.bar(group_names, data, width=width, color=colors)

plt.title('Strike Neuron Distribution')
plt.xlabel('brain areas')
plt.ylabel('# of neurons')

# 旋转x轴标签，以防止重叠
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig('fig.png', bbox_inches='tight')
plt.show()  # 显示图形
