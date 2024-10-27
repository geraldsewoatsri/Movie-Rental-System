from movies import movie_bank
from rental_system import MovieRental
from movie import Movie

movies_list = []

for movie in movie_bank:
    movies_list.append(Movie(movie['title'], movie['genre'], movie['release_year']))

movies = MovieRental(movies_list)

done = False

while not done:
    print("1. Display Movies by genre")
    print("2. Rent a movie")
    print("3. Return a movie.")
    print("4. Display all Movies")
    choice = (input())

    if choice == 'off':
        print("We hope to see you soon!")
        done = True
    elif choice == '1':
        movies.movie_by_genre()
    elif choice == '2':
        movie_to_rent = input("Enter the movie you would like to rent: ")
        if movies.movie_available(movie_to_rent):
            movies.rent_movie(movie_to_rent)
    elif choice == '3':
        movie_to_return = input("Enter the title of the movie you want to return: ")
        if not movies.movie_available(movie_to_return):
            movies.return_movie(movie_to_return)
        else:
            movies.return_movie(movie_to_return)
    elif choice == '4':
        movies.display_movies()
