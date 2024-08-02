class parent:
    def __init__(self):
        print("parent")

    def set_name(self,name):
        self.name = name
        print("Parent setname")
class son(parent):
    def __init__(self):
        print("Son")

    #to avoid constructor overrriding
    # def __init__(self):
    #     super().__init__()
    #     print("Son")

    def set_name(self,name):
        self.name=name
        #to avoid method overrriding
        # super().set_name(name)
        print("Son setname")
    def print_name(self):
        print("Name :"+self.name)
# x = parent()
y = son()

y.set_name("Abhinand")
y.print_name()