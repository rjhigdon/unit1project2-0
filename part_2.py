### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ["John Milton", "JK Rownling", "Earnest Hemingway", "George Orwell", "Aldous Huxley", "CS Lewis", "JRR Tolkein"]

# Now let's add a new author to the end with the .append() method. Type your code below. Code here

my_authors.append("Suzanne Collins")

# Now let's remove an element in the list. Code here

my_authors.remove("Suzanne Collins")

# Now access an element by it's index. (Remember it indexes start at 0. Code here

my_authors[2]

# Now slice the list.Code here

my_authors[1:2]

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.Code Here

my_author_tuple = ("John Milton", "JK Rownling", "Earnest Hemingway", "George Orwell", "Aldous Huxley", "CS Lewis", "JRR Tolkein")

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
my_author_set = {"John Milton", "JK Rownling", "Earnest Hemingway", "George Orwell", "Aldous Huxley", "CS Lewis", "JRR Tolkein"}

# Add a new author to your set.

# Code here

my_author_set.add("Suzanne Collins")

# Try adding the same author again, and be sure to print your set.

my_author_set.add("Suzanne Collins")

### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.
# Code here

for book in my_authors:
    print(book)

for book in my_author_tuple:
    print(book)

for book in my_author_set:
    print(book)

