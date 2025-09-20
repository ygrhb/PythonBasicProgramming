# To-Do List Manager (Beginner-Friendly)

# Ask for player's name
name = input("Welcome to the interactive To-Do Manager! Please enter your name: ")
print("\nHello " + name + ", please select a task from the menu below.\n")

# Global task list
tasklist = []

# --- FUNCTIONS ---
def add_task():
    task = input("Enter your task: ")
    tasklist.append(task)
    print("You have added '" + task + "' to the list!")
    print("Your current tasks are: " + str(tasklist))

def remove_task():
    task = input("Enter the task you want to remove: ")
    if task in tasklist:
        tasklist.remove(task)
        print("You removed '" + task + "' from the list.")
    else:
        print("That task is not in your list.")
    print("Your current tasks are: " + str(tasklist))

def view_tasks():
    print("Your tasks are:")
    for task in tasklist:
        print("- " + task)

def quit_program():
    print("Thank you for using the To-Do Manager, " + name + "!")
    return False  # signals the loop to stop


# --- MAIN LOOP ---
running = True
while running:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Quit")

    choice = input(name + ", please enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        running = quit_program()
    else:
        print("Invalid choice, please try again.")
