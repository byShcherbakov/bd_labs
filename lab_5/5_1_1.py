import pandas as pd
import numpy as np

incidents = [120,30,30,20,200,100]
times = [40,65,100,150,15,30]

ALLtotal = sum(incidents)
ALLtimes = 0

for i in range(len(incidents)):
    ALLtimes += incidents[i]*times[i]

total_1_1 = ALLtimes/ALLtotal
print(f"Среднее время: {total_1_1}")
