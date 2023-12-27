#taking an empty list to perform a perticular task
tasks = [ ]

#function to add a task in to-do list
def add_task(task):
    tasks.append(task)
    print("Task added: ", task)
    
    
#function to view all the task in to-do  
def view_task(task):
    if not tasks:
        print("No task found")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks,start=1):
            print(f"{i}.{task}")

#function to remove a task from a to-do list            
def remove_task(task_number):
    if 1<= task_number <= len(tasks):
        remove_task= tasks.pop(task_number-1)
        print(f"Task removed: {remove_task}")
    else:
        print("Invalid task number")

#Function to edit a task from a to-do list      
def edit_task(task_number):
    if 1<= task_number <= len(tasks):
         tasks[task_number-1] = input("Edit task: ")
         print(f"Task Edited: {task}")
    else:
        print("Invalid task number")
        
while True:
    print('''
Option:
Enter 'add' to add a task:
Enter 'view' to view all tasks:
Enter 'remove' to remove a task:
Enter 'edit' to edit a perticular task:
Enter 'quit' to exit the to-do list:
''')
    
    user_input = input("Enter: ").lower()
    
    if user_input == "quit":
        break
    elif user_input == "add":
        task=input("Enter Your Task: ")
        add_task(task)
    elif user_input == "view":
        view_task(task)
    elif user_input == "remove": 
        view_task(task)
        task_number = int(input("Enter the number of the task to remove: "))
        remove_task(task_number)
    elif user_input == "edit":
        view_task(task)
        task_number = int(input("Enter the number of the task to edit: "))
        edit_task(task_number)
    else:
        print("Invalid user input")