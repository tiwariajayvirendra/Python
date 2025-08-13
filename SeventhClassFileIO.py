# with open("parcle.txt", "r") as f:
#      data = f.read()
# new_data = data.replace("Java","Rust")
# print(new_data)

# with open("parcle.txt", "w") as f:
#      f.write(new_data)
# def check_for_word(word):
#     with open("parcle.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print(word, "it is present")
#         else:
#             print("it is not present")
 
# check_for_word("Rust")

# def check_for_line():
#     word = "Rust"
#     data = True
#     line_no = 1
#     with open("parcle.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return  
#             line_no += 1
#     return -1
# print(check_for_line())

        # for line in f:
        #     if word in line:
        #         print(f"{word} is present in line {line_no}")
        #         data = False
        #     line_no += 1
# count = 0
# with open("parcle.txt", "r") as f:
#     data=f.read()
     
#     # num= ""
    # for i in range(len(data)):
    #     if (data[i] == ","):
    #         print(num)
    #         num = ""
    #     else:
    #         num += data[i]

    num = data.split(",")
    for val in num :
        if(int(val) % 2 == 0):
            count += 1
    print(count)
        