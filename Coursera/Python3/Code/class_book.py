class Book:
    ''' Information about a book'''

    def __init__(self, title, authors, publisher, isnb, price):
        ''' (book, str, list of str, str, str, int) -> NoneType

        Create a new book entitled title, writen by the people in authors,
        published by publisher, with ISBN isbn and costing price in dollars.

        >>> python_book = Book( \
        'Practical Programming', \
        ['Campbell', 'Gries', 'Montojo'], \
        'Pragmatic Bookshelf', \
        '978-1-93778-545-1', \
        25.0)
        >>> python_book.title
        'Practical Programming'
        >>> python_book.authors
        ['Campbell', 'Gries', 'Montojo']
        >>> python_book.publisher
        'Pragmatic Bookshelf'
        >>> python_book.ISBN
        '978-1-93778-545-1'
        >>> python_book.price
        25.0
        '''

        self.title = title
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = isnb
        self.price = price

    def __str__(self):
        ''' (Book) -> str

        Return a human readable string representation of this book
        '''

        return """Title: {0}\nAuthors: {1}\nPublisher: {2}\nISBN: {3}\nPrice: ${4}""".format(
    self.title, ', '.join(self.authors), self.publisher, self.ISBN, self.price)

    def __eq__(self, other):
        ''' (Book, Book) -> bool

        Return True iff this book and the other hava the same ISBN
        '''

        return self.ISBN == other.ISBN

    def num_authors(self):
        ''' (Book) -> int

        Return the number of authors of this book

        >>> python_book = Book( \
        'Practical Programming', \
        ['Campbell', 'Gries', 'Montojo'], \
        'Pragmatic Bookshelf', \
        '978-1-93778-545-1', \
        25.0)
        >>> python_book.num_authors()
        3
        '''

        return len(self.authors)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    

