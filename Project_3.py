import pandas as pd

def format_datetime(row):
    release_date = row['release_date'].split('/')
    release_year = row['release_year']
    res = pd.to_datetime(f"{release_date[0]}/{release_date[1]}/{release_year}", format="%m/%d/%Y")
    return res


def sort_date(data: pd.DataFrame):
    data = data.sort_values(by='release_date', ascending=False)
    data.to_csv("/home/phuc/Desktop/DEC_K14_Class/Project/Project_3/sorted_date.csv")
    return

def high_rating_movie(data: pd.DataFrame):
    high_rating = data[(data['vote_average'] > 7.5)]
    high_rating.to_csv("/home/phuc/Desktop/DEC_K14_Class/Project/Project_3/high_rating.csv")
    return

def find_highest_lowest_revenue(data: pd.DataFrame):
    data = data.loc[(data['revenue_adj'] != 0)] # remove all rows where its revenue_adj column value is 0
    print("Movie with the highest revenue: ", data.nlargest(1, columns=['revenue_adj']))
    print("Movie with the lowest revenue: ", data.nsmallest(1, columns=['revenue_adj']))
    return
    
def sum_movies_budget(data: pd.DataFrame):
    print("Total revenue: ", data['revenue_adj'].sum())
    return

def movies_with_highest_profit(data: pd.DataFrame):
    data['profit'] = data['revenue_adj'] - data['budget_adj']
    print("Top 10 movies with the highest profit: ", data.nlargest(10, columns=['profit']))
    return

# def get_top_actors(data: pd.DataFrame):
#     actors_dict = {}
#     top_actors = []
#     top_appearance = 0
#     for index, row in data.iterrows():
#         if not pd.isna(row['cast']):
#             actors = row['cast'].split('|')
#             for actor in actors:
#                 if actor in actors_dict:
#                     actors_dict[actor] += 1
#                     if actors_dict[actor] > top_appearance:
#                         top_actors.clear()
#                         top_actors.append(actor)
#                         top_appearance = actors_dict[actor]
#                     elif actors_dict[actor] == top_appearance:
#                         top_actors.append(actor) 
                                
#                 else:
#                     actors_dict[actor] = 1
#     print(f"Actors with the most appearances ({top_appearance}) are: ")
#     for actor in top_actors:
#         print(actor)
#     return

# def get_top_directors(data: pd.DataFrame):
#     directors_dict = {}
#     top_directors = []
#     top_appearance = 0
#     for index, row in data.iterrows():
#         if not pd.isna(row['director']):
#             directors = row['director'].split('|')
#             for director in directors:
#                 if director in directors_dict:
#                     directors_dict[director] += 1
#                     if directors_dict[director] > top_appearance:
#                         top_directors.clear()
#                         top_directors.append(director)
#                         top_appearance = directors_dict[director]
#                     elif directors_dict[director] == top_appearance:
#                         top_directors.append(director) 
                                
#                 else:
#                     directors_dict[director] = 1
#     print(f"Directors with the most appearances ({top_appearance}) are: ")
#     for director in top_directors:
#         print(director)
#     return

def get_top_actors_v2(data: pd.DataFrame):
    data['cast'] = data['cast'].fillna('').str.split('|')
    data = data.explode('cast', ignore_index=True)
    data = data.loc[data['cast'] != '']
    top_actors = data.groupby('cast').agg(appearance=('id','count')).reset_index()
    print(top_actors.nlargest(1, columns=['appearance']))
    return

def get_top_directors_v2(data: pd.DataFrame):
    data['director'] = data['director'].fillna('').str.split('|')
    data = data.explode('director', ignore_index=True)
    data = data.loc[data['director'] != '']
    top_directors = data.groupby('director').agg(appearance=('id','count')).reset_index()
    print(top_directors.nlargest(1, columns=['appearance']))
    return

def count_movies_by_genres(data: pd.DataFrame):
    data['genres'] = data['genres'].fillna('').str.split('|')
    data = data.explode('genres', ignore_index=True)
    data = data.loc[data['genres'] != '']
    genres = data.groupby('genres').agg(count=('id', 'count'))
    print(genres)

def main():
    data = pd.read_csv("/home/phuc/Desktop/tmdb-movies.csv")
    # Clean data for analysis
    data['release_date'] = data.apply(format_datetime, axis=1) # format date from mm/dd/yy to mm/dd/yyyy
    data.drop_duplicates(keep='first', inplace=True) # drop all duplicated rows
    # data.info()
    # sort_date(data)
    # high_rating_movie(data)
    # find_highest_lowest_revenue(data)
    # sum_movies_budget(data)
    # movies_with_highest_profit(data)

    # get_top_actors(data)
    # get_top_directors(data)

    # get_top_actors_v2(data)
    # get_top_directors_v2(data)
    # count_movies_by_genres(data)
    
if __name__ == "__main__":
    main()
