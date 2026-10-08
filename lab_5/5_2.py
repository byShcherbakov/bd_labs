import pandas as pd
import numpy as np
import scipy.stats as st


attack_times = [22 ,19, 45, 12, 10, 20, 55, 14, 25, 35, 28, 15, 30, 18, 24]

n = len(attack_times)
n = 15

print(np.mean(attack_times))
print(np.std(attack_times))

t_critical = st.t.ppf(0.975, df=n - 1)
standard_error =np.std(attack_times) / np.sqrt(n)

margin = t_critical * standard_error

hight = np.mean(attack_times) +margin
under =np.mean(attack_times) - margin

print(f"Критическое значение t: {t_critical:.2f}")
print(f"Вверхняя позиция:{ hight:.2f}")
print(f"Нижняя позиция: { under:.2f}")