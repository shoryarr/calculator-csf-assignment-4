def calculator():
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input")
        return

    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    elif op == '/':
        if n2 != 0:
            res = n1 / n2
        else:
            print("Division by zero error")
            return
    else:
        print("Invalid operation")
        return

    print("Result: " + str(res))

calculator()