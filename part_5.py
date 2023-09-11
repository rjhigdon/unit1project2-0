### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def new_book3():
    book_name = input("Book name:")
    book_auth  = input("Book author:")
    try:
        book_year  = input("Book year:")
    except Exception:
        print(f"Year: {book_year} IS NOT AN INTEGER, IDIOT!!!")
    try:
        book_rating  = input("Book rating:")
    except Exception:
        print(f"Rating: {book_rating} IS NOT AN INTEGER, IDIOT!!!")
    try:
        book_pgs = input("Book pages:")
    except Exception:
        print(f"# of pages: {book_pgs} IS NOT AN INTEGER, IDIOT!!!")

    with open("library.txt", "a") as l:
        l.write(f"{book_name}, {book_auth}, {book_year}, {book_rating}, {book_pgs}\n")

new_book3()

### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def read_file():
    with open ("library.txt") as l:
        file = l.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_dictionary = {
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            }


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

