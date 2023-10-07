import csv
import requests
import sys

employee_id = int(sys.argv[1])

# URL for employee details
employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
# URL for employee's TODO list
todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

# Fetch employee details
employee_response = requests.get(employee_url)
employee_data = employee_response.json()

# Fetch TODO list
todo_response = requests.get(todo_url)
todo_data = todo_response.json()

# Calculate TODO list progress
total_tasks = len(todo_data)
completed_tasks = sum(1 for task in todo_data if task.get("completed"))


# Export data to CSV
csv_file_name = f"{employee_id}.csv"
with open(csv_file_name, mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    # Write TODO list data to CSV
    for task in todo_data:
        csv_writer.writerow([employee_id, employee_data.get(
            'name'), str(task.get('completed')), task.get('title')])
