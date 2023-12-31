"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
import json
import requests


# URL for employee details
employees_url = "https://jsonplaceholder.typicode.com/users"

# Fetch the list of employees
employees_response = requests.get(employees_url)
employees_data = employees_response.json()

# Create a dictionary to store data for all employees
all_employee_data = {}

for employee in employees_data:
    employee_id = employee.get("id")
    employee_name = employee.get("username")

    # URL for employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch TODO list for the current employee
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Create a list to store TODO items for the current employee
    todo_list = []

    # Populate the TODO list for the current employee
    for task in todo_data:
        task_title = task.get("title")
        task_completed = task.get("completed")
        todo_list.append(
            {"username": employee_name, "task": task_title, "completed": task_completed})

    # Add the TODO list for the current employee to the dictionary
    all_employee_data[employee_id] = todo_list

# Export data to JSON
json_file_name = "todo_all_employees.json"
with open(json_file_name, 'w') as json_file:
    json.dump(all_employee_data, json_file, indent=4)

print(f"Data for all employees exported to {json_file_name}")
