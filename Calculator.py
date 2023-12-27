#Function add
def add(x,y):
    return x + y

#Function substract
def sub(x,y):
    return x - y

#Function  Multiplication
def mul(x,y):
    return x * y

#Function divide
def div(x , y):
    if y == 0:
        print("Can't divisivle by Zero")
    else:
        return x / y

#Function Reminder
def rem(x,y):
    return x % y

while True:
    print('''Option:
Enter 'add' for addition:
Enter 'sub' for subtraction:
Enter 'mul' for multiplication:
Enter 'div' for divition:
Enter 'rem' for reminder:
Enter 'quit' for quit the calculation:
    ''')
    
    user_input = input("Enter : ").lower()
    
    if user_input == 'quit':
        break
    elif user_input in ("add","sub","mul","div","rem"):
        x = float(input("Enter the value of first number: "))
        y = float(input("Enter the value of second number: "))
        
        if user_input == 'add':
            print("Result: ", add(x,y))
        elif user_input == 'sub':
            print("Result: ", sub(x,y))
        elif user_input == 'mul':
            print("Result: ", mul(x,y))
        elif user_input == 'div':
            print("Result: ", div(x,y))
        elif user_input == 'rem':
            print("Result: ", rem(x,y))
        
    else:
        print("Invalid value")