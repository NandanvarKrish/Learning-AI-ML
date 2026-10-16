import matplotlib.pyplot as plt
import numpy as np

np.random.seed(3)

lines = ['Line A', 'Line B', 'Line C', 'Line D']

line_a = np.random.normal(50.0, 0.15, 150)
line_b = np.random.normal(50.2, 0.25, 150)
line_c = np.concatenate([
    np.random.normal(49.8, 0.1, 75),
    np.random.normal(50.3, 0.1, 75)
])
line_d = np.random.normal(50.0, 0.4, 150)

data = [line_a, line_b, line_c, line_d]

factors = ['Temp', 'Speed', 'Pressure', 'Humidity', 'DefectRate']

corr = np.array([
    [1.00, 0.65, 0.20, -0.10, 0.72],
    [0.65, 1.00, 0.15, -0.05, 0.58],
    [0.20, 0.15, 1.00, 0.30, 0.25],
    [-0.10, -0.05, 0.30, 1.00, 0.15],
    [0.72, 0.58, 0.25, 0.15, 1.00]
])

temp = np.linspace(150, 250, 60)
speed = np.linspace(10, 100, 60)
T, S = np.meshgrid(temp, speed)

defect_surface = (
    0.02 * (T - 200) ** 2 / 100
    + 0.01 * (S - 55) ** 2 / 50
)

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

ax1 = axes[0, 0]

bp = ax1.boxplot(
    data,
    label=lines,
    patch_artist=True,
    notch=True,
    showmeans=True
)

box_colors = ['#6EE7B7', '#93C5FD', '#FDBA74', '#C4B5FD']

for patch, color in zip(bp['boxes'], box_colors):
    patch.set_facecolor(color)

ax1.axhline(
    50.0,
    color='red',
    linestyle='--',
    linewidth=2,
    label='Target: 50.0 mm'
)

ax1.set_title('Production Line Dimension Distribution')
ax1.set_ylabel('Dimension (mm)')
ax1.set_xlabel('Production Line')
ax1.legend()
ax1.grid(axis='y', alpha=0.25)

ax2 = axes[0, 1]

vp = ax2.violinplot(
    data,
    showmeans=True,
    showmedians=True
)

for body, color in zip(vp['bodies'], box_colors):
    body.set_facecolor(color)
    body.set_edgecolor('black')
    body.set_alpha(0.8)

ax2.axhline(
    50.0,
    color='red',
    linestyle='--',
    linewidth=2,
    label='Target: 50.0 mm'
)

ax2.set_xticks(range(1, 5))
ax2.set_xticklabels(lines)
ax2.set_title('Production Line Distribution Shape')
ax2.set_ylabel('Dimension (mm)')
ax2.set_xlabel('Production Line')
ax2.legend()
ax2.grid(axis='y', alpha=0.25)

ax3 = axes[1, 0]

im = ax3.imshow(
    corr,
    cmap='RdBu_r',
    vmin=-1,
    vmax=1
)

ax3.set_xticks(range(len(factors)))
ax3.set_yticks(range(len(factors)))
ax3.set_xticklabels(factors, rotation=45, ha='right')
ax3.set_yticklabels(factors)

for i in range(len(factors)):
    for j in range(len(factors)):
        value = corr[i, j]
        text_color = 'white' if abs(value) > 0.5 else 'black'
        ax3.text(
            j,
            i,
            f'{value:.2f}',
            ha='center',
            va='center',
            color=text_color,
            fontsize=10,
            fontweight='bold'
        )

fig.colorbar(im, ax=ax3, label='Correlation')

ax3.set_title('Manufacturing Factor Correlation')

defect_correlations = corr[:-1, -1]
strongest_index = np.argmax(np.abs(defect_correlations))
strongest_factor = factors[strongest_index]
strongest_value = defect_correlations[strongest_index]

ax3.text(
    0.5,
    -0.25,
    f'Strongest correlate: {strongest_factor} ({strongest_value:.2f})',
    transform=ax3.transAxes,
    ha='center',
    fontsize=11,
    fontweight='bold'
)

ax4 = axes[1, 1]

cf = ax4.contourf(
    T,
    S,
    defect_surface,
    levels=20,
    cmap='RdYlGn_r'
)

cs = ax4.contour(
    T,
    S,
    defect_surface,
    levels=8,
    colors='black',
    linewidths=0.6
)

ax4.clabel(
    cs,
    inline=True,
    fontsize=7
)

fig.colorbar(
    cf,
    ax=ax4,
    label='Defect Rate (%)'
)

ax4.plot(
    200,
    55,
    '*',
    color='blue',
    markersize=20,
    markeredgecolor='white',
    markeredgewidth=1.5
)

ax4.annotate(
    'Optimal Point\nT = 200°C, Speed = 55',
    xy=(200, 55),
    xytext=(220, 75),
    arrowprops=dict(
        facecolor='black',
        arrowstyle='->'
    ),
    fontsize=10,
    fontweight='bold'
)

ax4.set_xlabel('Temperature (°C)')
ax4.set_ylabel('Speed (units/min)')
ax4.set_title('Temperature × Speed Process Window')

fig.suptitle(
    'Precision Manufacturing Co. — Manufacturing Quality Control Dashboard',
    fontsize=20,
    fontweight='bold',
    y=0.98
)

fig.text(
    0.5,
    0.01,
    'QC Analysis: Dimensional Tolerance, Distribution Shape, Factor Correlation and Optimal Process Window',
    ha='center',
    fontsize=11
)

plt.tight_layout(rect=[0, 0.04, 1, 0.95])

plt.savefig(
    'manufacturing_qc_dashboard.png',
    dpi=300,
    bbox_inches='tight'
)


print(f'Strongest factor correlated with DefectRate: {strongest_factor:}')
print(f'Correlation value: {strongest_value:.2f}')
print('Target dimension: 50.0 mm')
print('Optimal temperature: 200°C')
print('Optimal speed: 55 units/min')
print('Line C distribution: Bimodal')
print('Line D distribution: Highest variance')
print('Line B distribution: Positive bias from target')

fig.tight_layout()

plt.show()
