
# class Student:
#     def __init__(self, Name, Mark):
#         self.name = Name
#         self.mark = Mark


# s1 = Student("Ajay Tiwari", 85)
 
# print(s1.name)
# del s1.name
# print(s1.name)  # This will raise an AttributeError since 'name' has been deleted



# Private attributes in Python are not directly accessible outside the class.


# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_password(self, new_pass):
#         self.__acc_pass = new_pass

# acc1 = Account("123456789", "password123")


# print(acc1.acc_no)  # Output: 123456789
# print(acc1.reset_password())  # Output: password123


# class Person:
#     __name = "annonymous"

#     def __hello(self):
#         print("Hello, World!")
     
#     def welcome(self):
#          self.__hello()

# p1 = Person()

# # print(p1.welcome())  # Output: Annonymous


# inheritance
# Inheritance allows a class to inherit attributes and methods from another class.
# single level inheritance



# class Car:
#     colr = "red"
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota(Car):
#     def __init__(self, name):

#         self.name = name

# car1 = Toyota("Toyota Corolla")
# car2 = Toyota("Toyota Camry")

# print(car1.colr)

# Multi-level inheritance

# class Car:
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota(Car):
#     def __init__(self, brand):

#         self.brand = brand

# class Fortuner(Toyota):
#     def __init__(self, type):
#         self.type = type


# car1 = Fortuner("Toyota Corolla")
# # car1.start()

# Multiple Inheritance

# class A:
#     varA ="Welcome To Class A"

# class B:
#     varB = "Welcome To Class B"

# class C(A, B):
#     varC = "Welcome To Class C"

# c1 = C()

# print(c1.varA)  # Output: Welcome To Class A
# print(c1.varB)  # Output: Welcome To Class B
# print(c1.varC)  # Output: Welcome To Class C

# Super Method 
# static method decorator
# The super() function is used to call methods from a parent class.

# class Car:
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def stop():
#         print("Car stopped")

# class Toyota(Car):
#     def __init__(self, name,type):
        
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = Toyota("Toyota Corolla","electric")
 

# print(car1.type)  # Output: None, since type is not set in Toyota

# class Person:
#     name = "annonymous"

#     def changeName(self, name):
#         self.__class__.name = ("Allen Tripathi")

# p1 = Person()
# p1.changeName("Ajay Tiwari")  # This will raise an AttributeError since __changeName is private
# print(p1.name)  # Output: annonymous, since name was not changed
# print(Person.name)  # Output: annonymous, since name is a class attribute


# class Method

# class Person:
#     name = "annonymous"

#     # def changeName(obj, name):
#     #     obj.__class__.name = ("Allen Tripathi")

#     @classmethod

#     def changeName(cls, name):
#         cls.name = name


# p1 = Person()
# p1.changeName("Ajay Tiwari")  # This will raise an AttributeError since __changeName is private
# print(p1.name)  # Output: annonymous, since name was not changed
# print(Person.name)


# Property # A property in Python is a way to manage the attributes of a class using getter and setter methods.

# class Student:
#     def __init__(self,computer , science, maths):
#          self.computer = computer
#          self.science = science
#          self.maths = maths
#          self.percentage = str((self.computer + self.science + self.maths) / 3) + "%"
    
#     def calcPercentage(self):
#         self.percentage = str((self.computer + self.science + self.maths)/ 3) + "%"

# stu1 = Student(85, 90, 95)
# print(stu1.percentage)  # Output: 90.0%

# stu1.computer = 85
# print(stu1.computer)  # Output: 85
# stu1.calcPercentage()
# print(stu1.percentage)  # Output: 90.0%



# using property

# class Student:
#     def __init__(self,computer , science, maths):
#          self.computer = computer
#          self.science = science
#          self.maths = maths
          
#     @property
#     def percentage(self):
#         return str((self.computer + self.science + self.maths) / 3) + "%"
     

# stu1 = Student(97, 96, 95)
# print(stu1.percentage)  # Output: 90.0%

# stu1.computer = 85
# print(stu1.percentage,"Ajay Tiwari")  # Output: 90.0%

# print("There is 2  students first one is ajay and second one is Allen")
# stu2 = Student(43, 56, 78)
# print(stu2.percentage)  # 

# stu2.computer = 76
# print(stu2.percentage,"Allen")  #  

# Polymarphism 
# Polymorphism allows methods to do different things based on the object it is acting upon, even if they share the same name.

# Operators OverLoading
# Dunder function

# class Complex:
#     def __init__(self, real, imag):
#         self.real = real 
#         self.imag = imag

#     def showNumber(self):
#         print(self.real,"i +" ,self.imag, "j")

#     def __add__(self, num2):
#         newReal = self.real + num2.real
#         newImag = self.imag + num2.imag
#         return Complex(newReal, newImag)
    
#     def __sub__(self, num2):
#         newReal = self.real - num2.real
#         newImag = self.imag - num2.imag
#         return Complex(newReal, newImag)

# num1 = Complex(2, 3)
# num2 = Complex(4, 5)

# num1.showNumber()  # Output: 2 i + 3 i
# num2.showNumber()  # Output: 4 i + 5 i

# num3 = num1 + num2
# num3.showNumber()  # Output: 6 i + 8 i

# num4 = num1 - num2
# num4.showNumber()  # Output: -2 i + -2 i

 
# Practice Questions
# Q1

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius


#     def area(self):
#         return (22/7) * self.radius ** 2

#     def circumference(self):
#         return 2 * (22/7) * self.radius
    
# c1 = Circle(21)
# print(c1.area())
# print(c1.circumference())


# Q2 

# class Employee:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role:", self.role)
#         print("dept:", self.dept)
#         print("salary:", self.salary)
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("software engineer","IT", 150000)


# eng1 = Engineer("Ajay Tiwari", 28)   
# show_details = eng1.showDetails()  # Output: role: software engineer, dept: IT, salary: 150000


# e1 = Employee("Software Engineer", "IT", 160000) 
# e1.showDetails()  # Output: role: Software Engineer, dept: IT, salary: 60000


# Q3

class Order:
    def __init__(self, item , price):
        self.item = item
        self.price =price
    def __gt__(self, odr2):
        return self.price > odr2.price
odr1 = Order("Pizza", 500)
odr2 = Order("Burger", 300)
print(odr1 > odr2)  # Output: True, since 500 > 300
        