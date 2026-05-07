# Todo list ver 1 very basic
print("Welcome to basic Todo List Program")

tasks = []   # <-- move this OUTSIDE the loop

while True:
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Remove tasks")
    print("4. Exit")
    choice = input("Enter a choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks there")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks there")
        else:
            for index, task in enumerate(tasks, start=1):
                print(index, task)
            try:
                num = int(input("Enter a task number to remove: "))
            except ValueError:
                print("Wrong number  pls try again")
                continue
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
                print("Task removed")
            else:
                print("Invalid task number")

    elif choice == "4":
        break

print("Thx for using this simple todo list")