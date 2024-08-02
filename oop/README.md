 # Tasks for this directory:

 ## 0. Dive into Python Magic Methods
 __Objective:__ Master Python magic methods by implementing a `Book` class that incorporates constructors (`__init__`), destructors (`__del__`), and the representation methods (`__str__` and `__repr__`).
__Task Description__:

Create a Python script named `book_class.py`. In this script, define a `Book` class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

__Requirements for `Book` Class in `book_class.py`__:

 1. Attributes:
    - `title` (str): The title of the book.
    - `author` (str): The author of the book.
    - `year` (int): The publication year of the book.

 2. Magic Methods:
    - Constructor (`__init__`): Initializes a `Book` instance with `title`, `author`, and `year`.
    - Destructor (`__del__`): Prints "`Deleting (title of the book)`" upon object deletion.
    - String Representation (`__str__`): Returns a string in the format "`(title) by (author), published in (year)`".
    - Official Representation (`__repr__`): Returns a string that would recreate the Book instance: `f"Book('{self.title}', '{self.author}', {self.year})"`.

__Provided for Testing: `main.py`__

To test your `Book` class, use the following `main.py` script, which demonstrates creating a `Book` instance and utilizing the implemented magic methods:

```py
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()
    
```

Expected Output:

```sh
1984 by George Orwell, published in 1949
Book('1984', 'George Orwell', 1949)
Deleting 1984
```

## 1. Mastering Inheritance and Composition in Python
__Objective__: Deepen your understanding of inheritance and composition in Python by creating a system that models a library with different types of books.
__Task Description:__

Develop two Python scripts: `library_system.py` and `main.py`. In `library_system.py`, you’ll define a base class `Book` and two derived classes, `EBook` and `PrintBook`, showcasing inheritance. Additionally, implement a `Library` class demonstrating composition by managing a collection of books.
`library_system.py`:

1. Base Class - Book:
    - Attributes: `title` (str) and `author` (str).
    - Method: `__init__(self, title, author)` for initializing book attributes.

2. Derived Classes - `EBook` and `PrintBook`:
    - Both classes inherit from `Book`.
    - `EBook` additional attribute: `file_size` (int).
    - `PrintBook` additional attribute: `page_count` (int).
    - Each derived class should have its own `__init__` method that properly calls the base class `__init__` while also initializing its unique attribute.

3. Composition - `Library`:
    - Attributes: `books` (a list to store instances of `Book`, `EBook`, and `PrintBook`).
    - Methods:
        - `add_book(self, book)`: Adds a `Book`, `EBook`, or `PrintBook` instance to the library.
        - `list_books(self)`: Prints details of each book in the library.

__`main.py` (Provided for Testing)__:

This script tests the functionality of your classes in `library_system.py` by adding different types of books to a `Library` instance and listing them.

```py
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
```

__Expected Output:__

Your output should list the details of each book added to the library, reflecting the specific attributes of `EBook` and `PrintBook`, as well as the common attributes inherited from Book.

```sh
Book: Pride and Prejudice by Jane Austen
EBook: Snow Crash by Neal Stephenson, File Size: 500KB
PrintBook: The Catcher in the Rye by J.D. Salinger, Page Count: 234
```

