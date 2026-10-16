import matplotlib.pyplot as plt
import numpy as np

def generate_dashboard(months, rev_23, rev_24, depts, dept_rev, spend, ad_spend, sales_gen):
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Horizon Retail — Q4 2024 Board Report', fontsize=16, fontweight='bold')

    # Top-Left: Revenue Trend Line
    ax_line = axes[0, 0]
    ax_line.plot(months, rev_23, color='#94A3B8', linestyle='--', marker='o', linewidth=2, label='2023')
    ax_line.plot(months, rev_24, color='#0284C7', linestyle='-', marker='s', linewidth=2.5, label='2024')
    ax_line.set_title('Monthly Revenue Trend (2023 vs 2024)', fontsize=12, fontweight='600')
    ax_line.set_xlabel('Month')
    ax_line.set_ylabel('Revenue (₹ Lakhs)')
    ax_line.legend(loc='upper left')
    ax_line.grid(True, linestyle=':', alpha=0.5)

    # Top-Right: Horizontal Department Revenue
    ax_bar = axes[0, 1]
    sort_idx = np.argsort(dept_rev)
    sorted_depts = [depts[i] for i in sort_idx]
    sorted_rev = dept_rev[sort_idx]
    
    bars = ax_bar.barh(sorted_depts, sorted_rev, color='#059669', height=0.6)
    for bar in bars:
        w = bar.get_width()
        ax_bar.text(w + 5, bar.get_y() + bar.get_height() / 2, f'₹{w:.1f}L', va='center', fontsize=9)
    ax_bar.set_title('Department Revenue Breakdown', fontsize=12, fontweight='600')
    ax_bar.set_xlabel('Revenue (₹ Lakhs)')
    ax_bar.set_xlim(0, max(sorted_rev) * 1.18)

    # Bottom-Left: Customer Spending Distribution
    ax_hist = axes[1, 0]
    ax_hist.hist(spend, bins=30, color='#6366F1', edgecolor='white', alpha=0.85)
    mean_val, med_val = np.mean(spend), np.median(spend)
    ax_hist.axvline(mean_val, color='#EF4444', linestyle='--', linewidth=2, label=f'Mean: ₹{mean_val:.1f}')
    ax_hist.axvline(med_val, color='#F59E0B', linestyle='-', linewidth=2, label=f'Median: ₹{med_val:.1f}')
    ax_hist.set_title('Customer Spending Distribution', fontsize=12, fontweight='600')
    ax_hist.set_xlabel('Spend Amount (₹)')
    ax_hist.set_ylabel('Frequency')
    ax_hist.legend(loc='upper right')

    # Bottom-Right: Ad Spend vs Sales Scatter with Fit Line
    ax_sc = axes[1, 1]
    ax_sc.scatter(ad_spend, sales_gen, color='#0EA5E9', edgecolors='#0369A1', s=60, alpha=0.8)
    z = np.polyfit(ad_spend, sales_gen, 1)
    p = np.poly1d(z)
    x_line = np.linspace(ad_spend.min(), ad_spend.max(), 100)
    ax_sc.plot(x_line, p(x_line), color='#DC2626', linestyle='--', linewidth=2,
               label=f'Fit: y={z[0]:.2f}x + {z[1]:.1f}')
    ax_sc.set_title('Ad Spend vs Sales Generated', fontsize=12, fontweight='600')
    ax_sc.set_xlabel('Ad Spend (₹ Lakhs)')
    ax_sc.set_ylabel('Sales Generated (₹ Lakhs)')
    ax_sc.legend(loc='upper left')

    # Polish: remove top/right spines
    for ax in axes.flat:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    fig.tight_layout()
    fig.savefig('horizon_dashboard.png', dpi=200, bbox_inches='tight')
    plt.show()