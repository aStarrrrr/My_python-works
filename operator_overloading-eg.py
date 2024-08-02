class First:
    def se_name(self,name):
        self.name = name
    def __add__(self, other):
        name=self.name+" "+other.name
        return name

first_name = First()
second_name = First()

first_name.se_name("Abhinand")
second_name.se_name("Shaji")

full_name = first_name+second_name
print(full_name)