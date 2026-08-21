import matplotlib.pyplot as plt
import numpy as np

# 数据：Base, Depth_init, Earlystop, Ours
scenes = ['Courtyard', 'Office', 'Pipes', 'Terrains']
base = [6.63, 5.01, 5.16, 4.51]
depth = [4.28, 4.46, 4.96, 4.40]
early = [4.31, 4.38, 4.97, 4.40]
ours = [4.21, 4.46, 4.85, 4.25]

x = np.arange(len(scenes))
width = 0.18

fig, ax = plt.subplots(figsize=(8, 4))

# 绘制柱状图
rects1 = ax.bar(x - 1.5*width, base, width, label='Base', color='#95a5a6')
rects2 = ax.bar(x - 0.5*width, depth, width, label='Depth_Init', color='#3498db')
rects3 = ax.bar(x + 0.5*width, early, width, label='EarlyStop', color='#f1c40f')
rects4 = ax.bar(x + 1.5*width, ours, width, label='Ours', color='#e74c3c')

# 自动在柱子上方添加数值标签
ax.bar_label(rects1, padding=3, fontsize=7, rotation=90)
ax.bar_label(rects2, padding=3, fontsize=7, rotation=90)
ax.bar_label(rects3, padding=3, fontsize=7, rotation=90)
ax.bar_label(rects4, padding=3, fontsize=7, rotation=90)

# 图表美化
ax.set_ylabel('Training Time (Min)', fontsize=10)
ax.set_xticks(x)
ax.set_xticklabels(scenes, fontsize=10)
ax.legend(loc='upper right', fontsize=8, ncol=4, frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('efficiency_with_labels.pdf', dpi=300)