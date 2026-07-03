# light=input("enter the light colour")
# if(light=="red"):
#     print("stop")
# elif(light=="yellow"):
#     print("look")
# elif(light=="green"):
#     print("GO")
# else:
#     print("print light is broken")

# bill=int(input("enter your bill amount "))
# if(bill>=1000):
#     print("20% discount")
# elif(bill>=500):
#     print("10% discount")
# elif(bill>=200):
#     print("5% discount")
# else:
#     print("No discount")

# account_active=(input("your account is avtive (yes/no)"))
# otp=int(input("enter your otp"))
# if(account_active=="yes" and otp==3690):
#     print("access Granted")
# elif(account_active=="yes" and otp!=3690):
#     print("incorrect otp")
# elif(account_active=="no"):
#     print("account is not active")
# else:
#     print("invailed entery")

Balance='10000'
pin=int(input("enter your pin"))
Wihdraw_amount=int(input("enter your amount"))
if(Balance==10000 and pin==3690):
    print("transaction successful")
elif(Balance==10000 and pin!=3690):
    print("Invalid pin")
elif(Balance!=10000 and pin==3690):
    print("Insufficient balance")
else:
    print("Invalid Amount")