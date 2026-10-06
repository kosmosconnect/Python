# Class 22 - Capstone: Library Management System
# Uses classes (Week 7), a dictionary (Week 4), CSV files (Week 6),
# exceptions (Week 7) and a menu loop (Week 4).

import csv
import os

FILE = "books.csv"


class Book:
    def __init__(self, bid, title, author, holder=""):
        self.bid = bid
        self.title = title
        self.author = author
        self.holder = holder              # "" means on the shelf

    def __str__(self):
        s = self.holder or "available"
        return f"{self.bid} {self.title} - {s}"


class Library:
    def __init__(self):
        self.books = {}                   # bid -> Book

    def add(self, book):
        self.books[book.bid] = book

    def list_all(self):
        for b in self.books.values():
            print(b)

    def search(self, word):
        word = word.lower()
        found = [b for b in self.books.values()
                 if word in b.title.lower() or word in b.author.lower()]
        return found

    def issued(self):
        return [b for b in self.books.values() if b.holder]

    def issue(self, bid, name):
        book = self.books[bid]            # KeyError if the id is wrong
        if book.holder:
            raise ValueError("Already issued to " + book.holder)
        book.holder = name

    def give_back(self, bid):
        book = self.books[bid]
        if not book.holder:
            raise ValueError("That book is already on the shelf")
        book.holder = ""

    def save(self):
        with open(FILE, "w", newline="") as f:
            w = csv.writer(f)
            for b in self.books.values():
                w.writerow([b.bid, b.title, b.author, b.holder])

    def load(self):
        if os.path.exists(FILE):
            with open(FILE) as f:
                for row in csv.reader(f):
                    self.add(Book(*row))
        else:                             # first run: a few sample books
            self.add(Book("B1", "Wings of Fire", "A. P. J. Abdul Kalam"))
            self.add(Book("B2", "Godan", "Premchand"))
            self.add(Book("B3", "Python Basics", "A. Sahoo"))


def handle(lib, c):
    if c == "1":
        lib.list_all()
    elif c == "2":
        lib.issue(input("Id: ").strip().upper(), input("Name: ").strip().title())
        print("Issued.")
    elif c == "3":
        lib.give_back(input("Id: ").strip().upper())
        print("Returned. Thank you!")
    elif c == "4":
        for b in lib.search(input("Search: ")):
            print(b)
    elif c == "5":
        for b in lib.issued():
            print(b.bid, b.title, "is with", b.holder)
    elif c == "6":
        bid = "B" + str(len(lib.books) + 1)
        lib.add(Book(bid, input("Title: ").strip(), input("Author: ").strip()))
        print("Added as", bid)
    else:
        print("Invalid choice")


def main():
    lib = Library()
    lib.load()
    while True:
        print("\n1 List  2 Issue  3 Return  4 Search  5 Issued  6 Add  0 Exit")
        c = input("Choice: ")
        if c == "0":
            print("Bye!")
            break
        try:
            handle(lib, c)
            lib.save()
        except KeyError:
            print("No book with that id")
        except ValueError as e:
            print(e)


main()
