def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b if b != 0 else "Error : Division is not possible by 0!"

def calculator():
    print("\n--*-- Calculator --*--")
    
    while True:
        print("\nSelect Operation: ")
        print("1. Addition ➕ ")
        print("2. Subtraction ➖ ")
        print("3. Multiplication ✖️ ")
        print("4. Division ➗ ")
        print("5. Exiting ")

        op = input("\nEnter Your Choice (1/2/3/4/5): ")

        if op == '5':
            print("Exiting Calculator : GoodBye 👋 ")
            break

        a = float(input("Enter Your First Number: "))
        b = float(input("Enter Your Second Number: "))

        if op == '1':
            print(f"Result = {add(a,b)}")
        elif op == '2':
            print(f"Result = {subtract(a,b)}")
        elif op == '3':
            print(f"Result = {multiply(a,b)}")
        elif op == '4':
            print(f"Result = {divide(a,b)}")
        else:
            print("Invalid Choice! Please try again")
            continue
        
        again = input("Do you want to Continue? (y/n): ").lower()
        if again == 'n':
            print("\nThanks For Using Calculator!👋\n")
            break

calculator()
