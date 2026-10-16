import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.title('Sine Wave')
# plt.xlabel('x')
# plt.ylabel('y')

# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Sine Wave')
# ax.set_xlabel('x')
# ax.set_ylabel('y')

# data = np.random.randn(10)
# fig, ax = plt.subplots()
# ax.plot(data)

# fig, ax = plt.subplots(figsize=(10, 6), dpi=100) 

# fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,6))
# print(axes.shape)

# axes[0,0].plot(x, y)
# axes[0,1].plot(x, np.cos(x))
# axes[1,0].plot(x, np.tan(x))
# axes[1,1].plot(x, 1/(np.tan(x)))

# fig.savefig('my_chart.png', dpi=300, bbox_inches='tight')
# fig.savefig('my_chart.pdf')
# fig.savefig('my_chart.svg')

# fig.tight_layout() 
# plt.subplots_adjust(hspace=0.4, wspace=0.3)

# fig, ax = plt.subplots(figsize=(8,5))

months = ['Jan','Feb','Mar','Apr','May','Jun']
revenue_2023 = [45,52,48,61,58,67]
revenue_2024 = [50,55,60,65,70,75]

# ax.plot(months, revenue_2023, label='2023')
# ax.plot(months, revenue_2024, label='2024')

# ax.plot(months, revenue_2023,
#         color="#0B316F",        # hex color code
#         linewidth=2.0,
#         linestyle='-.',           # '-' solid, '--' dashed, ':' dotted, '-.' dash-dot
#         marker='o',               # circle markers at each point
#         markersize=8,
#         label='2023 Revenue',
#         alpha=0.8)               # transparency 0-1

# ax.plot(months, revenue_2024, 'ro-.')  # red circles, dashed line
# ax.plot(months, revenue_2023, 'go-')   # green triangles, solid line
# ax.plot(months, revenue_2024, 'bs:')   # blue squares, dotted line

# ax.set_title('Monthly Revenue Comparison', fontsize=14, fontweight='bold')
# ax.set_xlabel('Month')
# ax.set_ylabel('Revenue (₹ Lakhs)')
# ax.legend(loc='upper left')     # shows the label= entries
# ax.grid(True, alpha=0.3)         # light gridlines

# fig, ax1 = plt.subplots(figsize=(8,5))

# ax1.plot(months, revenue_2024, 'b-', label='Revenue')
# ax1.set_xlabel('Month')
# ax1.set_ylabel('Revenue (₹L)', color='b')
# ax1.tick_params(axis='y', labelcolor='b')

# ax2 = ax1.twinx()
# units_sold = [1200,1350,1100,1600,1450,1800]
# ax2.plot(months, units_sold, 'r--', label='Units Sold')
# ax2.set_ylabel('Units Sold', color='r')
# ax2.tick_params(axis='y', labelcolor='r')

# fig.tight_layout()

# np.random.seed(42)
# study_hours = np.random.uniform(1, 10, 50)
# exam_scores = study_hours * 7 + np.random.normal(0, 8, 50) + 20

# fig, ax = plt.subplots(figsize=(8,6))

# ax.scatter(study_hours, exam_scores)
# attendance = np.random.uniform(60, 100, 50)

# sc = ax.scatter(study_hours, exam_scores, 
#                 c=attendance, 
#                 cmap='viridis', 
#                 s=80, 
#                 alpha=0.7)

# cbar = fig.colorbar(sc, ax=ax)
# cbar.set_label('Attendance %')

# ax.set_title('Study Hours vs Exam Scores')
# ax.set_xlabel('Study Hours per Week')
# ax.set_ylabel('Exam Score')

# z = np.polyfit(study_hours, exam_scores, 1)
# p = np.poly1d(z)
# x_line = np.linspace(study_hours.min(), study_hours.max(), 100)
# ax.plot(x_line, p(x_line), 'r--', linewidth=2, label=f'Trend: y={z[0]:.1f}x+{z[1]:.1f}')
# ax.legend()

# depts = ['Eng','Sales','Mktg','HR','Finance']
# headcount_2023 = [45,30,20,15,18]
# headcount_2024 = [52,35,22,16,20]

# fig, ax = plt.subplots(figsize=(8,5))
# ax.bar(depts, headcount_2024, color='#0284C7')
# ax.set_title('Headcount by Department (2024)')

# fig, ax = plt.subplots(figsize=(8,5))
# ax.barh(depts, headcount_2024, color='#059669')

# fig, ax = plt.subplots(figsize=(9,5))
# x = np.arange(len(depts))

# width = 0.35

# ax.bar(x - width/2, headcount_2023, width, label='2023', color='#93C5FD')
# ax.bar(x + width/2, headcount_2024, width, label='2024', color='#0284C7')
# ax.set_xticks(x)
# ax.set_xticklabels(depts)
# ax.legend()
# ax.set_title('Headcount: 2023 vs 2024')

# fig, ax = plt.subplots(figsize=(8,5))
# male = [25,18,10,6,9]
# female = [20,12,10,9,9]
# ax.bar(depts, male, label='Male', color='#3B82F6')
# ax.bar(depts, female, bottom=male, label='Female', color='#F472B6')  # bottom= stacks it

# ax.legend()

# bars = ax.bar(depts, headcount_2024, color='#0284C7')
# for bar in bars:
#     height = bar.get_height()
#     ax.text(bar.get_x() + bar.get_width()/2, height + 0.5,
#             str(int(height)), ha='center', fontsize=10)

# scores = np.random.normal(70, 12, 500)
# fig, ax = plt.subplots(figsize=(8,5))
# # ax.hist(scores, bins=20)

# ax.hist(scores,
#         bins=25,                # number of bins (bars)
#         color='#0284C7',
#         edgecolor='white',       # border between bars
#         alpha=0.85)

# class_a = np.random.normal(70, 10, 300)
# class_b = np.random.normal(78, 8, 300)
# ax.hist(class_a, bins=20, alpha=0.5, label='Class A', color='#3B82F6')
# ax.hist(class_b, bins=20, alpha=0.5, label='Class B', color='#F97316')
# ax.legend()

# ax.hist(scores, bins=25, density=True)
# ax.axvline(scores.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {scores.mean():.1f}')
# ax.legend()

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(months, revenue_2024, marker='o')

ax.set_title('2024 Monthly Revenue', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Revenue (₹ Lakhs)', fontsize=12)

ax.set_xlim(-0.5, 5.5)
ax.set_ylim(0, 100)

ax.set_yticks([0,25,50,75,100])
ax.set_yticklabels(['₹0L','₹25L','₹50L','₹75L','₹100L'])

ax.tick_params(axis='x', rotation=45)

ax.annotate('Peak!',
            xy=(5, 75),
            xytext=(4, 85),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=11)

ax.text(0.5, 90, 'Q1 Growth Phase', fontsize=10, color='gray')

ax.legend(loc='best')
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1))

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
