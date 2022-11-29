class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print(f'ISBN: {self.isbn}')
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Publisher: {self.publisher}')
        print(f'Pages: {self.pages}')
        print(f'Price: {self.price}')
        print(f'Copies: {self.copies}')
        print('-'*25)

    def in_stock(self):
        return self.copies > 0

    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print('The book is out of stock')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_value):
        if 50 < new_value < 1000:
            self._price = new_value
        else:
            raise ValueError('Price should be between 50 and 1000')


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

books = [book1, book2, book3, book4]
for book in books:
    book.display()

books_by_Jack = [book.title for book in books if book.author == 'Jack']
print(books_by_Jack)