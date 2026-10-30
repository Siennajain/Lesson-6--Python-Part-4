class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.is_borrowed= False

    def borrow(self):
        self.is_borrowed=True
        print(self.title,"by",self.author,"is borrowed")

    def return_book(self):
        self.is_borrowed=False
        print(self.title,"by",self.author,"is returned")

book1=book("Harry Potter","J.K. Rowling")

book2=book("Matilda","Roald Dahl")

book3=book("Pride and Prejudice","Jane Austen")

for kitab in (book1,book2,book3):
    kitab.borrow()
    kitab.return_book()
    print()