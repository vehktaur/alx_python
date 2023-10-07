"""
This module serves as a utility for interacting with a REST API to retrieve employee data and their associated todo tasks. It provides functionality to request data from the API, process it, and export it into JSON format.

Usage:
    To use this module, provide an employee ID as a command-line argument when running the script. The module will then retrieve information about the specified employee, including their name and a list of todo tasks. It calculates the progress of completed tasks and exports this data into a JSON file.
"""

import json
import requests
import sys


def main():
    """
    main class function
    for the export to JSON module
    """
    employee_id = sys.argv[1]

    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    print(
        "Employee {} is done with tasks ({}/{}):".format(
            employee_data.get("name"), completed_tasks, total_tasks
        ))

    for task in todo_data:
        if task.get("completed"):
            print(f"\t{task.get('title')}")

    employee_json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_data.get("username")
            }
            for task in todo_data
        ]
    }

    json_file_name = f"{employee_id}.json"
    with open(json_file_name, "w") as json_file:
        json.dump(employee_json_data, json_file, indent=4)

    print(f"Data exported to {json_file_name}")


if __name__ == "__main__":
    main()
