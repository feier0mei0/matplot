# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# edgecolor='none'，删除数据点的轮廓，黑色变为蓝色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标轴加标签
plt.title("Squares Numbers1", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')

