#инцилизация библиотек
import pandas as pd
import numpy as np



np.random.seed(42) # andom number 42 for 100k
# generation arr info

# Ex_1
classic_data = np.random.normal(loc = 175, scale = 7, size = 100_000)
print("Классическая теория статистики")

print(f"Среднее:{np.mean(classic_data):.2f}")
print(f"Медиана:{np.median(classic_data):.2f}")
print(f"Размах:{np.ptp(classic_data):.2f}")
print(f"Стандартное отклонение:{np.std(classic_data):.2f}")

# Ex_2
big_data = np.random.lognormal(mean=3, sigma=2.5,size=1_000_000)
outliers = np.random.uniform(10_000,50_000,size=10_000)

#add animals in arr
big_data[:10000]  = outliers
print()
print("Big data")
print(f"Среднее: {np.mean(big_data):.2f}")
print(f"Медиана: {np.median(big_data):.2f}")
print(f"Размах: {np.ptp(big_data):.2f}")
print(f"Стандартное отклонение:{np.std(big_data):.2f}")
print(f"Коэффициент вариации:{(np.std(big_data)/np.mean(big_data))*100:.2f}%")
print(f"Коэффициент осцилляции:{(np.ptp(big_data)/np.mean(big_data))*100:.2f}%")

print(f"3_75 квартиль: {np.percentile(big_data, 75):.2f}")
print(f"95 персентель : {np.percentile(big_data, 95):.2f}")
print(f"99 персентель: {np.percentile(big_data, 99):.2f}")

trim_propotion = 0.01
sorted_data = np.sort(big_data)
n = len(sorted_data)
trim_count = int(n * trim_propotion)
trimmed_data = sorted_data [trim_count:n - trim_count]
print()
print("Усеченные данные")
print(f"Среднее: {np.mean(trimmed_data):.2f}")
print(f"Медиана: {np.median(trimmed_data):.2f}")
print(f"Стандартное отклонение: {np.std(trimmed_data):.2f}")
print(f"Коэффициент вариации: {(np.std(trimmed_data) / np.mean(trimmed_data)) * 100:.2f} %")
print(f"3_75 квартиль: {np.percentile(trimmed_data, 75):.2f}")
print(f"95 персентель : {np.percentile(trimmed_data, 95):.2f}")
print(f"99 персентель: {np.percentile(trimmed_data, 99):.2f}")