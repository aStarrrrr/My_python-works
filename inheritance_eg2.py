class parent:
    def set_name(self,name):
        self.name = name
class child(parent):
    def printing(self):
        print("child is executing\n")
    def print_name(self):
        print("The name of child is :"+self.name)

y = child()

y.set_name("ABHINAND")
y.printing()
y.print_name()