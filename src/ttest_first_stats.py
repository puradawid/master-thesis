from scipy.stats import ttest_ind
from scipy.stats import describe
import numpy as np

def normalize(arr):
    return arr[0]

group_1 = [[2027, 528], [1720, 180], [1106, 300], [2265, 273], [380, 70]]
group_2 = [[2031, 581], [411, 120], [2017, 670], [1213, 480]]

sample_1 = list(map(normalize, group_1))
sample_2 = list(map(normalize, group_2))

t_stat, p_value = ttest_ind(sample_1, sample_2, equal_var=False)

median_1 = np.median(sample_1)
median_2 = np.median(sample_2)

basic_stats = [
[
    "odchylenie standardowe",
    "średnia",
    "mediana",
    "25 percentyl",
    "75 percentyl"
],
[
    lambda x: np.std(x),
    lambda x: np.mean(x),
    lambda x: np.median(x),
    lambda x: np.percentile(x, 25),
    lambda x: np.percentile(x, 75)
]
]

samples = [{"name": "Grupa 1", "data": sample_1}, {"name" : "Grupa 2", "data": sample_2}]

for basic_stat in basic_stats[0]:
    print(basic_stat + " & ", end = "")
print("\\\\")
for sample in samples:
    sample_results = [stat(sample["data"]) for stat in basic_stats[1]]
    print(" & ".join(map(str, sample_results)) + " \\\\")

print(f"First group seconds normalized: {sample_1}")
print(f"Second group seconds normalized: {sample_2}")
print(f"First group mean: {describe(sample_1).mean}")
print(f"Second group mean: {describe(sample_2).mean}")

print(f"t value: {t_stat}")
print(f"p value: {p_value}")
