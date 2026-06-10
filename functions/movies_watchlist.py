watchlist = {}

# add a movie

def add(watchlist):
    title = input("Name the title of the movie to add: ").lower()

    for details in watchlist.values():
        if details["title"] == title:
            return "Movie already exists"

    x = len(watchlist) + 1
    watchlist[x] = {}
    watchlist[x]["title"] = title
    watchlist[x]["genre"] = input("What is the genre of the movie?: ").lower()
    watchlist[x]["watched"] = False
    watchlist[x]["rating"] = None

    return f"{watchlist[x]['title']} added to your watchlist!"

# watch a movie

def watch(watchlist):
    movie_title = input("Name the title of the movie to watch: ").lower()
    for movies, details in watchlist.items():
        if details["title"] == movie_title and details["watched"] == True:
            return f"{details['title']} is already marked as watched."
        elif details["title"] == movie_title and details["watched"] == False:
            details["watched"] = True
            return f"{details['title']} marked as watched."
    return "Movie not in watchlist"

# rate a movie

def rate(watchlist):
    title = (input("Name the title of the movie to rate: ")).lower()
    found = False
    for movie, details in watchlist.items():
        if details["title"] == title and not details["watched"]:
            found = True
            return "Watch the movie first!"
        elif details["title"] == title and details["watched"]:
            found = True
            rate_num = int(input("Enter the rating for the movie: "))
            if rate_num >0 and rate_num <= 5:
                details["rating"] = rate_num
                return f"Rating added for the movie {details['title']} is {details['rating']}."
            else:
                return "Enter the correct rating.(1 to 5)"
    if not found:
        return "Movie not found in watchlist!"
def list_movies(watchlist):
    if len(watchlist) == 0:
        return "Watchlist is empty."
    for movie, details in watchlist.items():
        print(
            f"Title: {details['title']}, "
            f"Genre: {details['genre']}, "
            f"Watched: {details['watched']}, "
            f"Rating: {details['rating']}"
        )
    return "That's it!"

def recommend(watchlist):
    genre = (input("Enter the genre to recommend: ")).lower()
    found = False
    for movie, details in watchlist.items():
        if details["watched"] and details["genre"] == genre and details["rating"] is not None and details["rating"]>=4:
                found = True
                print(details["title"])
    if not found:
        return "No recommendations found!"
    return "These are the recommendations!"

is_on=True

while is_on:
    user_input = (input("What would you like? (add/watch/rate/recommend/list_movies/quit): ")).lower()
    if user_input == "add":
        print(add(watchlist))
        #print(watchlist)
    elif user_input == "watch":
        print(watch(watchlist))
        print(watchlist)
    elif user_input == "rate":
        print(rate(watchlist))
    elif user_input == "list_movies":
        print(list_movies(watchlist))
    elif user_input == "recommend":
        print(recommend(watchlist))
    elif user_input == "quit":
        is_on = False
    else:
        print("Invalid choice")
