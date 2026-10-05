import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)
test_data = np.random.normal(loc =50 ,scale=2 , size= 10_000)
print(f"Задание 1 ")
print(f"Среднее:{np.mean(test_data):.2f}")
print(f"Медиана:{np.median(test_data):.2f}")
print(f"Стандартное отклонение:{np.std(test_data):.2f}")
print(f"Вариация:{(np.std(test_data)/np.mean(test_data))*100:.2f}%")
print(f"Дисперсия:{np.var(test_data):.2f}")
print(f"Min:{np.min(test_data):.2f}")
print(f"Max:{np.max(test_data):.2f}")

# Creat graf
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
ax1.hist(test_data, bins=30, color='blue', edgecolor='black', alpha=0.7)
ax1.set_title('Распределение времени отклика')
ax1.set_xlabel('Время отклика')
ax1.set_ylabel('Частота')

ax2.boxplot(test_data, vert=True, patch_artist=True, showmeans=True, meanline=False)
ax2.set_title('Базовые показатели времени отклика')
ax2.set_ylabel('Время отклика')
plt.show()
