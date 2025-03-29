import matplotlib.pyplot as plt
import numpy as np

# Normalization function
def normalize(arr):
    return arr[0]

# Data for the two groups
group_1 = [[2027, 528], [1720, 180], [1106, 300], [2265, 273], [380, 70]]
group_2 = [[2031, 581], [411, 120], [2017, 670], [1213, 480]]

# Apply normalization
sample_1 = list(map(normalize, group_1))
sample_2 = list(map(normalize, group_2))

# Compute means
mean_1 = np.mean(sample_1)
mean_2 = np.mean(sample_2)

# Create box plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.boxplot([sample_1, sample_2], labels=["Grupa 1", "Grupa 2"])

# Add mean lines
ax.axhline(mean_1, linestyle="dashed", color="blue", label=f"Średnia grupy 1: {mean_1:.2f}")
ax.axhline(mean_2, linestyle="dashed", color="orange", label=f"Średnia grupy 2: {mean_2:.2f}")

# Labels and title
ax.set_title("Porównanie T1 pomiędzy grupami")
ax.set_ylabel("T1")
ax.set_xlabel("Grupy")
ax.legend()

# Save the plot as a PNG file
output_filename = "../diagramy/normalized_time_comparison_first.png"
plt.savefig(output_filename, dpi=300, bbox_inches='tight')  # High-quality output

print(f"Plot saved as {output_filename}")