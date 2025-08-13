# class Student:
#     name= "Ajay Tiwari"
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)/
# ///////////////////////////////

# class Car:
#     color = "Red"
#     brand = "Tesla"
# car1 = Car()
# print(car1.color)
# car2 = Car()


# print(car2.brand)

# Paramiterized Constructor Example
# class Student:
#     def __init__(self , fullname):
#         self.name = fullname
#         print("Constructor called")
     

# s1 = Student("Ajay Tiwari")
# print(s1.name)

# s2 = Student("John Doe")
# print(s2.name)

# s3 = Student("Jane Smith")
# print(s3.name)

# class Student:
#     collage = "ABC University"
#     name = "anynymous"

#     def __init__(self, Name, Mark, Rollnum ):
#         print("Constructor called")
#         self.name = Name
#         self.mark = Mark
#         self.rollnum = Rollnum
    
#     def welcome(self):
#             print("Welcome to the class",self.name)
    
# s1 = Student("Allen Tripathi", 84, 21)
# print(s1.name)
# print(s1.collage)
# print(s1.mark)
# print(s1.rollnum)
# s1.welcome()

# class Student:
     
#     def __init__(self, Name, Mark ): 
#         self.name = Name
#         self.mark = Mark

#     def get_avg(self):
#         sum = 0
#         for value in self.mark:
#             sum += value
            
#         print("Average marks of", self.name, "is", sum /  3 )
        
# s1 = Student("Ajay Tiwari", [85, 90, 95])
# s1.name = "Allen Tiwari"
# s1.get_avg()\


# staticmethod called decorator


# @staticmethod
# def get_name():
#     print() "Ajay Tiwari"

    


# Abstraction Example\

# class Car:
#     def __init__(self):
#         self.break1 = False
#         self.clutch = False
#         self.gare = False

#     def start(self):
#         self.break1 = True
#         self.clutch = True
#         self.gare = True
#         print("Car started with color:")

# car1 = Car()
# car1.start()

# inharitance

# class Account:
#     def __init__(self, bal , Acc):
#         self.balance = bal
#         self.account_number = Acc
    
#     def debit(self, amount):
#         self.balance -= amount
#         print("Debited amount:", self.balance)

#     def credit(self, amount):
#         self.balance += amount
#         print("Credited amount:", self.balance)

#     def get_balance(self):
#         print("Current balance:", self.balance)

    
# acc1 =Account(104544, 123455)
# acc1.debit(4500)
# acc1.credit(1500)




