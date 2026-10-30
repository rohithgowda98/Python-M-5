
class Book:
    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    # Method to borrow a book
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(self.title, "has been borrowed successfully!")
        else:
            print(self.title, "is already borrowed.")

    # Method to return a book
    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(self.title, "has been returned successfully!")
        else:
            print(self.title, "was not borrowed.")

    # Special method to display book details
    def __str__(self):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        return "Title: " + self.title + "\nAuthor: " + self.author + "\nStatus: " + status


# Creating book objects
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Jungle Book", "Rudyard Kipling")
book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam")

# Displaying book details
print(book1)
print()
print(book2)
print()
print(book3)

# Borrowing books
print("\n--- Borrowing Books ---")
book1.borrow()
book2.borrow()

# Trying to borrow the same book again
book1.borrow()

# Returning a book
print("\n--- Returning Books ---")
book1.return_book()

# Displaying updated details
print("\n--- Updated Book Details ---")
print(book1)
print(book2)
