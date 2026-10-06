import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats


df = pd.read_csv('logs.csv', sep=';', decimal=',')
print(f"Успешно прочитано. Длина: {len(df)}")

print('Этап 2 ')
print(f"Среднее: {df['response_time_ms'].mean():.2f}")
print(f"Стандартное отклонение : {df['response_time_ms'].std():.2f}")
print(f"Минимальное : {df['response_time_ms'].min():.2f}")
print(f"Максимальное  : {df['response_time_ms'].max():.2f}")
print(f"Размах: {np.ptp(df['response_time_ms']):.2f}")

print(f"Коэффициент вариации: {(df['response_time_ms'].std() / df['response_time_ms'].mean()) * 100:.2f} %")
print(f"Коэффициент осцилляции: {(np.ptp(df['response_time_ms']) / df['response_time_ms'].mean()) * 100:.2f} %")
print(f"Дисперсия: {np.var(df['response_time_ms']):.2f}")

fig, (ax1) = plt.subplots(1, 1, figsize=(14, 6))
ax1.hist(df, bins=50, color='blue', edgecolor='black', alpha=0.7)

ax1.axvline(df['response_time_ms'].mean(), color='red', linestyle='-', linewidth=2.5, label=f'Среднее ({df['response_time_ms'].mean():.2f})')

ax1.set_title('Распределение времени отклика')
ax1.set_xlabel('Время отклика')
ax1.set_ylabel('Частота')
plt.show()