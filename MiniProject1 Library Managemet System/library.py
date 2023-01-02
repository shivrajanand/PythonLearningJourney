from tabulate import tabulate
# from functions import *


class Library():
    def __init__(self, name_of_library, library_id, booklist):
        self.name_of_library = name_of_library
        self.library_id = library_id
        self.total_books = len(booklist)
        self.booklist = booklist

    def display_books(self):
        print(f"Total number of books = {self.total_books}")
        print(self.booklist)

    def lend_book(self, customer):
        print("Books Available ###############################################")
        data = []
        choice_list = []
        for book in self.booklist:
            data.append([book.book_id, book.book_name, book.book_author])
            choice_list.append((book.book_id.lower()))
        print(tabulate(data, headers=["Name", "Author", "BookID"]))

        choice = input("\n\nEnter Book Id of your choice: ")
        choice = choice.lower().lstrip().rstrip()

        if choice in choice_list:

            print(f"You have choosen book: ")
            # choice_index = choice_list.index(choice)
            # print(choice_index)
            # data = data[choice_index]
            # print(data)
            print(tabulate([data[choice_list.index(choice)]],
                  headers=["BookID", "Book Name", "Author"]))

            confirmation = input(
                "\nPress [Y] to confirm or any other key to abort: ")
            if confirmation.lower().lstrip().rstrip() == 'y':
                customer.lended_books.append(data[choice_list.index(choice)])
                print(
                    f"\nISSUED BOOKS FOR {customer.customer_name} :: {customer.lended_books[len(customer.lended_books)-1]}")
                # holdScreen()
                # clearScreen()
            else:
                print(
                    f"Books Issue Cancelled for Customer {customer.customer_name}, ID: {customer.customer_id}")

        else:
            print(f"No Book matches for given id {choice.upper()}")


class Books:
    def __init__(self, book_name, book_author, book_id):
        self.book_name = book_name
        self.book_author = book_author
        self.book_id = book_id


class Customer:

    def __init__(self, customer_name, customer_id, lended_books):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.lended_books = lended_books

    def display_lended_books(self):
        lended_book_list = self.lended_books
        print(tabulate([item for item in lended_book_list],
                       headers=["Book Id", "Book Name", "Author"]))


if __name__ == '__main__':
    new_list = []
    new = Customer("customer_name", "customer_id", lended_books=new_list)
    print(type(new.lended_books))
