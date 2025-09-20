# calculator 2

calculations = []

calculating = True

def calculator(num1,num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "You can't divide by zero"
        return num1 / num2
    elif op == "^":
        return num1 ** num2
    else:
        return "Invalid input"


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operation: ")

while calculating:
    result = calculator(num1, num2, op)
    calculations.append(result)
    print(result)
    if calculating:
        playagain = input("Would you like to play again?")
        if playagain == "yes":
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            op = input("Enter the operation: ")
        elif playagain == "no":
            print("Thank you for playing")
            calculating = False
        else:
            print("Invalid input")

print("Your numbers were: ")
for results in calculations:
    print(results)




