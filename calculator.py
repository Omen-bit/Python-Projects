print("Welcome to the Calculator Program")

game_over=True

def calculation(num1,num2,operator):
    if operator=="+":
        return num1+num2
    elif operator=="-":
        return num1-num2
    elif operator=="*":
        return num1*num2
    elif operator=="%":
        return num1%num2
    elif operator=="//":
        if num2==0:
            return "invalid numerator",0
        else:
            return num1//num2

def calculate(num1):
    num2 = int(input("Whats the second number? :"))
    operator = input("Choose a operator from: \n + \n - \n * \n // \n % \n >>>")

    result=calculation(num1,num2,operator)
    return result



while game_over:
    num1=int(input("Whats the first number? :"))
    num2=int(input("Whats the second number? :"))

    operator=input("Choose a operator from: \n + \n - \n * \n // \n % \n >>>")

    result=calculation(num1,num2,operator)
    print(result)

    stop=True

    while stop:
        opinion=input(f"Type y to continue calculating with {result},or Type n to start new calculation: ").lower()
        if opinion=="y":
            result=calculate(result)
            print(result)
        else:
            stop=False



