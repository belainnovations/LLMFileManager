import matplotlib.pyplot as plt
import pandas as pd

def create_chart(data):
    plt.figure(figsize=(12, 6))
    plt.bar(data.index, data['price'], width=0.02, color='gold')
    plt.title('Current Gold Spot Price', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Add value label above the bar
    for i, price in enumerate(data['price']):
        plt.text(data.index[i], price, f'${price:.2f}', ha='center', va='bottom', fontsize=14)

    # Set y-axis limits to create padding
    plt.ylim(0, max(data['price']) * 1.5)

    # Set x-axis limits to create padding
    plt.xlim(data.index[0] - pd.Timedelta(days=1), data.index[0] + pd.Timedelta(days=1))

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    chart_path = 'examples/test04/gold_price_chart.png'
    plt.savefig(chart_path, dpi=300, bbox_inches='tight')
    plt.close()

    return chart_path
