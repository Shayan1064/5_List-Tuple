#  To-Do List Manager (Simple) → Add, remove, and view tasks using a list.

tasks = []

while True:
    print("\n--- To-Do List Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))
    if(choice==1):
        task=input("Enter Task Name: ")
        tasks.append(task)
        print("Task Added")
    elif(choice==2):
        if(not tasks):
            print("List is Empty")
        else:
            print("\nYour Task")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif(choice==3):
        if(not tasks):
            print("No Task To Remove")
        else:
            task=input("Enter Task Name to Remove: ")
            if(task not in tasks):
                print(task," Is Not Present")
            else:
                tasks.remove(task)

    else:
        print("Invalid Choice....!")