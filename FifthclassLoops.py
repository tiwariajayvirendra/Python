 
# count = 5

# while count >= 1 :
#     print("hii ajay",count)
#     count -= 1

#  Q1
# # i = 1

# # while i <= 100 :
# #     print(i)
# #     i += 1
    
#  Q2
# # i = 100

# # while i >= 1:
# #     print(i)
# #     i -= 1

# #  Q3
# n = int(input("enter the number which you want the table"))
# i=1
# while i <= 10:
#     print(n*i)
#     i += 1
 

# # Q4
# num=[1,4,9,16,25,36,49,64,81,100]

# i = 0

# while i <len(num):
#     print(num[i])
#     i += 1


# Q5

# num=(1,4,9,16,25,36,49,36,81,100)

# x =36

# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found it" ,i)
#     else:
#         print("Finding")

#     i += 1
 

# Loop - break and Continue

# num=(1,4,9,16,25,36,49,36,81,100)

# x =36

# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found it" ,i)
#         break
#     else:
#         print("Finding")

#     i += 1

# print("end of the line")

# Q1

# nums = [1,2,5,7,8,49,56,75,34,33,49]
# x = 49
# idx = 0
# for val in nums:
#     if(val == x ):
#         print("Print the value of idx",idx)
#     idx += 1
 
# New Topic RANGE 

# seq = range(7)
# for i in seq:
#     print(i)

# Start , stop , step

# for i in range(20): #Stop Condintion is performing
#     print(i)

# for i in range(1 , 19): #it is start and stop condition 
#     print(i)

# for i in range (2, 20,2): # here i am performing Start And Stop ANd then Setp condition performing
#     print(i)

# Print even number using range method

# for i in range (2 , 100 , 2):
#     print(i)


# Print odd Number using Range Method

# for i in range (1, 100, 2):
#     print(i)
     

# n = 10
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum of",sum)

# using while loop
 
# n = 6
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1

# print("Total sum", sum)


# n = 6
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# print("Total sum", sum)


# n = 5
# fact = 1
# i = 1
# for i in range(1, n):
#     sum *= i
# print("total sum of",sum)


# factorial of this number is this
n = 5
fact = 1
 
# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial is", fact)

# for i in range(1, n+1):
#     fact *= i

# print("factorial is ", fact)