# به نام خدا 
list_of_books = []
class Book:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def chap(self):
        print(self.name, self.subject)

while True:
    x = input("1.add   2.remove  3.edit  4.list :>> ")

    if x == "1":
        name = input("enter the name of Book: ")
        subject = input("enter the subject of book : ")
        book = Book(name, subject)
        list_of_books.append(book)

    elif x == "2":
        n_f_r = input("enter the name of books for del : ")
        found = False
        for book in list_of_books:
            if book.name == n_f_r:
                list_of_books.remove(book)
                found = True
                print("کتاب حذف شد")
                break
        if not found:
            print("این کتاب وجود خارجی ندارد")

    elif x == "3":
        sb = input("enter the name book before edit :")
        found = False
        for book in list_of_books:
            if book.name == sb:
                xs = input("enter the old subject of book: ")
                if book.subject == xs:
                    vs = input("enter the new subjectof book : ")
                    xx = input("enter the new name of book: ")
                    book.subject = vs
                    book.name = xx
                    print("book edited")
                    found = True
                else:
                    print(" you entered wrong subject")
                    found = True
                break
        if not found:
            print("book was not find")

    elif x == "4":
        for k in list_of_books:
            k.chap()

    else:
        print("wrong value")
        break