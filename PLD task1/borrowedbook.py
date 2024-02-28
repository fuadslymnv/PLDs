class Book:
    
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        
    def SetTitle(self, nTitle):
        self.__title = nTitle
        
    def GetTitle(self):
        return self.__title
    
    def SetAuthor(self, nAuthor):
        self.__author = nAuthor
        
    def GetAuthor(self):
        return self.__author
    def SetISBN(self, nIsbn):
        self.__isbn = nIsbn
        
    def GetISBN(self):
        return self.__isbn
    
    def Info(self):
        return self.__author+" "+self.__title+" "+self.__isbn
    
class BorrowedBook(Book):
    def __init__(self, title, author, isbn, borrower_name,borrow_date,return_date):
        super().__init__(title, author, isbn)
        self.borrower_name=borrower_name
        self.borrow_date=borrow_date
        self.return_date=return_date
        
    def ReturnBook(self,rDate):
        self.return_date = rDate
        
    def BorrowBook(self,bDate):
        
        self.borrow_date = bDate
        
    def Info(self):
        return super().Info()+ " "+self.borrower_name+" "+self.borrow_date+" "+self.return_date
class Library:
    def __init__(self):
        self.Books = []
    def AddBook(self, Book):
        self.Books.append(Book)
    def Save(self):
        f = open("saving.txt","w")
        lines = ""
        for book in self.Books:
            lines+=book.Info()+"\n"
        f.write(lines)
        f.close()
    def Read(self):
        f = open("saving.txt")
        print(f.read())
lib = Library()
lib.AddBook(Book("emin","emin","emin"))
lib.AddBook(Book("emin","emin","emin"))
lib.AddBook(Book("emin","emin","emin"))
lib.AddBook(BorrowedBook("emin","emin","emin","emin","eim00","das"))
lib.Save()
lib.Read()