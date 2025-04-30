while True:
    try:
        a= int(input("Enter a number: "))
        b= int(input("Enter another number: "))
        print(f"Sum is {a+b}")
    except Exception as e:
        print("Invalid input. Please enter a number.",e)

