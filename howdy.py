from imdb import Cinemagoer

# create an instance of the Cinemagoer class
ia = Cinemagoer()

# # get a movie
# movie = ia.get_movie('0133093')

# # print the names of the directors of the movie
# print('Directors:')
# for director in movie['directors']:
#     print(director['name'])

# # print the genres of the movie
# print('Genres:')
# for genre in movie['genres']:
#     print(genre)

# # search for a person name
# people = ia.search_person('Mel Gibson')
# for person in people:
#    print(person.personID, person['name'])


def seedFilm():
    print("Hello, please enter film")
    rawMovie = input()
    film = ia.search_movie(rawMovie)
    cleanMovie = film[0]
    print(cleanMovie)
    seedID = cleanMovie.movieID
    print(seedID)
    return(seedID)
    
def nextFilmGen(nextID):
    currentMovie = ia.get_movie(nextID)
    print(currentMovie)
    
    
    
prevID = seedFilm()
nextFilmGen(prevID)
    
    
