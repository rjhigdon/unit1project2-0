### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
# def add_new_book():
#     book_name = input("Book name:")
#     book_year  = input("Book year:")
#     book_auth  = input("Book author:")
#     book_rating  = input("Book rating:")
#     book_pgs = input("Book pages:")
    
#     book_dictionary = {
#         "title": book_name,
#         "Year": book_year, 
#         "Author": book_auth,
#         "Rating": book_rating, 
#         "Pages": book_pgs 
#     }
#     print(book_dictionary)
#     return(book_dictionary)
# add_new_book()

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def new_book2():
#     book_name = input("Book name:")
#     book_year  = int(input("Book year:"))
#     book_auth  = input("Book author:")
#     book_rating  = int(input("Book rating:"))
#     book_pgs = int(input("Book pages:"))
#     book_dictionary = {
#         "title": book_name,
#         "Year": book_year, 
#         "Author": book_auth,
#         "Rating": book_rating, 
#         "Pages": book_pgs 
#     }
#     print(book_dictionary)
#     return(book_dictionary)
# new_book2()

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
# def new_book3():
#     book_name = input("Book name:")
#     book_auth  = input("Book author:")
#     try:
#         book_year  = input("Book year:")
#     except Exception:
#         print(f"Year: {book_year} IS NOT AN INTEGER, IDIOT!!!")
#     try:
#         book_rating  = input("Book rating:")
#     except Exception:
#         print(f"Rating: {book_rating} IS NOT AN INTEGER, IDIOT!!!")
#     try:
#         book_pgs = input("Book pages:")
#     except Exception:
#         print(f"# of pages: {book_pgs} IS NOT AN INTEGER, IDIOT!!!")
    
#     book_dictionary = {
#         "title": book_name,
#         "Year": book_year, 
#         "Author": book_auth,
#         "Rating": book_rating, 
#         "Pages": book_pgs 
#     }
#     print(book_dictionary)
#     return(book_dictionary)

# new_book3()



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
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
def main_search():
    search_query = input("For which book would you like to get info? \n A) Hunger Games, B) Paradise Lost, C) Harry Potter (respond with letter): \n" )
    if search_query == 'a' or search_query == 'A':
        print(my_book)
        return(my_book)
    elif search_query == 'b' or search_query == 'B':
        print(your_book)
        return(your_book)
    elif search_query == 'c' or search_query == "C":
        print(their_book)
        return(their_book)
    else:
        print("Please enter a valid response")
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

# while 1 == 1:
#     main_search()