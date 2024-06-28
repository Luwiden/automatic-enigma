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
    seedID = cleanMovie.movieID
    return(seedID)
    
def nextactorGen(nextID):
    currentMovie = ia.get_movie(nextID)
    topActor = currentMovie['actors'][0]
    topActor = str(topActor)
    cleanActor = ia.search_person(topActor)
    actorID = cleanActor[0].personID
    return(actorID)

def nextFilmGen(prevActorID):
    
    
    

    
    
    
    
    
    
    
    
    
#the program will get the top actor of an inputted film. it will then get
#that actors top film. each film is added to a list - if that film is 
#already on the list, the next actor will be picked in order to prevent a 
# loop.     
trackingList = []
prevID = seedFilm()
for x in range(5):
    trackingList = trackingList + [prevID]
    topactorID = nextactorGen(prevID)
    nextFilmID = nextFilmGen(topactorID)

    
    
