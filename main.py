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
