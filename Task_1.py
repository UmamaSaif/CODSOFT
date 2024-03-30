# ######################## PROGRAMMED BY UMAMA SAIF #########################

# Following are functions to be used in the calculator
def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def modulus(num1, num2):
    return num1 % num2

# Following is the main functionality of the calculator


print("____________MY CALCULATOR____________")
while (1):
    try:
        num1 = int(input("Enter first number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")

    # Arithmetic operations provided in the calculator
    print("For Addition Enter \"+\"")
    print("For Subtraction Enter \"-\"")
    print("For Multiplication Enter \"*\"")
    print("For Division Enter \"/\"")
    print("For Modulus Enter \"%\"")
    
    try:
        operator = str(input("Choose an arithmetic operation"
                             " you want to perform: "))
    except ValueError:
        print("Invalid input. Please enter a character operator.")

    # Use of match for every operator 
    
    match operator:
        case "+":
            try:
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
            
            result = addition(num1, num2)
            print(f"{num1} + {num2} = {result}")
    
        case "-":
            try:
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
            result = subtraction(num1, num2)
            print(f"{num1} - {num2} = {result}")
        
        case "*":
            try:
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
            result = multiplication(num1, num2)
            print(f"{num1} * {num2} = {result}")

        case "/":
            try:
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
            while (num2 == 0):
                print("Division by 0 is not possible,"
                      " please enter another number: ")
                try:
                    num2 = int(input("Enter second number: "))
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            result = division(num1, num2)
            print(f"{num1} / {num2} = {result}")

        case "%":
            try:
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
            result = modulus(num1, num2)
            print(f"{num1} % {num2} = {result}")
    
    # Taking user choice
    print("Do you want to perform another calculation?")
    print("Enter \"Y\" for YES and \"N\" for NO")
    
    try:
        choice = str(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a string.")
    
    if (choice.lower()=="n"):
        print("Thank you for using MY CALCULATOR")
        quit()  # Quitting the program if user wants
    else:
        print()

