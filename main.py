import json
import os
from datetime import datetime

class Todolist:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # load tasks from JSON file
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    return json.load(file)
            
            except (json.JSONDecodeError, IOError):
                print("Warrning: Could not load tasks file. Starting with empty list.")
                return []
            
        return []
    
    # Save task from JSON file
    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.task, file, indent=2)

        except IOError:
            print("Error: Couldn't save tasks to the file")

    # Add a new task to the file
    def add_task(self, description):

        if not description.strip():
            print("Error: Task description cannot be empty")
            return False
        
        task = {
            'id': len(self.tasks) + 1,
            'description': description.strip(),
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H-%M-%S"),
            'completed_at': None
        }

        self.task.append(task)
        self.save_task()
        print(f"Added task: {description.strip()}")
        return True


    # Display all Tasks
    def list_tasks(self, show_completed=True):
        if not self.tasks:
            print("No tasks in your todo list")
            return
        
        print("\n" + "="*20)
        print("YOUR TO-DO LIST")
        print("="*20)

        for task in self.tasks:
            if not show_completed and task['completed']:
                continue

            status = "Done" if task['completed'] else "Still"
            completed_info = f"(Completed: {task['completed_at']})" if task ['completed'] else ""

            print(f"{task['id']:3d}. [{status}] {task['description']}{completed_info}")

             # Show statistics
            total = len(self.tasks)
            completed = sum(1 for task in self.tasks if task['completed'])
            pending = total - completed
        
            print("="*20)
            print(f"Total: {total} | Completed: {completed} | Pending: {pending}")
            print("="*20)

        
    # Delete a task by ID
    def delete_task(self, task_id):

        task_to_delete = None

        for task in self.tasks:
            if task['id'] == task_id:
                task_to_delete = task
                break

        if not task_to_delete:
            print(f"Error: Task with ID {task_id} not found.")
            return False

        # Reassign IDs to maintain sequential order
        for i, task in enumerate(self.tasks, 1):
            task['id'] = i

        self.save_tasks()
        print(f"Deleted task: {task_to_delete['description']}")
        return True
    
    # Mark a task as Completed
    def mark_completed(self, task_id):
        task_to_complete = None

        for task in self.tasks:
            if task['id'] == task_id:
                task_to_complete = task
                break

        if not task_to_complete:
            print(f"Task with ID {task_id} not Completed.")
            return False

        if task_to_complete['completed']:
            print(f"Task '{task_to_complete['description']}' is already completed.")
            return True

        task_to_complete['completed'] = True
        task_to_complete['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save_tasks()

        print(f"Completed task: {task_to_complete['description']}")
        return True
    
    # Mark a task as pending
    def mark_pending(self, task_id):
        task_to_pending = None

        for task in self.tasks:
            if task['id'] == task_id:
                task_to_pending = task
                break

        if not task_to_pending:
            print(f"Task with ID {task_id} not pending.")
            return False
        
        if task_to_pending['pending']:
            print(f"Task '{task_to_pending['description']}' is already peding.")
            return True
        
        task_to_pending['pending'] = True
        task_to_pending['pending_at'] = None
        self.save_tasks()
        print(f"Marked as pending '{task_to_pending['description']}'")
        return True
    

        
