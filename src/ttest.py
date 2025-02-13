from scipy.stats import ttest_ind
from scipy.stats import describe

def normalize(arr):
    return (arr[1] / arr[0])

group_1 = [[2027, 528], [1720, 180], [1106, 300], [2265, 273], [380, 70]]
group_2 = [[2031, 581], [411, 120], [2017, 670], [1213, 480], [221, 523]]

sample_1 = list(map(normalize, group_1))
sample_2 = list(map(normalize, group_2))

t_stat, p_value = ttest_ind(sample_1, sample_2, equal_var=False)

print(f"First group seconds normalized: {sample_1}")
print(f"Second group seconds normalized: {sample_2}")
print(f"First group mean: {describe(sample_1).mean}")
print(f"Second group mean: {describe(sample_2).mean}")

print(f"t value: {t_stat}")
print(f"p value: {p_value}")
