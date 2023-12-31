import csv
import requests
import sys


def get_employee_info(employee_id):
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
            f"Employee {employee_data.get('name')} is done with tasks({completed_tasks}/{total_tasks}):")

        # Print titles of completed tasks
        for task in todo_data:
            if task.get("completed"):
                print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
