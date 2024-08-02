class SampleClass:
    year = 2024
    def __init__(self, Name, Age, Place):
        self.name = Name
        self.age = Age
        self.place = Place
    def display(self):
        print("Year :"+str(SampleClass.year))
        print("Name :"+self.name)
        print("Age :"+str(self.age))
        print("Place :"+self.place)

    def age_inc(self):
        self.age = self.age+1

x = SampleClass("Abhinand",20,'Kochi')
y = SampleClass("Karthika",20,"Muvattupuzha")

x.display()
print("\n")
y.display()
print('\n')

print('After One Year\n')

SampleClass.year+=1

x.age_inc()
y.age_inc()

x.display()
print("\n")
y.display()

#this (incrementing the year) can also be done in a way by declaring a separate function for it like: in next program "Sample_class 5"