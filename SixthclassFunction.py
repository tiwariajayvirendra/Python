# def calc_sum(a, b): # function defination 
#     sum = a + b
#     print(sum)
#     return sum

# calc_sum(23, 53)
# #first test of function

# calc_sum(42, 52)

# calc_sum(2,5)

# def calc_sum(a, b):
#     return a + b

# sum=calc_sum(200, 400)
# print(sum)


# def calc_avg(a , b , c):
#     sum= a + b + c
#     avg= sum / 3
#     print(avg)
#     return avg
    
# calc_avg( 95, 94,93)


# Fuction

# cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix','delhi', 'mumbai', 'chennai', 'kolkata']
# heroes = ['Superman', 'Batman', 'Wonder', 'shaktiman', 'spiderman', 'ironman', 'hulk', 'thor']
# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heroes)

# print(cities[5],end='/')
# print(heroes[4],end='/')

# def print_list(list):
#     for item in list:
#         print(item, end=' ')
#     print_list(heroes)  # for a new line after printing the list

# n = 6
# fact = 1
# for i in range (1,n+1):
#      fact *= i
# print(fact)

# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)
# cal_fact(6)

# def converter(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD =", inr_val, "INR")
# converter(20000)


# Rcursion 

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(10)

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(7))  # Output: 5040
 
# Write a recursive function to calulate the sum of the first n natural numbers..

# def sum_natural(n):
#     if n == 0:
#         return 0
#     return n + sum_natural(n - 1)
# print(sum_natural(8))  # Output: 36 (0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


# Writ a recursiv function to print all elements in a list

# def print_list(list, idx =0 ):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx + 1)
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# print_list(fruits)

