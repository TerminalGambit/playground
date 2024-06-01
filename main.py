class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}"

class Member:
    member_count = 0

    @classmethod
    def generate_id(cls):
        cls.member_count += 1
        return cls.member_count

    def __init__(self, name):
        self.id = self.generate_id()
        self.name = name
        self.books = []

    @property
    def borrowed_books(self):
        return self.books

    def borrow_book(self, book):
        self.books.append(book)

    def return_book(self, book):
        self.books.remove(book)

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def check_out_book(self, book, member):
        if book not in [b for m in self.members for b in m.borrowed_books]:
            member.borrow_book(book)
            print(f"{book} checked out to {member.name}.")
        else:
            print("Book is currently unavailable.")

    def check_in_book(self, book, member):
        member.return_book(book)
        print(f"{book} has been returned.")

    @staticmethod
    def library_hours():
        return "Library hours are 9 AM to 8 PM."
