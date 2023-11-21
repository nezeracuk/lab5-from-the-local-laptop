from enum import Enum


class TypeMovie(Enum):
    ACTION = 1
    COMEDY = 2
    DRAMA = 3
    FANTASY = 4
    HORROR = 5


class Movie:
    def __init__(self, id, title, ranking, release_date, character, number, ticket_price, comment, movie_type):
        self.id = id
        self.title = title
        self.ranking = ranking
        self.release_date = release_date
        self.character = character
        self.number = number
        self.ticket_price = ticket_price
        self.comment = comment
        self.movie_type = movie_type

    def __str__(self):
        return (f"Movie: ID: {self.id}, "
                f"Title: {self.title}, "
                f"Ranking: {self.ranking}, "
                f"Release date: {self.release_date}, "
                f"Character: {self.character}, "
                f"Number: {self.number}, "
                f"Ticket price: {self.ticket_price}, "
                f"Comment: {self.comment}")


class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.movies = []

    def __str__(self):
        return (f"Cinema: Name of cinema: {self.name}, "
                f"Location: {self.location}")

    def add_movie(self, movie):
        self.movie = movie
        self.movies.append(movie)

    def calculate_profit(self, day):
        profits = {}
        for movie in self.movies:
            if day == movie.release_date:
                profit = movie.ticket_price * movie.number
                profits[movie.title] = profit
                return profits

    def choose_movie(self, genre, character):
        eligible_movies = []
        for movie in self.movies:
            if movie.movie_type == genre and movie.character >= character:
                eligible_movies.append(movie)

        return eligible_movies

    def sort_movies_by_release_date(self):
        self.movies.sort(key=lambda movie: movie.release_date)


movie1 = Movie(1, "Black Adam", "9.2", "12.04.2014", 4, 2, 10,
               "Black Adam is an American superhero film based on the comic book of the same name by DC Comics.", TypeMovie.FANTASY)
movie2 = Movie(2, "Sinister", "8.3", "21.11.2012", 5, 4, 9,
               "is a horror film directed by Scott Derrickson and starring Ethan Hawke, Vincent D'Onofrio and James Ransone. The world premiere took place at the South by Southwest Film Festival on March 11, 2012.", TypeMovie.HORROR)
movie3 = Movie(3, "John Wick: Chapter 4", "6.4", "27.10.2003", 1, 6, 7, "Action film with Keanu Reeves", TypeMovie.ACTION)
if __name__ == "__main__":
    cinema1 = Cinema("Planet of cinema", "Bandery 28A")
    cinema1.add_movie(movie1)
    cinema1.add_movie(movie2)
    cinema1.add_movie(movie3)
    print(cinema1)
    print()
    print(movie1)
    print()
    print(movie2)
    print()
    print(movie3)
    print()

    chosen_day = "12.04.2014"
    print(f"Movies and their profits on {chosen_day}:")
    profits = cinema1.calculate_profit(chosen_day)
    for movie_title, profit in profits.items():
        print(f"{movie_title}: Profit ${profit}")

    chosen_day = "27.10.2003"
    profits = cinema1.calculate_profit(chosen_day)
    for movie_title, profit in profits.items():
        print(f"{movie_title}: Profit ${profit}")

    chosen_day = "21.11.2012"
    profits = cinema1.calculate_profit(chosen_day)
    for movie_title, profit in profits.items():
        print(f"{movie_title}: Profit ${profit}")
    print()

    def Eligible_movies1():
        chosen_movies = cinema1.choose_movie(TypeMovie.ACTION, 1)
        print("Eligible Movies:")
        for movie in chosen_movies:
            print(f"{movie.title} ({movie.release_date})")
    Eligible_movies1()
    def Eligible_movie2():
        chosen_movies = cinema1.choose_movie(TypeMovie.HORROR, 5)
        for movie in chosen_movies:
            print(f"{movie.title} ({movie.release_date})")
    Eligible_movie2()
    def Eligible_movie3():
        chosen_movies = cinema1.choose_movie(TypeMovie.FANTASY, 3)
        for movie in chosen_movies:
            print(f"{movie.title} ({movie.release_date})")
    Eligible_movie3()
    print()
    cinema1.sort_movies_by_release_date()
    print("Sorted Movies by Release Date:")
    for movie in cinema1.movies:
        print(f"{movie.title} ({movie.release_date})")
