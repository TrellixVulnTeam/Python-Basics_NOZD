class Base1:
    def get(self):
        global a,b
        print("Enter the Two Numbers in Class Base1 :  ")
        a=int(input())
        b=int(input())
class Base2:
    def get(self):
        global c,d
        print("Enter the Two Numbers in Class Base2 :  ")
        c=int(input())
        d=int(input())
class Derived(Base2,Base1):
    def display(self):
        sum=a+b+c+d
        print("Sum = ",sum)
obj=Derived()
obj.get()
obj.display()