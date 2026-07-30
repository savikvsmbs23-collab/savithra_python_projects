from book_class import Book
from member_class import Member
library = {}
members = {}
is_on = True

def add_book():
    title = input("Enter the title of the book you want to add: ").lower()
    author = input("Enter the author of the book: ").lower()
    genre = input("Enter the genre of the book: ").lower()
    book_obj = Book(title, author, genre)
    library[title] = book_obj
    print(book_obj.get_details())

def borrow_book():
    name = input("Enter the name of the member: ").lower()
    member_id = input("Enter the member id: ").lower()
    borrowed_books = []
    num_books = int(input("Enter the number of books to borrow: "))
    for num in range(num_books):
        title = input("Enter the title of the book: ").lower()

        if title in library and library[title].available == True:
            borrowed_books.append(title)
            library[title].available = False
        else:
            print(f"The book {title} is not found.")
    member_obj = Member(name, member_id, borrowed_books)
    members[member_id] = member_obj
    print(member_obj.get_profile())


def return_book():
    name_of_return = input("Enter the name of the book to return: ").lower()
    if name_of_return in library:
        library[name_of_return].available = True
    else:
        print(f"The book {name_of_return} is not found.")
def list_books():
    for details in library.values():
        print(f"{details.title} | {details.available}")

def find_book():
    book_to_find = input("Enter the name of the book to find: ")
    if book_to_find in library:
        if library[book_to_find].available == True:
            return f"The book {book_to_find} is available"
    return f"The book {book_to_find} is not available"

while is_on:

    user_choice = input("add/borrow/return/list/find/quit: ").lower()
    if user_choice == "add":
        add_book()
    elif user_choice == "borrow":
        borrow_book()
    elif user_choice == "return":
        return_book()
    elif user_choice == "list":
        list_books()
    elif user_choice == "find":
        print(find_book())
    elif user_choice == "quit":
        is_on = False
