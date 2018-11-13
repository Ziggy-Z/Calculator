num1 = float(input("Enter 1st number: "))
op = input("Enter Operator: ")
num2 = float(input("Enter 2nd number: "))

while True:
    if op == '+':
        print(num1 + num2)
        break
    elif op == '-':
        print(num1 - num2)
        break
    elif op == '*':
        print(num1 * num2)
        break
    elif op == '/':
        print(num1 / num2)
        break
    else:
        print('Invalid')
        num1 = float(input("Enter 1st number: "))
        op = input("Enter Operator: ")
        num2 = float(input("Enter 2nd number: "))





