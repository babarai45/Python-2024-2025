import time

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"\n✅  Task '{task}' has been successfully added!\n")

    def remove_task_by_id(self, task_id):
        # Check if task_id is valid
        if 1 <= task_id <= len(self.tasks):
            removed_task = self.tasks.pop(task_id - 1)  # Convert task_id to 0-based index
            print(f"\n🗑️ Task '{removed_task}' has been successfully removed.\n")
        else:
            print(f"\n⚠️ Invalid task ID '{task_id}'. Please enter a valid ID.\n")

    def view_tasks(self):
        if self.tasks:
            print("\n📝 Current To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"   {i}. {task}")
        else:
            print("\n📭 Your To-Do List is currently empty.\n")

    def clear_tasks(self):
        self.tasks.clear()
        print("\n🧹 All tasks have been cleared from your list!\n")

    def switch_case(self, choice, task=None, task_id=None):
        operations = {
            "1": self.add_task,
            "2": lambda task: self.remove_task_by_id(task_id),
            "3": self.view_tasks,
            "4": self.clear_tasks
        }
        func = operations.get(choice)
        if func:
            if choice == "1" and task:  # Add task
                func(task)
            elif choice == "2" and task_id is not None:  # Remove by ID
                func(task_id)
            else:  # View and Clear tasks
                func()
        else:
            print("❌ Invalid choice. Please try again.\n")

# Display Welcome Message
def display_welcome():
    print("\n" + "="*40)
    print("🎉 Welcome to Your Professional To-Do List App 🎉")
    print("="*40)
    time.sleep(1)
    print("Manage your tasks efficiently and stay organized!\n")

# Main ToDoList Execution
def main():
    display_welcome()
    todo_list = ToDoList()
    
    while True:
        print("\nPlease select an option from the menu below:")
        print("1️⃣  Add a Task")
        print("2️⃣  Remove a Task by ID")
        print("3️⃣  View All Tasks")
        print("4️⃣  Clear All Tasks")
        print("5️⃣  Exit\n")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "5":
            print("\n👋 Exiting the To-Do List App. Have a productive day!\n")
            break
        elif choice == "1":
            task = input("Please enter the task description: ").strip()
            todo_list.switch_case(choice, task=task)
        elif choice == "2":
            try:
                task_id = int(input("Enter the task ID to remove: ").strip())
                todo_list.switch_case(choice, task_id=task_id)
            except ValueError:
                print("\n⚠️ Please enter a valid numeric ID.\n")
        else:
            todo_list.switch_case(choice)

# Run the app
if __name__ == "__main__":
    main()
