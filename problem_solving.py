"""class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand",self.brand)
        print("price",self.price)
phone1=Mobile("samsung",40000)
phone2=Mobile("1plus",20000)
phone1.display()
phone2.display()"""
"""class Laptop:
    def __init__(self,brand,ram):
        self.brand=brand
        self.ram=ram
    def show_info(self):
        print("brand",self.brand)
        print("ram",self.ram)
L1=Laptop("Dell","8GB")
L2=Laptop("HP","16GB")
L1.show_info()
L2.show_info()"""
"""class person:
    def __init__(self,name,age,emailid):
        self.name=name
        self.emailid=emailid
        self.age=age
    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("emailid",self.emailid)
p1=person("Ranga",19,"hemanth@gmail.com")
p2=person("hemanth",20,"gowda@gmail.com")   
p1.display()
p2.display()"""
"""class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("name",self.name)
        print("marks",self.marks)
        if self.marks>=40:
            print("Student has passed")
        else:
            print("student has failed")
s1=student("Ranga",35)
s2=student("nitya",45)
s1.display()
s2.display()"""

"""class circle:
    def __init__(self,area,circumference):
        self.area=area
        self.circumference=circumference
    def display(self):
        print("area",self.area)
        print("circumference",self.circumference)
area=3.14*5*5
circumference=2*3.14*5
c1=circle(area,circumference)
c1.display()"""

"""class vehicle:
    def start(self):
        print("vehicle is starting")
class car(vehicle):
    def drive(self):
        print("self driving")
c1=car()
c1.start()
c1.drive()"""

"""class animal:
    def sound(self):
        print("animal is sounding")
class cat(animal):
    def meow(sef):
        print("cat is sounding")
class dog(animal):
    def bark(self):
        print("dog is barking")
c1=cat()
d1=dog()
c1.meow()
d1.bark()"""

"""class bankaccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposited",amount)
    def withraw(self,amount):
        self.balance-=amount
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("withdraw", amount)
        else:
            print("insufficient balance",amount)
    def display(self):
        print("current balance",self.balance)
account1=bankaccount(1000)
account1.deposit(500)
account1.display()
account1.withraw(200)
account1.display()
account1.withraw(2000)
account1.display()"""


