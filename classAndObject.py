class developer:
    def __init__(self,name,age):  #constructor method — it runs when you create a new object.
        self.name=name   #attribute
        self.age=age     #attribute

    def developerDetails(self):   #method
        print(f"My name is{self.name},I am {self.age} years old")

developer1=developer("Tabitha",19) # object created from the developer class.
developer1.developerDetails() #calling the developerDetails() method using developer1.developerDetails()


class rectangle:
    area=0  #is a class variable, meaning it's shared by all instances of the class.
    def __init__(self,length,widith):
        self.length=length
        self.widith=widith
        rectangle.area=length*widith

    def dimensions(self):
        print(f"The length is:{self.length} ,widith is{self.widith}")

    def rectangleArea(self):
        print(rectangle.area)

area1=rectangle(20,20)
area1.dimensions()

area1.rectangleArea()

class cube:
     
    def __init__(self,length,widith,height=40,*list):
        self.length=length
        self.widith=widith
        self.height=height
        self.list=list
        self.volume=length*widith*height

    def dimensions(self):
        print(f"The length is: {self.length} ,widith is {self.widith} and height is: {self.height}" )

    def rectangleArea(self):
        print(self.volume)

    def mylist(self):
        print(self.list[1:3])

volume1=cube(20,15,40,50,60,70,80,90)
volume1.dimensions()

volume1.rectangleArea()
volume1.mylist()

#area and circumference of a circle
import math
class circle:
    def __init__(self,radius):
        self.radius=radius
        self.area=math.pi*radius**2
        self.circumference=2*math.pi*radius

    def dimension(self):
        print(f"the radius is: {self.radius}")

    def circleArea(self):
        print(f"area is: {self.area:.2f}")

    def circlecircumference(self):
        print(f"circumference is: {self.circumference:.2f}")

circle1=circle(7)
circle1.dimension()
circle1.circleArea()
circle1.circlecircumference()

class Employee:
   name = "Bhavesh Aggarwal"
   age = "30"

# instance of the class
emp = Employee()
# accessing class attributes
print("Name of the Employee:", emp.name)
print("Age of the Employee:", emp.age)


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

emp = Employee("Bhavesh Aggarwal", 30)
print(emp.name)
print(emp.age)
