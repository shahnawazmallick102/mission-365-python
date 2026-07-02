                            #Revision             
#tesk 1

#even and odd number

# num=int(input("enter your number"))
# if(num%2==0):
#     print("even number")
# else:
#     print("odd number")

#vote eligblity

# num=int(input("enter your age for vote"))
# if(num>=18):
#     print("yes your a eligible for for vote")
# else:
#     print("NO you are eligible for vote")

#largest of tow number
# num1=int(input("enter your first number"))
# num2=int(input("enter your secound number"))
# if(num1>=num2):
#     print("num1 is a largerst number")
# else:
#     print("num2 is a largest number")

#pass fail
# marks=int(input("enter your marks"))
# if(marks>=80):
#     print("student passed")
# else:
#     print("student failed")


# #gread calculated
# marks=int(input("enter your marks"))
# if(marks>=90):
#     print("Gread A")
# elif(marks>=75  and marks<=89):
#     print("Gread b")
# elif(marks>=60 and marks<=74):
#     print("Gread C")
# elif(marks>=50 and marks<=59):
#     print("Gread d")
# else:
#     print("student failed")

#   task 2
#nested 
# age=int(input("enter your age"))
# if(age>=18):
#     license=input("do you have a licence")
#     if(license=="yes"):
#         print("yes you can drive")
#     else:
#         print("you can not drive")
# else:
#     print("you are under 18,")

# card=input("do you have card")
# pin=input("enter pin")
# if(card=="yes"and pin=="3690"):
#         print("cash withdraw successful")
# else:
#     print("transaction failed",)

# username=input("enter your username  ")
# password=input("enter your password ")
# if(username=="mallick"and password=="3690"):
#     print("login Sucessful")
# else:
#     print("login failed")

# amount=int(input("enter your order amount  "))
# membership=(input("Are you premium member ? (yes/no) "))
# if(amount>=500 and membership=="yes"):
#     print("free delivery")
# else:
#     print("delivery charge apply")


# age=int(input("enter your age "))
# parents=input("praents with you (yes/no)")
# if(age>=18 or parents=="yes"):
#     print("you can watch the movie")
# else:
#     print("you can not watch the movie")

banned=input("Are you banned ?(yes/no)  ")
if not(banned=="yes"):
    print("login allowed")
else:
    print("login blocked")