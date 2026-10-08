import pandas as pd
import numpy as np


changes = [2.0,0.5,8.0]
file = 1


ll = len(changes)
for i in range(ll):
    file *= changes[i]

total_5_3 = file**(1/ll)
print(f" средний коэффициент сжатия: {total_5_3}")