class First:
    def display_first(self):
        print("First Class")
class Second:
    def display_second(self):
        print("Second Class")
class Third(First,Second):
    def display_third(self):
        print("Third Class")

x = Third()

x.display_first()
x.display_second()
x.display_third()