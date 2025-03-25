num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Kindly input your prefered sign(+,-,*,/)")

if operation=='+':
    print(num1 + num2)
elif operation=='-':
    print(num1 - num2)
elif operation=='*':
    print(num1 * num2)
elif operation=='/':
    print(num1 / num2)
else:
    print("kindly enter a valid operator sign(+,-,*,/) ")

