movie_list = []
while True:
    movie = input("Enter a movie name or 'quit' to exit: ") 
    if movie == "quit":
        break
    movie_list.append(movie)
print("The list of Movies are : ",movie_list)