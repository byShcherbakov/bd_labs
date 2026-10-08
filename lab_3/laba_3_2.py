import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

pravila_block = np.random.lognormal(mean=np.log(150),sigma=((np.log(10_000)-np.log(150))/2.33),size=100000)

print(f"Задание 2 ")
print(f"Среднее:{np.mean(pravila_block):.2f}")
print(f"Медиана:{np.median(pravila_block):.2f}")
print(f"Стандартное отклонение:{np.std(pravila_block):.2f}")
print(f"Вариация:{(np.std(pravila_block)/np.mean(pravila_block))*100:.2f}%")
print(f"Дисперсия:{np.var(pravila_block):.2f}")
print(f"Min:{np.min(pravila_block):.2f}")
print(f"25-й перцентиль: {np.percentile(pravila_block, 25):.2f}")
print(f"75-й перцентиль: {np.percentile(pravila_block, 75):.2f}")
print(f"99-й перцентиль: {np.percentile(pravila_block, 99):.2f}")
print(f"Max:{np.max(pravila_block):.2f}")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.hist(pravila_block, bins=30, color='blue', edgecolor='black', alpha=0.7)
ax1.set_title('Распределение времени отклика')
ax1.set_xlabel('Время отклика')
ax1.set_ylabel('Частота')

ax2.boxplot(pravila_block, vert=True, patch_artist=True, showmeans=True, meanline=False)
ax2.set_title('Базовые показатели времени отклика')
ax2.set_ylabel('Время отклика')
plt.show()
