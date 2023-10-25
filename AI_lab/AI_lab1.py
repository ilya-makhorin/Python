import pandas
data = pandas.read_csv(filepath_or_buffer='/Users/oksanamakhorina/Downloads/Титаник.csv')

# 1. Сколько мужчин было на корабле?
male_count = data[data['Sex'] == 'male'].shape[0]
print('1. Количество мужчин на корабле:',male_count)

# 2. Какая доля пассажиров (в %) выжила?
survivors = data[data['Survived'] == 1].shape[0]
percentage = survivors / len(data) * 100
print('2. Доля выживших пассажиров:',round(percentage,1))

# 3. Какая доля пассажиров (в %) от общего количества путешествовала во 2-ом классе?
Pclass2 = data[data['Pclass'] == 2].shape[0]
percentage_class = Pclass2 / len(data) * 100
print('3. Доля пассажиров путешествовавшая во 2 классе:',round(percentage_class,1))

# 4. Посчитайте среднее и медиану возраста всех людей на корабле.
age_column = data['Age']
mean_age = age_column.mean()
median_age = age_column.median()
print("4. Средний возраст:",round(mean_age, 1),"Медиана возраста:", median_age)


# 5. Коррелируют ли число братьев/сестер с числом родителей/детей? Посчитайте корреляцию по Пирсону между признаками SibSp и Parch датасета.
corr = data['SibSp'].corr(data['Parch'], method='pearson')
print("5. Корреляция между SibSp и Parch:", round(corr,1))

#6. Какое самое популярное женское имя было на корабле? Извлеките из полного имени пассажира (колонка Name) его личное имя (FirstName).
# Cоздаем копии всех уникальных имен без дубликатов
unique_names =data[data['Sex'] == 'female']['Name'].str.split(',').str[1].str.split('.').str[1]

# Определение самого часто встречающегося имени
most_common_name = max(set(unique_names), key=unique_names.tolist().count)

# Определение количества вхождений самого популярного имени
count_most_common_name = unique_names.tolist().count(most_common_name)

print("6. Самое популярное женское имя: ", most_common_name,"Количество найденных имен: ", count_most_common_name)




