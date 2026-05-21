import json
import random


def load_movies():
    try:
        with open("movies.json", "r") as file:
            movies = json.load(file)
            return movies
    except FileNotFoundError:
        return []


def save_movies(movies):
    with open("movies.json", "w") as file:
        json.dump(movies, file)


def show_menu():
    print("\n= Movie wathclist =")
    print("1. add a movei")
    print("2. Veiw all movies")
    print("3. Show averge rating")
    print("4. pick random movie for tonite")
    print("5. Serch by genere")
    print("6. quit")


def add_movie(movies):
    title = input("Movie title: ")
    genre = input("Genre: ")
    rating = float(input("Rating 1 to 10: "))

    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(movie)
    save_movies(movies)

    print("movies saved succesfully")


def view_movies(movies):
    if movies == []:
        print("no movies yet")
    else:
        number = 1
        for movie in movies:
            print("\nMovei #", number)
            print("title:", movie["title"])
            print("genre:", movie["genre"])
            print("Ratting:", movie["rating"])
            number = number + 1


def show_average_rating(movies):
    if movies == []:
        print("no moveis yet")
        return

    total = 0
    for movie in movies:
        total = total + movie["rating"]

    average = total / len(movies)
    print("avg rating:", average)


def pick_random_movie(movies):
    if movies == []:
        print("no movies yet")
        return

    random_number = random.randint(0, len(movies) - 1)
    picked = movies[random_number]

    print("\tonight you should wach:")
    print("Title:", picked["title"])
    print("Genere:", picked["genre"])
    print("Rating:", picked["rating"])


def search_by_genre(movies):
    if movies == []:
        print("no moveis yet")
        return

    genre_search = input("What genre do you want to search for: ")
    found = False

    for movie in movies:
        if movie["genre"].lower() == genre_search.lower():
            found = True
            print("\nTitle:", movie["title"])
            print("Genere:", movie["genre"])
            print("Ratting:", movie["rating"])

    if found == False:
        print("no moveis found in that genre")


def main():
    movies = load_movies() #load movies from file

    while True:
        show_menu()
        choice = input("Pick 1 to 6: ")

        if choice == "1":
            add_movie(movies)

        elif choice == "2":
            view_movies(movies)

        elif choice == "3":
            show_average_rating(movies)

        elif choice == "4":
            pick_random_movie(movies)

        elif choice == "5":
            search_by_genre(movies)

        elif choice == "6":
            save_movies(movies)
            print("Goodby. see ya later")
            break

        else:
            print("invalid choise. please select again.")


if __name__ == "__main__":
    main()
