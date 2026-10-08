import  numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import math

max_mb = 2048
min_mb = 512

# станд отклонение
sigma = (max_mb - min_mb )/4

# ур доверия
z=1.96

n =  math.ceil((z*sigma/50)**2)

print(f"Cтандартное отклонение: {sigma}")
print(f"Необходимый размер выборки: {n}")
print(f"Время стестирования: {227*15/60}")