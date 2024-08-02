class father:
    def job(self):
        print("Carpenter")
class son(father):
    def study(self):
        print("Engineering")

#creating object
x = father()
y = son()

x.job()

#but in son..We can call
y.job()
y.study()