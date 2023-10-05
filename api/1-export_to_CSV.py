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
            f"Employee {employee_data.get('name')} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Print titles of completed tasks
        for task in todo_data:
            if task.get("completed"):
                print(f"\t{task.get('title')}")

        # Export data to CSV
        csv_file_name = f"{employee_id}.csv"
        with open(csv_file_name, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(
                csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # Write CSV header
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            # Write TODO list data to CSV
            for task in todo_data:
                csv_writer.writerow(
                    [employee_id, employee_data.get('name'), task.get("completed"), task.get('title')])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_info(employee_id)
