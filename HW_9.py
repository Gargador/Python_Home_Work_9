# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Фильтрация данных по количеству людей
filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# Вычисление средней стоимости дома
average_cost = filtered_data['median_house_value'].mean()

print('Средняя стоимость дома с количеством людей от 0 до 500:', average_cost)


# Задача 42: Узнать какая максимальная households в зоне минимального значения population.
# Пример кода для решения задачи:

import pandas as pd

# Загрузка данных из файла
data = pd.read_csv('sample_data/california_housing_train.csv')

# Поиск зоны с минимальным значением population
min_population_zone = data[data['population'] == data['population'].min()]

# Поиск максимального значения households в этой зоне
max_households = min_population_zone['households'].max()

print('Максимальное количество households в зоне с минимальным значением population:', max_households)
