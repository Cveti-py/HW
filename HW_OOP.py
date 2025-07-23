import math


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"Engine started for {self.make} {self.model} {self.year}")

    def stop_engine(self):
        print(f"Engine stopped for {self.make} {self.model} {self.year}")



class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)

    def remove_course(self, course_name):
        if course_name in self.courses:
            self.courses.remove(course_name)

    def list_courses(self):
        print("Courses:", ",".join(self.courses))




class Book:
    def __init__(self, title, author, isbn, year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}\nYear: {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(book)
            print("-" * 20)







class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance







class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return "Not implemented for common shape"

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


car1 = Car("Toyota", "Camry", 2022)
car1.start_engine()
car1.stop_engine()





student1 = Student("Alice", 12345)
student1.add_course("Math")
student1.add_course("History")
student1.list_courses()





book1 = Book("1984", "George Orwell", "123456789", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", "987654321", 1960)

library = Library()
library.add_book(book1)
library.add_book(book2)

print("List of books in the library:")
library.list_books()

 
library.remove_book("123456789")
print("\nList of books after removal:")
library.list_books()


book = library.find_book("987654321")
if book:
     print(f"\nFound book: {book}")
else:
     print("\nBook not found.")



account1 = BankAccount("12345", 1000.0)
account1.deposit(500.0)
account1.withdraw(200.0)
print(account1.get_balance())

account1.__balance = 0
print(account1.get_balance())


rectangle1 = Rectangle("Rectangle", 5.0, 3.0)
circle1 = Circle("Circle", 2.0)
print(rectangle1.area())
print(f"{circle1.area():.2f}")






