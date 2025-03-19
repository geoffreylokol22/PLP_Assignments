# Assignment 1: Design Your Own Class - Book

class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def book_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}, Checked Out: {self.is_checked_out}")

class EBook(Book): #Inheritance
    def __init__(self, title, author, pages, genre, file_format, download_link):
        super().__init__(title, author, pages, genre)
        self.file_format = file_format
        self.download_link = download_link

    def download(self):
        print(f"Downloading '{self.title}' from {self.download_link} in {self.file_format} format.")
        
        
# Book example
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224, "Science Fiction")
book2 = EBook("Python Crash Course", "Eric Matthes", 544, "Programming", "PDF", "https://example.com/python_crash_course.pdf")

book1.book_info()
book1.check_out()
book1.book_info()
book1.return_book()
book1.book_info()

book2.download()
book2.book_info()