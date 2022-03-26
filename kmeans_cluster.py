import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
df['target'] = iris['target']

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

scaler = preprocessing.StandardScaler()
x_scaled_array = scaler.fit_transform(X)
x_scaled = pd.DataFrame(x_scaled_array, columns=X.columns)

plt.figure(figsize=(14, 7))
colourmap = np.array(['red', 'blue', 'green'])

plt.subplot(1, 3, 1) # divide into 3 pieces, in that 1st image
plt.scatter(x_scaled['petal length (cm)'], x_scaled['petal width (cm)'], s=40, c=colourmap[y])
plt.title('Real')

# KMeans
plt.subplot(1, 3, 2)
km = KMeans(n_clusters=3, random_state=0)
y_km_predict = km.fit_predict(X)
y_km_predict = np.choose(y_km_predict, [1, 0, 2]).astype(int)
plt.scatter(x_scaled['petal length (cm)'], x_scaled['petal width (cm)'], s=40, c=colourmap[y_km_predict])
plt.title('KMeans')

# Gaussian
plt.subplot(1, 3, 3)
gmm = GaussianMixture(n_components=3, max_iter=200)
y_gmm_predict = gmm.fit_predict(x_scaled)
y_gmm_predict = np.choose(y_gmm_predict, [2, 0, 1])
plt.scatter(x_scaled['petal length (cm)'], x_scaled['petal width (cm)'], s=40, c=colourmap[y_gmm_predict])
plt.title('GMM')
