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
