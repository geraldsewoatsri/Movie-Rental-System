class MovieRental:

    def __init__(self, movie_list):
        self.movie_list = movie_list
        self.rented = []


    def display_movies(self):
        """ Displays all movies available in the movie bank. """
        for movie in self.movie_list:
            print(f"Title: {movie.title}, Genre: {movie.genre}, Released in {movie.release_year}")

        print("\n")


    def movie_by_genre(self):
        """ Prints out all movies available for the selected genre. """
        choice = input("What genre of movies would you like to view? (Sci-Fi, Crime, Action, etc: ").title()
        matching_movies = [movie.title for movie in self.movie_list if movie.genre == choice]
        if matching_movies:
            print(f"Movies in {choice} genre.")
            for title in matching_movies:
                print(title)
        else:
            print(f"No movies found in {choice} genre.")

        print("\n")

    def movie_available(self, title):
        """ Checks if a movie is available in the movie list. Returns True if it is, otherwise False. """
        for m in self.movie_list:
            if m.title == title:
                return True
        return False

    def rent_movie(self, title):
        for m in self.movie_list:
            if m.title == title:
                print(f"You have successfully rented {m.title}.")
                self.rented.append(m)
                self.movie_list.remove(m)
                return

        print(f"{title} is not available at the moment.")


    def return_movie(self, title):
        """ Checks if movie has been rented. Then it allows user to return the movie."""
        for m in self.rented:
            if m.title == title:
                print(f"You have successfully returned {m.title}")
                self.movie_list.append(m)
                self.rented.remove(m)
                return

        print(f"{title} is not recognized as a rented movie.")
