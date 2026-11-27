
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from pathlib import Path

data = {
    'cash': 942.498,
    'todayCash': 9053.299,
    'Rev00016': 348.8300000005,
    'Rev00013': 31.99993,
    'Rev00015': 92.36,
    'Rev00017': 287.34,
    'Rev00020': 296.1,
    'Rev00018': 47.54,
    'Rev00045': 77.00
}

revTypes = {
    'Rev00016': {'name': 'Petty cash', 'connectedTo': 'Physical'},
    'Rev00013': {'name': 'Debit card', 'connectedTo': 'HDFC'},
    'Rev00015': {'name': 'PhonePe', 'connectedTo': 'ICICI'},
    'Rev00017': {'name': 'Google pay', 'connectedTo': 'SBI'},
    'Rev00020': {'name': 'UPI', 'connectedTo': 'ICICI'},
    'Rev00018': {'name': 'Credit card', 'connectedTo': 'SBI'}
}


def get_rev_name(revId):
    return revTypes.get(revId, {}).get('name', 'Unknown')

total = sum(
    value for key, value in data.items()
    if key.startswith('Rev')
)

print("Total Revenue:", f"{total:.3f}")


names = []
values = []

print("\nRevenue Details:")

for key, value in data.items():
    if key.startswith('Rev'):
        name = get_rev_name(key)

        names.append(name)
        values.append(value)

        print(f"{name}: {value:.3f}")

plt.figure(figsize=(10, 6))

bars = plt.bar(names, values)

plt.xlabel("Revenue Types")
plt.ylabel("Revenue Amount")
plt.title("Revenue Analysis")
plt.gca().yaxis.set_major_formatter(
    FormatStrFormatter('%.3f')
)
for bar, value in zip(bars, values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{value:.3f}',
        ha='center',
        va='bottom'
    )

plt.xticks(rotation=30)
plt.tight_layout()

output_path = Path(__file__).resolve().parent / "revenue_plot.png"
plt.savefig(output_path, dpi=300)

print("\nRevenue plot saved successfully!")

plt.show()
