class Library():
    def __init__(self):
        self.available_books = []
        self.count = 0
    def books(self,addedbook):
        self.available_books.append(addedbook)
        self.count +=1
    def info(self):
        print(f"No. of books in the library are :\n{self.count}")
        print("The Books are shown below :")
        for i in self.available_books:
            print(i)

g = Library()
g.books("Mindset")
g.books("The Heat")
g.books("REAL")
g.info()
 