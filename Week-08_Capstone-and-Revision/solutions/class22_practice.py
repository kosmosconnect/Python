# Class 22 practice - due dates (task 3). Tasks 1 and 2 are menu choices 4 and 5
# in code/class22_library.py. Task 4 (ATM version) is your own project.

from datetime import date, timedelta


class Book:
    def __init__(self, bid, title, holder="", issued_on=""):
        self.bid, self.title = bid, title
        self.holder, self.issued_on = holder, issued_on

    def issue(self, name):
        self.holder = name
        self.issued_on = str(date.today())

    def days_out(self):
        if not self.holder:
            return 0
        return (date.today() - date.fromisoformat(self.issued_on)).days


books = [Book("B1", "Wings of Fire"), Book("B2", "Godan")]
books[0].issue("Ananya")
books[1].issue("Subham")
books[1].issued_on = str(date.today() - timedelta(days=20))   # pretend: 20 days ago

for b in books:
    if b.days_out() > 14:
        print(b.title, "is overdue with", b.holder, "-", b.days_out(), "days")
