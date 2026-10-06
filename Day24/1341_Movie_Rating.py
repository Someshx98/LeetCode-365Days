import pandas as pd

data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id':'Int64', 'title':'object'})
data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id':'Int64', 'name':'object'})
data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'], [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'], [3, 2, 4, '2020-02-25']]
movie_rating = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype({'movie_id':'Int64', 'user_id':'Int64', 'rating':'Int64', 'created_at':'datetime64[ns]'})

def movie_ratings(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    user_counts = movie_rating.groupby("user_id").size().reset_index(name = "rating_count")
    user_merge = pd.merge(user_counts, users, on = "user_id")

    user_merge.sort_values(by = ["rating_count", "name"], ascending = [False, True], inplace = True)

    top_user = user_merge.iloc[0]["name"]

    movie_rating["created_at"] = pd.to_datetime(movie_rating["created_at"])

    feb_ratings = movie_rating[
        (movie_rating["created_at"] >= "2020-02-01") &
        (movie_rating["created_at"] <= "2020-02-29")
    ]

    movie_avgs = feb_ratings.groupby('movie_id')['rating'].mean(). reset_index(name='avg_rating')
    movie_merged = pd.merge(movie_avgs, movies,on='movie_id')

    movie_merged.sort_values(by=['avg_rating', 'title'], ascending=[False, True], inplace=True)
    top_movie = movie_merged. iloc[0]["title"]

    return pd.DataFrame({
        "results" : [top_user, top_movie]
    })

print(movie_ratings(movies, users, movie_rating))