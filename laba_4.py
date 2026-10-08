import math

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

for i in range(1, 4):

    ax1.axvline(df['response_time_ms'].mean() + i * df['response_time_ms'].std(), color='orange', linestyle='--', linewidth=1.5,
                label=f'±{i}σ' if i == 1 else "")  # label пишем один раз, чтобы не дублировать в легенде


    ax1.axvline(df['response_time_ms'].mean() - i * df['response_time_ms'].std(), color='orange', linestyle='--', linewidth=1.5)

print('Пункт 3')
print('Вычисление сигм %')


mean_v = df['response_time_ms'].mean()
std_v = df['response_time_ms'].std()
total_len = len(df)

print(f"Реальный % в пределах ±1 сигма: {(len(df[df['response_time_ms'].between(mean_v - 1*std_v, mean_v + 1*std_v)]) / total_len) * 100:.2f}%")
print(f"Реальный % в пределах ±2 сигма: {(len(df[df['response_time_ms'].between(mean_v - 2*std_v, mean_v + 2*std_v)]) / total_len) * 100:.2f}%")
print(f"Реальный % в пределах ±3 сигма: {(len(df[df['response_time_ms'].between(mean_v - 3*std_v, mean_v + 3*std_v)]) / total_len) * 100:.2f}%")


print('Пункт 4')
arr = []
i = 0

df['z_score'] = (df['response_time_ms']-mean_v)/std_v
while i <total_len:
    if math.fabs(df['z_score'].iloc[i]) > 3:
        arr.append(df.iloc[i])

    i+=1
df_anomalies = pd.DataFrame(arr)
print(f" Количество найденных аномалий (|Z| > 3): {len(df_anomalies)}")
if len(df_anomalies) > 0:
    for idx in range(min(5, len(df_anomalies))):
        print(f"Значение {idx+1}: Дата: {df_anomalies['Date'].iloc[idx]} | Время: {df_anomalies['response_time_ms'].iloc[idx]:.2f} мс | Z-Score: {df_anomalies['z_score'].iloc[idx]:.4f}")
else:
    print("Строк с критическими аномалиями (|Z| > 3) в данном логе не обнаружено.")


print('Пункт 5')
print(f'Асимметрия:{scipy.stats.skew(df['response_time_ms']):.2f}')
print(f'Эксцесс:{scipy.stats.kurtosis(df['response_time_ms']):.2f}')

plt.style.use('seaborn-v0_8-whitegrid')


plt.figure(figsize=(10, 4))

plt.boxplot(
    df["response_time_ms"],
    vert=False,
    patch_artist=True,
    boxprops=dict(facecolor="lightblue", color="blue"),
    flierprops=dict(markerfacecolor="red", marker="D")
)

plt.title("Box Plot (Ящик с усами) для времени отклика веб-сервера", fontsize=14)
plt.xlabel("Время отклика (мс)", fontsize=12)
plt.grid(axis='x', alpha=0.5)


plt.show()

ax1.set_title('Распределение времени отклика')
ax1.set_xlabel('Время отклика')
ax1.set_ylabel('Частота')
plt.show()


