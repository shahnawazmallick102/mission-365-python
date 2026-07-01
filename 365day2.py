#operatos
#1 arithmetic operators
#example

# a=5
# b=6
# print(a+b)
# print(a*b)
# print(a-b)
# print(a/b)
# print(a%b)

#this are arithmetic operators

#2 relational and comparsion operators is called Boleen valus
#are(==,!=,<,>.>=,<=)
#example

# a=5
# b=10
# print(a==b)
# print(a<b)
# print(a>b)
# print(a!=b)
# print(a>=b)
# print(a<=b)

#this are relational operators

#3 assignment opeators
#(=,+=,-=,*=,/=,%=,**=)
# num=10
# num*=10
# print(num)

# num=10
# num**=10
# print(num)

#4 logical operators
#And both conduction must be true
#not reverses true to false and false to true
#or at least one conduction must be true
# are ussed to combine towo more conditon, they return True and false
#(not,and,or)
#AND
# x=10
# print(x>5 and x<20)

#NOT
# a=50
# print(a<10 and not a<60 )

#or
# x=40
# print(x>41 or x<50)

#string
# name=input("enter your name ")
# length=len(name)
# print(length)

# #occurence of $
# str=("occurence")
# print(str.count("$"))

#occurence of $

# str=("my mac cost $500,and iphone cost $900 ,copy cost $40")
# print(str.count("$"))

#conduction Statemnt

# age=int(input("enter your age"))
# if(age>=18):
#     print("yes you are eligible for vote")
    
# else:
#     print("not eligible for vote")

#even and odd number
# num=int(input("enter your number"))
# if(num%2==0):
#     print("even number")
# else:
#     print("odd number")


#largst of tow number
# num1=int(input("enter your first number"))
# num2=int(input("enter your secound number"))
# if(num1>num2):
#     print("num1 is a largest number",num1)

# elif(num1==num2):
#     print("both number are same ")
# else:
#     print("num2 is a largest number",num2)


#pass and fail 
marks=int(input("enter your marks"))
if(marks>=90):
    print("Gread A")
elif(marks>=75 and marks<89):
    print("Gread B")
elif(marks>=60 and marks<74):
    print("Gread c")
elif(marks>=50 and marks<59):
    print("Gread D")
else:
    print("student are fail")
