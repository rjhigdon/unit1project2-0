my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def read_dict(dict):
    print(dict.items())

read_dict(my_book)
    

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

def dict_title(dict):
    print(dict["title"])

dict_title(my_book)


def dict_auth(dict):
    print(dict["author"])

dict_auth(my_book)


def dict_yr(dict):
    print(dict["year"])

dict_yr(my_book)


def dict_rate(dict):
    print(dict["rating"])

dict_rate(my_book)


def dict_pg(dict):
    print(dict["pages"])

dict_pg(my_book)

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
from operator import itemgetter
import random

my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}
your_book = {
    "title": "Paradise Lost",
    "author": "John Milton",
    "year": 1667,
    "rating": 5,
    "pages": 200
}
their_book = {
    "title": "Harry Potter",
    "author": "JK Rowling",
    "year": 1998,
    "rating": 4.14,
    "pages": 210
}
my_library=[my_book, your_book, their_book]

# Function 1: sorting by best books
def best_books(lib):
    best_books_order = sorted(lib, key=itemgetter('rating'), reverse=True)
    print(f"The books in this library from best to worst are {best_books_order}")
best_books(my_library)
#Function 2: random book in library
def random_book(lib):
    print(f"a random book from this library is{lib[random.randint(0, (len(lib)-1))]}")
random_book(my_library)
# Function 3: averaage book rating
def avg_rating(lib):
    sum = 0
    for books in lib:
        sum += books["rating"]
        print(sum)
    return(f"the average rating of the books in this library is {round(float(sum/len(lib)), 2)}")
avg_rating(my_library)