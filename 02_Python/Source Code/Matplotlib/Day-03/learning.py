import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(1)
# dept_a = np.random.normal(70000, 12000, 100)
# dept_b = np.random.normal(85000, 18000, 100)
# dept_c = np.random.normal(60000, 8000,  100)

# fig, ax = plt.subplots(figsize=(8,6))

# ax.boxplot(dept_a)

# data = [dept_a, dept_b, dept_c]

# ax.boxplot(data,
#            label=['Engineering', 'Sales', 'Support'],
#            patch_artist=True,
#            showmeans=True,
#            notch=True)

# bp = ax.boxplot(data, label=['Eng','Sales','Support'], patch_artist=True)
# colors = ['#6EE7B7', '#93C5FD', '#FDBA74']
# for patch, color in zip(bp['boxes'], colors):
#     patch.set_facecolor(color)

# ax.boxplot(data, label=['Eng','Sales','Support'], vert=False)

# ax.set_title('Salary Distribution by Department')
# ax.set_ylabel('Salary (₹)')


# fig, ax = plt.subplots(figsize=(8,6))

# parts = ax.violinplot(data, showmeans=True, showmedians=True)

# for pc, color in zip(parts['bodies'], colors):
#     pc.set_facecolor(color)
#     pc.set_edgecolor('black')
#     pc.set_alpha(0.8)

# ax.set_xticks([1,2,3])
# ax.set_xticklabels(['Engineering','Sales','Support'])
# ax.set_title('Salary Distribution Shape by Department')

# bimodal = np.concatenate([np.random.normal(50,5,200), np.random.normal(80,5,200)])
# fig2, (ax1,ax2) = plt.subplots(1,2, figsize=(10,5))
# ax1.boxplot(bimodal)
# ax1.set_title('Box Plot — hides bimodal shape!')
# ax2.violinplot(bimodal)
# ax2.set_title('Violin Plot — reveals TWO peaks')

# segments = ['Enterprise','SMB','Startup','Individual']
# revenue  = [450, 280, 150, 70]

# fig, ax = plt.subplots(figsize=(7,7))

# # ax.pie(revenue, labels=segments, autopct='%1.1f%%')

# colors = ['#047857','#10B981','#6EE7B7','#D1FAE5']
# explode = [0.08, 0, 0, 0]

# ax.pie(revenue,
#        labels=segments,
#        colors=colors,
#        explode=explode,
#        autopct='%1.1f%%',
#        startangle=90,
#        shadow=True,
#        textprops={'fontsize':11})

# ax.set_title('Revenue Share by Segment')
# ax.axis('equal')

# fig, ax = plt.subplots(figsize=(7,7))
# wedges, texts, autotexts = ax.pie(revenue, labels=segments, colors=colors,
#                                     autopct='%1.1f%%', pctdistance=0.85)

# centre_circle = plt.Circle((0,0), 0.6, fc='white')
# fig.gca().add_artist(centre_circle)
# ax.text(0,0, f'Total\n₹{sum(revenue)}L', ha='center', va='center', fontsize=14, fontweight='bold')

# data_matrix = np.random.rand(5,5)
# data_matrix = (data_matrix + data_matrix.T) / 2
# np.fill_diagonal(data_matrix, 1.0)

# labels = ['Price','Sqft','Bedrooms','Age','Rating']

# fig, ax = plt.subplots(figsize=(7,6))
# im = ax.imshow(data_matrix, cmap='RdBu_r', vmin=-1, vmax=1)

# ax.set_xticks(range(len(labels)))
# ax.set_yticks(range(len(labels)))
# ax.set_xticklabels(labels, rotation=45, ha='right')
# ax.set_yticklabels(labels)

# for i in range(len(labels)):
#     for j in range(len(labels)):
#         text_color = 'white' if abs(data_matrix[i,j]) > 0.5 else 'black'
#         ax.text(j, i, f'{data_matrix[i,j]:.2f}',
#                 ha='center', va='center', color=text_color, fontsize=10)

# fig.colorbar(im, ax=ax, label='Correlation')
# ax.set_title('Feature Correlation Matrix')
# fig.tight_layout()

# X, Y = np.meshgrid(np.linspace(0,10,50), np.linspace(0,10,50))
# Z = np.sin(X) * np.cos(Y)
# fig, ax = plt.subplots()
# mesh = ax.pcolormesh(X, Y, Z, cmap='viridis', shading='auto')
# fig.colorbar(mesh, ax=ax)

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-(X**2 + Y**2)) * np.cos(2*X)

# fig, ax = plt.subplots(figsize=(7,6))

# cs = ax.contour(X, Y, Z, levels=10, cmap='viridis')
# ax.clabel(cs, inline=True, fontsize=8)

# fig, ax = plt.subplots(figsize=(7,6))
# cf = ax.contourf(X, Y, Z, levels=20, cmap='RdYlBu_r')
# fig.colorbar(cf, ax=ax)
# ax.set_title('Filled Contour Plot')

# fig, ax = plt.subplots(figsize=(7,6))
# cf = ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.8)
# cs = ax.contour(X, Y, Z, levels=10, colors='black', linewidths=0.5)
# fig.colorbar(cf, ax=ax)
# ax.legend()

# fig = plt.figure(figsize=(8,7))
# ax = fig.add_subplot(111, projection='3d')

# x = np.random.rand(100)
# y = np.random.rand(100)
# z = x**2 + y**2
# ax.scatter(x, y, z, c=z, cmap='viridis')
# ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

# fig = plt.figure(figsize=(9,7))
# ax = fig.add_subplot(111, projection='3d')

# x = np.linspace(-5,5,50)
# y = np.linspace(-5,5,50)
# X, Y = np.meshgrid(x,y)
# Z = np.sin(np.sqrt(X**2+Y**2))

# surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none', alpha=0.9)
# fig.colorbar(surf, ax=ax, shrink=0.5)

# ax.view_init(elev=25, azim=45)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xpos, ypos = np.meshgrid([0,1,2],[0,1])
xpos, ypos = xpos.ravel(), ypos.ravel()
heights = [3,5,2,4,6,1]
ax.bar3d(xpos, ypos, 0, 0.8, 0.8, heights, shade=True)

plt.show()
