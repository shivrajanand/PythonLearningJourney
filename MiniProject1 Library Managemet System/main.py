from library import *
from functions import *
import os

# Customer Instances
shivraj_lbl = vishal_lbl = syed_lbl = abhishek_lbl = tanya_lbl = manya_lbl = ekta_lbl = sonali_lbl = []
shivraj = Customer("Shivraj Anand", "AILIB001", lended_books=shivraj_lbl)
vishal = Customer("Vishal Kumar", "AILIB002", lended_books=vishal_lbl)
syed = Customer("Syed Hamid", "AILIB003", lended_books=syed_lbl)
abhishek = Customer("Abhishek Kumar", "AILIB004", lended_books=abhishek_lbl)
tanya = Customer("Tanya Ragini", "AILIB005", lended_books=tanya_lbl)
manya = Customer("Manya Mridul", "AILIB006", lended_books=manya_lbl)
ekta = Customer("Ekta Mishra", "AILIB007", lended_books=ekta_lbl)
sonali = Customer("Sonali Priya", "AILIB008", lended_books=sonali_lbl)

customerlist = [shivraj, vishal, syed, abhishek, tanya, manya, ekta, sonali]

# Book instances
os_galvin = Books("Operating Systems", "Galvin", "BOOKID001")
python_thareja = Books("Understanding Python",
                       "Reema Thareja", "BOOKID002")
LetUsC = Books("Let us C", "Yashwant Kanetkar", "BOOKID003")
AnsiC = Books("ANSI C", "E Balaguruswamy", "BOOKID004")
CppBalaguruswamy = Books("C++", "E Balaguruswamy", "BOOKID005")
DigitalLogic_MorrisMano = Books(
    "Digital Logic", "Morris Mano", "BOOKID006")
DigitalLogic_Floyed = Books("Digital Logic", "L Floyed", "BOOKID007")
DSLebschevtch = Books("Data Structure Fundamentals",
                      "Lebschevtch", "BOOKID008")
AlgoCollins = Books("Algorithms", "Collins", "BOOKID009")
EnggChemistry = Books("Engineering Chemistry",
                      "Jain and Jain", "BOOKID010")
EnggMathBS = Books("Engineering Mathematics", "B.S.Grewal", "BOOKID011")
EnggMathHK = Books("Higher Engineering Mathematics",
                   "H.K.Das", "BOOKID012")

# Library Instances
Anand_Library_Book_List = [os_galvin, python_thareja, LetUsC, AnsiC, CppBalaguruswamy, DigitalLogic_MorrisMano,
                           DigitalLogic_Floyed, DSLebschevtch, AlgoCollins, EnggChemistry, EnggMathBS, EnggMathHK]
Anand_Library = Library("Anand Library", "LIBAI001",
                        Anand_Library_Book_List)


# Customer Login Function
def customerLogin():
    # customerlist = [shivraj, vishal, syed, abhishek, tanya, manya]
    print("CUSTOMER LIST ###############################################")
    data = []
    choice_list = []
    for customer in customerlist:
        data.append([customer.customer_id, customer.customer_name, customer])
        choice_list.append((customer.customer_id.lower()))
    print(tabulate([[person[0], person[1]] for person in data], headers=["Customer ID",
          "NAME",]))
    # print(choice_list, end=", ")

    choice = input("\n\nEnter Your Customer Id\n::>>> ")
    choice = choice.lower().lstrip().rstrip()

    if choice in choice_list:

        print(f"Customer Details: ")
        # choice_index = choice_list.index(choice)
        # print("choice_index = choice_list.index(choice)", choice_index)
        # new_data = data[choice_index]
        # print("data = data[choice_index]: ", new_data)

        print(tabulate([data[choice_list.index(choice)]],
                       headers=["Customer Id", "Customer Name", "Temporary Digital Address"]))

        confirmation = input(
            "\nPress [Y] to confirm or any other key to abort: ")
        if confirmation.lower().lstrip().rstrip() == 'y':
            # print(data[choice_list.index(choice)][2])
            return data[choice_list.index(choice)][2]
        else:
            print(
                f"Login Cancelled for Customer")

    else:
        print(f"No Customer matches for given id {choice.upper()}")

# main Function


def main():
    while True:
        holdScreen()
        clearScreen()
        choice1 = None
        try:
            choice1 = int(
                input("Enter your choice:\n1.Customer Login\n2.Exit\n::>>>"))
        except Exception as e:
            print("There is some error. Kindly check your input again")
            holdScreen()
            clearScreen()

        if choice1 != None:
            if choice1 == 1:
                customer_object = customerLogin()
                clearScreen()
                if customer_object != None:
                    while True:
                        print(
                            f"{customer_object.customer_name} :: {customer_object.customer_id}")
                        try:
                            choice2 = int(input(
                                "1.Lend Book\n2.Display Issued Book(s)\n3.Donate Book\n4.Return Book\n5.Logout\n::>>> "))
                            if choice2 == 1:
                                Anand_Library.lend_book(customer_object)
                                holdScreen()
                                clearScreen()

                            elif choice2 == 2:
                                # Write code to display issued books
                                clearScreen()
                                customer_object.display_lended_books()
                                # lended_book_list = customer_object.lended_books
                                # print(tabulate([item for item in lended_book_list],
                                #                headers=["Book Id", "Book Name", "Author"]))
                                holdScreen()
                                clearScreen()

                            elif choice2 == 3:
                                # write code to donate books
                                book_name = input("Enter Book Name: ")
                                book_author = input("Enter Book Author: ")
                                latest_id = Anand_Library_Book_List[len(
                                    Anand_Library_Book_List)-1].book_id
                                id_number = latest_id[6:9]
                                id_number = int(id_number)
                                new_id_number = id_number + 1
                                book_id = "BOOKID0"+str(new_id_number)
                                new_book = Books(
                                    book_name, book_author, book_id)
                                Anand_Library_Book_List.append(new_book)
                                print("\n\nThankyou for donating a book")
                                holdScreen()
                                clearScreen()

                            elif choice2 == 4:
                                # Write code to return a book
                                print("You have issued these books: \n")
                                lend_list = customer_object.lended_books
                                print(tabulate([item for item in lend_list],
                                               headers=["Book Id", "Book Name", "Author"]))
                                # print(lend_list)
                                choice_list = [book[0].lower()
                                               for book in lend_list]
                                # print(choice_list)
                                choice3 = input(
                                    "Enter the book-id you have to return: ")
                                if choice3 in choice_list:
                                    choice_index = choice_list.index(
                                        choice3.lower())
                                    # print("choice_index = ", choice_index)
                                    del customer_object.lended_books[choice_index]
                                    print(
                                        f"Successfully Returned Book\nYou have {len(customer_object.lended_books)} books issued: ")
                                    if len(customer_object.lended_books) != 0:
                                        customer_object.display_lended_books()
                                    holdScreen()
                                    clearScreen()

                            elif choice2 == 5:
                                print("Logging out")
                                holdScreen()
                                clearScreen()
                                break

                        except Exception as e:
                            print(f"\nERROR IS :\n{e}\n\n")
                            print("There is some error")
                            holdScreen()
                            clearScreen()
                else:
                    print("Customer Login Failed")
            elif choice1 == 2:
                clearScreen()
                print("LIBRARY CLOSED! PLEASE COME AGAIN SOON")

                #Clear all pyc files
                os.system(
                    f"python -Bc \"import pathlib; [p.unlink() for p in pathlib.Path('.').rglob('*.py[co]')]\"")
                #Clear all pycache folders
                os.system(
                    f"python -Bc \"import pathlib; [p.rmdir() for p in pathlib.Path('.').rglob('__pycache__')]\"")
                exit()
            else:
                print("Wrong choice")
                holdScreen()
                clearScreen()
