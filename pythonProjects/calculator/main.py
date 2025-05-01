while True:
    a = int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    match operation:
        case "+":
            print(f"Result: {a} + {b} = {a + b}")
        case "-":
            print(f"Result: {a} - {b} = {a - b}")
        case "*":
            print(f"Result: {a} * {b} = {a * b}")
        case "/":
            if b == 0:
                raise ValueError("Cannot divide by zero.")
            print(f"Result: {a} / {b} = {a / b}")
        case default:
            print("Invalid operation. Please use +, -, *, or /.")


