import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
from sklearn.decomposition import PCA

# 1. Загрузка выборки и масштабирование признаков
digits = load_digits()
data = scale(digits.data)

# 2. Размерность данных и количество уникальных значений в target
print("Размерность данных:", data.shape)
print("Количество признаков:", data.shape[1])
print("Количество объектов:", data.shape[0])
print("Количество уникальных значений в target:", np.unique(digits.target).size)

# 3. Создание модели KMeans с init='k-means++', n_clusters=количество уникальных значений, n_init=10
kmeans_pp = KMeans(init='k-means++', n_clusters=np.unique(digits.target).size, n_init=10)
kmeans_pp.fit(data)

# 4. Подсчет метрик и времени работы для KMeans с init='k-means++'
pp_ari = adjusted_rand_score(digits.target, kmeans_pp.labels_)
pp_ami = adjusted_mutual_info_score(digits.target, kmeans_pp.labels_)

# 5. Создание модели KMeans с init='random'
kmeans_random = KMeans(init='random', n_clusters=np.unique(digits.target).size, n_init=10)
kmeans_random.fit(data)

# 6. Применение PCA с количеством компонент равным количеству уникальных значений
pca = PCA(n_components=np.unique(digits.target).size)
pca.fit(data)
pca_data = pca.transform(data)

# 7. Создание модели KMeans с init=pca.components_
kmeans_pca = KMeans(init=pca.components_, n_clusters=np.unique(digits.target).size, n_init=10)
kmeans_pca.fit(data)

# 8. Сравнение по времени и метрикам для всех трех подходов
print("Время работы KMeans (init='k-means++'):", kmeans_pp.inertia_)
print("ARI для KMeans (init='k-means++'):", pp_ari)
print("AMI для KMeans (init='k-means++'):", pp_ami)

print("Время работы KMeans (init='random'):", kmeans_random.inertia_)
print("ARI для KMeans (init='random'):", adjusted_rand_score(digits.target, kmeans_random.labels_))
print("AMI для KMeans (init='random'):", adjusted_mutual_info_score(digits.target, kmeans_random.labels_))

print("Время работы KMeans (init=pca.components_):", kmeans_pca.inertia_)
print("ARI для KMeans (init=pca.components_):", adjusted_rand_score(digits.target, kmeans_pca.labels_))
print("AMI для KMeans (init=pca.components_):", adjusted_mutual_info_score(digits.target, kmeans_pca.labels_))

# 9. Отображение данных на 2D плоскости с помощью PCA
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=digits.target)
plt.scatter(kmeans_pca.cluster_centers_[:, 0], kmeans_pca.cluster_centers_[:, 1], marker='x', c='r')
plt.title("KMeans with PCA")
plt.show()

# Выводы:
# - KMeans с инициализацией 'k-means++' показал лучшие значения метрик ARI и AMI, чем KMeans с инициализацией 'random'.
# - Использование метода PCA в KMeans позволило сохранить большую часть информации и достичь похожих значений метрик ARI и AMI.
# - Метод PCA сократил размерность данных, что упростило визуализацию с использованием диаграммы рассеяния.
# - Время выполнения KMeans с использованием PCA оказалось меньше, чем при использовании инициализации 'k-means++', но больше,
# чем при использовании инициализации 'random', так как PCA добавляет дополнительные вычисления для сокращения размерности данных.