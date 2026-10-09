import pandas as pd
import numpy as np
import math


# Пункт 1
df = pd.read_csv('movies_ratings.csv',  sep=',', decimal='.', on_bad_lines='skip')
print(f"Успешно прочитано. Длина: {len(df)}")
C = df['mean_rating'].mean()
print(f'Средний рейтинг :{C:.4f}')

# Пункт 2
m = 50


df["WR"] = (
    (df["count"] / (df["count"] + m)) * df["mean_rating"]
    + (m / (df["count"] + m)) * C
)
print(df['WR'])

# Пункт 3
df = df.sort_values("WR",ascending=False).reset_index(drop=True)
print("\nТоп 5 фильмов ")
print(df[["title","count","mean_rating","WR"]].head(5))

print("\nТоп худших 5 фильмов  ")
print(df[["title","count","mean_rating","WR"]].tail(5))

# Пункт 4
movie_idx = {mid: idx for idx, mid in enumerate(df["movieId"])}
while True:
    s = input("\nВведите ID фильма или exit: ")
    if s == "exit":
        break
    if not s.isdigit():
        print("Введите ID фильма")
        continue

    movie_id = int(s)

    if movie_id not in movie_idx:
        print("Фильм с таким ID не найден!")
        continue

    try:
        rating = float(input("Введите оценку (0.5–5.0): "))
    except ValueError:
        print("Введите число!")
        continue
    if not 0.5 <= rating <= 5.0:
        print("Оценка должна быть от 0.5 до 5.0!")
        continue

    idx = movie_idx[movie_id]
    old_count = df.at[idx, "count"]
    old_mean = df.at[idx, "mean_rating"]
    old_wr = df.at[idx, "WR"]
    df.at[idx, "count"] += 1
    df.at[idx, "sum_ratings"] += rating
    count = df.at[idx, "count"]
    mean = df.at[idx, "sum_ratings"] / count
    df.at[idx, "mean_rating"] = mean
    df.at[idx, "WR"] = (
        count / (count + m) * mean
        + m / (count + m) * C
    )

    # 9. Вывод результатов
    print("\nФильм:", df.at[idx, "title"])
    print(f"Количество оценок: {old_count} -> {count}")
    print(f"Средний рейтинг: {old_mean:.4f} -> {mean:.4f}")
    print(f"Байесовский рейтинг: {old_wr:.4f} -> {df.at[idx, 'WR']:.4f}")