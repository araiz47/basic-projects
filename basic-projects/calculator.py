#Basic calculator project ver 1
def add(x,y):   #Created functions to avoid clutter in main code
    result = x + y
    return result

def subtract(x,y):
    result = x - y
    return result

def multiply(x,y):
    result = x * y
    return result

def divide(x,y):
    result = x / y
    return result

while True: #added while statement to loop through the choices
    print("Basic Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice (1 to 5): "))
    num1 = int(input("Enter first number: ")) #Get the first num
    num2 = int(input("Enter second number: ")) #Get the second num

    if choice == 1:
        print("Result: ",add(num1,num2))
    
    elif choice == 2:
        print("Result: ",subtract(num1,num2))

    elif choice == 3:
        print("Result: ",multiply(num1,num2))
    
    elif choice == 4:
        print("Result: ",divide(num1,num2))

    else:
        print("Exiting now....")
        break 
        
