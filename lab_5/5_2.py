import pandas as pd
import numpy as np
import scipy.stats as st


attack_times = [22 ,19, 45, 12, 10, 20, 55, 14, 25, 35, 28, 15, 30, 18, 24]
np.random.seed(15)
info_=np.random.normal(attack_times,size=15)
n = 15

print(np.mean(info_))
print(np.std(info_))

t_critical = st.t.ppf(0.975, df=n - 1)
standard_error =np.std(info_) / np.sqrt(n)

margin = t_critical * standard_error

hight = np.mean(info_) +margin
under =np.mean(info_) - margin

print(f"Критическое значение t: {t_critical:.2f}")
print(f"Вверхняя позиция:{ hight:.2f}")
print(f"Нижняя позиция: { under:.2f}")