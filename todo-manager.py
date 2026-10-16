# a todo list manager that allows users to add, view, and remove tasks

tasks = ["Buy groceries", "Finish homework", "Call the dentist"]

print("=" * 20)
print("My To-Do List")
print("=" * 20)

# displays the list of tasks in the todo list numbered
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")
    
# show total number of tasks
print(f"Total number of tasks: {len(tasks)}")

# asks the user if they would like to add or remove a task then allows the user to add a new task or remove an existing task based on their input
choose = input("What would you like to do? (Add a task/Remove a task): ")
if choose == "Add a task":
    new_task = input("Enter a new task: ")
    tasks.append(new_task)
elif choose == "Remove a task":
    remove_task_index = int(input("Enter the number of the task to remove: ")) - 1
    try:
        tasks.pop(remove_task_index)
    except IndexError:
        print("Invalid task number.")

# displays the updated list of tasks
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")

# show total number of tasks
print(f"Total number of tasks: {len(tasks)}")


    
    