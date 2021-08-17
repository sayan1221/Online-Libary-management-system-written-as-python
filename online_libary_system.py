class Libary:
    def __init__(self,libary_name,list_of_books):
        self.libary_name = libary_name
        self.list_of_books = list_of_books
        self.donate_book = {}
        self.withdraw_book = {}

    def book_display(self):
        print(f"All books are : \n {self.list_of_books}")

    def withdraw(self):
        name = input("Enter your name : ")
        book = input("Enter book name : ")
        if book in self.list_of_books:
            self.withdraw_book [name] = book
            self.list_of_books.remove(book)
            print("Withdraw of successfully Done")
        else:
            print("This book is not available")

    def donates_book(self):
        name = input("Enter your name : ")
        book = input("Enter book name : ")
        self.list_of_books.append(book)
        self.donate_book [name] = book
        print("Successfully Added")

    def return_book(self):
        book = input("Enter book name : ")
        self.list_of_books.append(book)
        print("Successfully return")

    def delete_book(self):
        book = input("Enter book name : ")
        self.list_of_books.remove(book)
        print("Successfully remove")

    def donate(self):
        for i, j in self.donate_book.items():
            print(f"'{i}' donatated : '{j}' book")


    def withdraw_std(self):
        for i, j in self.withdraw_book.items():
            print(f"'{i}' withdraw : '{j}' book")

def main():
    list_of_books = ["a","b","c"]
    libary_name = input("Enter your libary name :")

    lib_system = Libary(libary_name,list_of_books)

    print("Check all book : Press - 'c_book'")
    print("Withdraw a book : Press - 'withdraw'")
    print("Donate book : Press - 'donate'")
    print("Return book : Press - 'return'")
    print("Delete book : Press - 'delete'")
    print("Check Donater : Press - 'donater'")
    print("Check withdraw book list : press - 'w_book'")
    print("Exit : Press - 'exit'")
    loop = True
    while loop == True:
        n = input("Enter any item :")

        if n == "c_book":
            lib_system.book_display()

        elif n == "withdraw":
            lib_system.withdraw()

        elif n == "donate":
            lib_system.donates_book()

        elif n == "return":
            lib_system.return_book()

        elif n == "delete":
            lib_system.delete_book()

        elif n == "donater":
            lib_system.donate()

        elif n == "w_book":
            lib_system.withdraw_std()

        elif n == "exit" :
            loop = False
            print("Thanks for using ")

        else :
            print("Invalid input")


if __name__ == "__main__":
    main()
