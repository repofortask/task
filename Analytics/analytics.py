import pandas as pd
import os 
import psycopg2
HOST = os.environ.get('HOST_DB')

conn = psycopg2.connect(
            host=HOST,
            database="root",
            user="root",
            password="root")
cur = conn.cursor()

# a. How many movies are in data set ?
cur.execute('SELECT COUNT(*) from movies')
db_version = cur.fetchone()
print('How many movies are in data set? ->', db_version[0])
print('\n')


# b. What is the most common genre of movie?
df_movies = pd.read_sql("SELECT * FROM movies", conn, index_col='movie_id')
list_with_genres = df_movies['genres'].values.tolist()
count_dict = {}
for element in list_with_genres:
    for i in element.split('|'):
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 0
print('What is the most common genre of movie? ->', max(count_dict, key=count_dict.get))
print('\n')

# d What are 5 most often rating users ?
df_ratings = pd.read_sql("SELECT * FROM ratings", conn)
top_5_users = df_ratings.groupby(['user_id']).count().sort_values(by='rating', ascending=False).head(5).index.values 
print('What are 5 most often rating users? ->', top_5_users)
print('\n')

# c What are top 10 movies with highest rate ?
new_df_movies = pd.read_sql("SELECT * FROM movies", conn)
list_with_ratings = df_ratings.groupby(['movie_id']).sum().loc[:, 'rating']/df_ratings.groupby(['movie_id']).count().loc[:,'user_id']
list_with_movie_id_with_ratings = list_with_ratings.sort_values(ascending=False).head(10).index.values.tolist()
print('What are top 10 movies with highest rate? ->',new_df_movies.loc[new_df_movies.movie_id.isin(list_with_movie_id_with_ratings)])
print('\n')


# e When was done first and last rate included in data set and what was the rated movie tittle?
# df_ratings['timestamp'] = df_ratings['timestamp']
df_ratings['timestamp'] = pd.to_datetime(df_ratings['timestamp'],unit='s')
movie_id_of_first_rating = df_ratings.sort_values(by='timestamp').head(1)['movie_id'].values[0]
timestamp_of_first_rating = df_ratings.sort_values(by='timestamp').head(1)['timestamp'].values[0]
movie_id_of_last_rating = df_ratings.sort_values(by='timestamp', ascending=False).head(1)['movie_id'].values[0]
timestamp_of_last_rating = df_ratings.sort_values(by='timestamp', ascending=False).head(1)['timestamp'].values[0]
print('When was done first rate included in data set and what was the rated movie tittle ->', timestamp_of_first_rating, df_movies.iloc[movie_id_of_first_rating, 0])
print('When was done last rate included in data set and what was the rated movie tittle ->', timestamp_of_last_rating, df_movies.iloc[movie_id_of_last_rating, 0])
print('\n')

# f. Find all movies released in 1990
all_movies_with_release_in_1990 = []
all_movies = df_movies['title'].values.tolist()
for movie in all_movies:
    try:
        if int(movie.split(' ')[-1].replace('(', '').replace(')', '')) == 1990:
            all_movies_with_release_in_1990.append(movie)
            print('movie released in 1990 ->', movie)
    except ValueError:
        pass
# print(all_movies_with_release_in_1990)
