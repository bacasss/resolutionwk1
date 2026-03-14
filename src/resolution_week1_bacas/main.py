#added: version, priority, message when no tasks
#to add task: in terminal, type python main.py "your task name" -p (type a number 1 - 3 for priority, where 3 is the highest priority)




import argparse
import sys
import os
import json

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_task(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action = "version", version = "Version: 0.0.2", help = "Shows the version of the code.")
    parser.add_argument("task", type=str, nargs="?", help="Task to add")
    parser.add_argument("-p", "--priority", type = int, choices = [1, 2, 3], help = "Set task priority, higher is more priority. To be added after python main.py (task name).")
    parser.add_argument("-l", "--list", help="List all tasks", action="store_true")
    parser.add_argument("-c", "--complete", type=int, help="Mark a task as complete by ID")
    parser.add_argument("-d", "--delete", type=int, help="Delete a task by ID")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
        
    # if args.task:
        
    #     tasks = load_tasks()

    #     if len(tasks) == 0:
    #         new_id = 1
    #     else:
    #         new_id = tasks[-1]["id"] + 1

    #     tasks.append({"id": new_id, "tasks": args.task, "done": False})
    #     save_task(tasks)

    #     print(f"Task {args.task} added with ID of {new_id}")


    if args.list:
        tasks = load_tasks()
        if len(tasks) == 0:
            print("No tasks yet!")
            sys.exit(0)
        for task in tasks:
            status = "x" if task["done"] else " "
            print(f"[{status}] {task['id']}: {task['task']}, Prioriry: {task['priority']}")
        sys.exit(0)

    elif args.complete:
        tasks = load_tasks()
        for task in tasks:
            if task["id"] == args.complete:
                task["done"] = True
                save_task(tasks)
                print(f"Task {args.complete} marked as complete")
                break

    elif args.delete:
        tasks = load_tasks()
        new_tasks = []
        for task in tasks:
            if task["id"] != args.delete:
                new_tasks.append(task)
        save_task(new_tasks)
        print(f"Task with ID of {args.delete} deleted")

    elif args.task:
        tasks = load_tasks()
        if len(tasks) == 0:
            new_id = 1
        else:
            new_id = tasks[-1]["id"] + 1
        tasks.append({"id": new_id, "task": args.task, "done": False, "priority": args.priority})
        save_task(tasks)

        print(f"Task {args.task} added with ID of {new_id} and priority of {args.priority}")



if __name__ == "__main__":
    main()