import pandas as pd
import numpy as np

Speed = [60,120,180,360,720]
count  = len(Speed)
V = 0

for i in range(count):
    V += 1/Speed[i]

total_1_2 = count/V
print(f"Средняя скорость: {total_1_2} МБ/с")