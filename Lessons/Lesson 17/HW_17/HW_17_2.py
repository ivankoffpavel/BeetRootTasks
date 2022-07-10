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

class Library(Book):
    def __init__(self,lib_name,name,year,author):
        super().__init__(name,year,author)
        self.authors = []
        self.books = []
        self.lib_name = lib_name
    def new_book(self):
        b_inst = Book(self.name,self.year,self.author)
        self.books.append(b_inst)
    def group_by_author(self,author):
        for item in self.books:
            if item.author.name == self.author.name:
                print(item.author.books)
            else:
                print('This author name doesn\'t exist!')
        


    def __str__(self):
        return f'Bookname: {self.name}, year: {self.year},author: {self.author}'




class Author:
    def __init__(self,name,country,birthday,books):
        self.books = books
        self.birthday = birthday
        self.country = country
        self.name = name
    def __str__(self):
        return f'{self.name},{self.country},{self.birthday}'







auth1 = Author("Teodor Driser",'USA',1863,["Titan","Finansist"])
auth2 = Author("Fransi")

lib1 = Library('Main','Titan',1863,auth1)
lib1.new_book()

print(lib1)
lib1.group_by_author('Teodor Driser')















