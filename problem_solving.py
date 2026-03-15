"""class student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if marks<=100:
            self.__marks=marks
        else:
            print("Marks should not be greater than 100")
s=student(80)
print("Marks",s.get_marks())
s.set_marks(95)
print("updated Marks",s.get_marks())"""



"""class  calculator:
   def multiply(self,a,b,c=0):
      if c is 0:
         return a*b
      else:
         return a*b*c
cal=calculator()
print("Multiply",cal.multiply(2,3))
print("Multiple of three numbers",cal.multiply(2,3,4))"""
      
"""class Shape:
    def draw(self):
        print("drawing shape")
class circle(Shape):
    def draw(self):
        print("drawing a circle")
c=Shape()
c.draw()"""


"""from abc import ABC,abstractmethod
class employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class Manager(employee):
    def calculate_salary(self, hours, rate):
    
        return hours * rate
m=Manager()
print("Manager salary",m.calculate_salary(4,1000)) """

class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        self.__balance=amount
b=bankaccount(4000)
print("Initial balance",b.get_balance())
b.set_balance(5000)
print("updated balance",b.get_balance())





