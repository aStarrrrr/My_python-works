class SampleClass:
    year = 2024
    def __init__(self,Name,Age,Place):
        self.name = Name
        self.age = Age
        self.place = Place

    def display(self):
        print("At the year of "+str(SampleClass.year))
        print("Name :"+self.name)
        print("Age :"+str(self.age))
        print("Place :"+self.place)

    def age_inc(self):
        self.age+=1

    def relocate(self,place):
        self.place=place

    def displaym(self):
        print("Name :"+self.name)
        print("Place :"+self.place)

    @classmethod
    def year_inc(cls):
        cls.year+=1

    @staticmethod
    def display_static():
        print("----    ----    ----    ----    ")

x = SampleClass("Abhinand",20,"Kochi")
y = SampleClass("Karthika",20,"Muvattupuzha")

x.display()
print("\n")
y.display()

print("\nAfter Years --\n")
SampleClass.display_static()

for i in range(5):
    x.age_inc()
    y.age_inc()
    SampleClass.year_inc()

    print("NEXT YEAR")
    x.display()
    print("\n")
    y.display()
    print("\n")

print("\nAfter Marriage :\n")
x.relocate("CANADA")
y.relocate("CANADA")

x.displaym()
print("\n")
y.displaym()