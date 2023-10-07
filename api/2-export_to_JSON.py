"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
import json
import requests
import sys


employee_id = sys.argv[1]

# URL for employee details
employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
# URL for employee's TODO list
todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

try:
    # Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Fetch TODO list
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    # Print employee's TODO list progress
    print(
        f"Employee {employee_data.get('name')} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Print titles of completed tasks
    for task in todo_data:
        if task.get("completed"):
            print(f"\t{task['title']}")

    # Create a dictionary to represent the data
    employee_json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_data.get('username')
            }
            for task in todo_data
        ]
    }

    # Export data to JSON
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(employee_json_data, json_file, indent=4)

    print(f"Data exported to {json_file_name}")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    sys.exit(1)
