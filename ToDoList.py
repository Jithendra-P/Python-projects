#To do list application in python

import json
import os.path

List = {}
if os.path.isfile('TaskList.json'):
    with open("TaskList.json","r") as file:
        json_object = json.load(file)
        List.update(json_object)

print("To do list application using python")

while(True):
    print("Enter your choice")
    choice = int(input("1.Add Task\n2.Display all Tasks\n3.Mark Task as Completed\n4.Update Task Description\n5.Remove Task\n6.Exit\n"))
    
    if choice == 1:
        title = input("Enter the title for your task: ")
        description = input("Enter the description for your task: ")
        completed = False
        List[title] = {"Description":description, "Completed":completed}
        with open("TaskList.json","w") as file:
            json.dump(List, file)

    elif choice == 2:
        if len(List) != 0:
            for task_name, task_data in List.items():
                description = task_data["Description"]
                completed = task_data["Completed"]
                status = "Completed" if completed else "Not Completed"
                print(f"Task: {task_name} - Description: {description} - Status: {status}")
        else:
            print("No Tasks Found")

    elif choice == 3:
        title = input("Enter the task which you want to mark as completed: ")
        if title in List:
            completed = True
            List[title] = {"Description":description, "Completed":completed}
            with open("TaskList.json","w") as file:
                json.dump(List, file)
            print("Task marked as completed")
        else:
            print("Task not found")

    elif choice == 4:
        title = input("Enter the task whose description you want to update: ")
        if title in List:
            description = input("Enter the description: ")
            List[title] = {"Description":description, "Completed":completed}
            with open("TaskList.json","w") as file:
                json.dump(List, file)
            print("Task updated")
        else:
            print("Task not found")

    elif choice == 5:
        task = input("Enter a task to delete: ")
        if task in List:
            del List[task]
            with open("TaskList.json","w") as file:
                json.dump(List, file)
        else:
            print("Task not found")

    elif choice == 6:
        exit(0)

    else:
        print("Enter a valid choice")

    print("-----------------------------")
        

#restore deleted task
#display completed tasks