# Task 2
# Library Write a class structure that implements a library.Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author(author must be an instance of Author class )
# 3) Author - name, country, birthday, books =[]
# Library
# class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the
# current library. - group_by_author(author: Author) - returns a list of all books grouped by the specified author - group_by_year(year: int) - returns
# a list of all the books grouped by the specified year All 3 classes must have a readable __repr__ and __str__ methods. Also, the book
# class should have a class variable which holds the amount of all existing books
# ```
class Book:
    total_num_of_books = 0
    def __init__(self,name,year,author):
        self.author = author
        self.year = year
        self.name = name
        Book.total_num_of_books += 1


    def book_info(self):
        print(self.name,self.year,self.author)




class Author:
    def __init__(self,name,country,birthday,books):
        self.books = books
        self.birthday = birthday
        self.country = country
        self.name = name


class Library(Book):
    def __init__(self,name,books,authors):
        self.authors = authors
        self.books = books
        self.name = name
    def list_of_books(self):
        print(self.books)



CJ = Book('"Living in NY"',1925,'Carl Johnson')
CJ.book_info()
CJ.total_num_of_books
print(Book.total_num_of_books)




