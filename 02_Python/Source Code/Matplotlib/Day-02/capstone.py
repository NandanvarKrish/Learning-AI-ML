import matplotlib.pyplot as plt
import numpy as np

BRAND = {
    'primary'  : '#6D28D9',
    'secondary': '#0891B2',
    'accent'   : '#F59E0B',
    'dark'     : '#1E1B4B',
    'light'    : '#F5F3FF'
}

plt.rcParams.update({
    'figure.figsize': (10,6),
    'font.family': 'sans-serif',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.edgecolor': BRAND['dark'],
    'axes.titlesize': 15,
    'axes.titleweight': 'bold',
    'axes.grid': True,
    'grid.alpha': 0.25
})

np.random.seed(5)
quarters = ['Q1','Q2','Q3','Q4']
arr_revenue = [120,145,168,210]
segments = ['Enterprise','SMB','Startup']
segment_rev = [95,70,45]
users_daily = np.random.poisson(500, 90) + np.arange(90)*3

fig, axes = plt.subplot_mosaic("""
    AA
    BC
""", figsize = (13, 8), height_ratios = [1.2, 1])

axes['A'].plot(range(90), users_daily, color = BRAND['primary'], linewidth = 2)
axes['A'].fill_between(range(90), users_daily, alpha = 0.15, color = BRAND['primary'])
axes['A'].set_title('Daily Active Users (90-Day Trend)')

bars = axes['B'].bar(quarters, arr_revenue, color=BRAND['secondary'])
axes['B'].set_title('Quarterly Revenue (₹L)')

axes['C'].barh(segments, segment_rev, color=[BRAND['primary'],BRAND['secondary'],BRAND['accent']])
axes['C'].set_title('Revenue by Segment (₹L)')

fig.tight_layout()
plt.show()
