import pandas as pd
print('========= movies ==========')
# Index(['movieId', 'title', 'genres'], dtype='object')
endereco_movies = './csv/movies.csv'
lista_movies = pd.read_csv(endereco_movies)
print(lista_movies.head())
print(lista_movies.columns)
print(lista_movies['title'][0:10])

print('========== ratings =================')
# Index(['userId', 'movieId', 'rating', 'timestamp'], dtype='object')
endereco_ratings = './csv/ratings.csv'
lista_ratings = pd.read_csv(endereco_ratings)
print(lista_ratings.head())
print(lista_ratings.columns)
print(lista_ratings['rating'][0:10])
print('unique', lista_ratings['rating'].unique())
print(lista_ratings['rating'].mean())
print(lista_ratings['rating'].min())
print(lista_ratings['rating'].max())
print(lista_ratings.describe())
