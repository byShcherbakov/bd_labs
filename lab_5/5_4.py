import numpy as np



normal = np.random.normal(500,50,9850)
anomalies = np.random.uniform(5000, 15000, 150)

data = np.concatenate((normal, anomalies))

print(f"Количество событий: {len(data)}")

print(f'Среднее: {np.mean(data):.2f}')
print(f'Медиана: {np.median(data):.2f}')
print(f'Стандартное отклонение: {np.std(data):.2f}')

print(f"P95: {np.percentile(data,95):.2f} мкс")
print(f"P99: {np.percentile(data,99):.2f} мкс")
print(f"P99.9: {np.percentile(data,99.9):.2f} мкс")

med = np.median(data)
mad = np.median(np.fabs(data - med))
madn = 1.4826 * mad # 1.4826 - коэффициент нормализаци

print(f"MAD: {mad:.2f}")
print(f"MADN: {madn:.2f}")

# Граница допустимого отклонения
threshold = 3 * madn

# Оставляем нормальные события
filtered_data = data[np.abs(data - med) <= threshold]

print(f"Событий до фильтрации: {len(data)}")
print(f"Событий после фильтрации: {len(filtered_data)}")
print(f"Удалено аномалий: {len(data) - len(filtered_data)}")

print("\nДо фильтрации:")
print(f"Среднее: {np.mean(data):.2f} мкс")
print(f"Медиана: {np.median(data):.2f} мкс")

print("\nПосле фильтрации:")
print(f"Среднее: {np.mean(filtered_data):.2f} мкс")
print(f"Медиана: {np.median(filtered_data):.2f} мкс")