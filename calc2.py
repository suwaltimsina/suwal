choice = input("Type what you want to do (add/sub/multiply/divide): ")

while True:
    if choice in ('add', 'sub', 'multiply', 'divide'):
        number1 = float(input("Enter number: "))
        number2 = float(input("Enter number: "))

        if choice == 'add':
            print(number1 + number2)
        elif choice == 'sub':
            print(number1 - number2)
        elif choice == 'multiply':
            print(number1 * number2)
        elif choice == 'divide':
            if number2 == 0:
                print("Error! not divisibe by zero")
            else:
                print(number1 / number2)
    else:
        print("ERROR! selcet between the given option.")


