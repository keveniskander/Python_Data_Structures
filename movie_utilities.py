"""
-------------------------------------------------------
movie_utilties.py
Movie class utility functions.
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-01-20"
-------------------------------------------------------
"""
from movie import Movie


def get_movie():
    """
    -------------------------------------------------------
    Creates a movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Postconditions:
        returns
        movie - a completed movie object (Movie).
    -------------------------------------------------------
    """
    title = input("Title: ")
    year = int(input("Year of release: "))
    director = input("Director: ")
    rating = float(input("Rating: "))
    genres = read_genres()
    print(genres)
    movie = Movie(title, year, director, rating, genres)
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Preconditions:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Postconditions:
        returns
        movie - contains the data from line (Movie)
    -------------------------------------------------------
    """
    data = line.strip().split("|")
    # Convert genres string to a genres list
    genres = data[4].split(",")
    n = len(genres)
    i = 0

    while i < n:
        genres[i] = int(genres[i])
        i += 1

    movie = Movie(data[0], int(data[1]), data[2], float(data[3]), genres)
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of movie objects into a list.
    Use: movies = read_movies( fv)
    -------------------------------------------------------
    Preconditions:
        fv - an already open file of movie data (file)
    Postconditions:
        returns
        movies - a list of movie objects (list of Movie)
    -------------------------------------------------------
    """
    fv.seek(0)
    movies = []
    line = fv.readline()

    while line != "":
        movie = read_movie(line.strip("|"))
        movies.append(movie)
        line = fv.readline()
    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Postconditions:
        Menu of genres is printed.
    -------------------------------------------------------
    """
    print("Genres")
    n = len(Movie.GENRES)
    i = 0

    while i < n:
        print("{:2d}: {}".format(i, Movie.GENRES[i]))
        i += 1
    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Postconditions:
        returns
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """
    genres = []
    n = len(Movie.GENRES)
    menu()
    value = input("Enter a genre number (ENTER to quit): ")

    while value != "" or genres == []:
        # Requires at least one genre.

        if value.isdigit():
            # Convert the input to an integer.
            number = int(value)

            if number >= n:
                # Verify the number is not too large.
                print("Error: input must be < {0:d}".format(n))
            elif number in genres:
                # See if the number has already been chosen.
                print("Error: genre already chosen")
            else:
                # Save the number in the genres list.
                genres.append(number)
        else:
            # Also rejects negative numbers. '-' is not a digit.
            print("Error: not a positive number.")

        value = input("Enter a genre number (ENTER to quit): ")
    # Sort the genres list for consistency
    genres.sort()
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Preconditions:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Postconditions:
        fv contains the contents of movies
    -------------------------------------------------------
    """
    n = len(movies)
    i = 0

    while i < n:
        movies[i].write(fv)
        i += 1
    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Postconditions:
        returns
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    max = len(movies)  
    i = 0
    while max != i:
        movie = movies[i]
        cyear = movie.year
        
        if cyear == year:
            ymovies.append(movie)
            
        i+=1
        
    return ymovies
        
    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Postconditions:
        returns
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    rmovies = []
    max = len(movies)  
    i = 0
    
    while max != i:
        movie = movies[i]
        crating = movie.rating
        
        if crating == rating:
            rmovies.append(movie)
            
        i+=1

# Your code here        
        
    return rmovies

# your code here        



def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Postconditions:
        returns
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    max = len(movies)  
    i = 0
    
    while max != i:
        movie = movies[i]
        cgenre = movie.genres
        
        if genre in cgenre:
            gmovies.append(movie)
            
        i+=1
        
    return gmovies
    

# your code here        



def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Postconditions:
        returns
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """
    gmovies = []
    max = len(movies)  
    i = 0
    
    while max != i:
        movie = movies[i]
        cgenre = movie.genres
        
        if cgenre == genres: 
            gmovies.append(movie)
            
        i+=1
        
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Preconditions:
        movies - a list of Movie objects (list of Movie)
    Postconditions:
        returns
        counts - the number of movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []

# your code here        

    return counts