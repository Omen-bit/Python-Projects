"""Fix Errors"""
try:
    num=int(input("Enter a number : "))
except ValueError:
    print("you have typed an invalid value,please try again with a numerical number")
    num = int(input("Enter a number : "))

if num>18:
    print("You are eligible to ride a bike")