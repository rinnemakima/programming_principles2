def above5true(movie):
    return movie["imdb"] > 5.5

def above5(movies):
    return list(filter(above5true, movies))

def category(movies, category):
    return [movie for movie in movies if movie["category"] == category]

def avg(movies):
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)

def average_imdb_score_by_category(movies, category):
    category_movies = category(movies, category)
    return avg(category_movies)
