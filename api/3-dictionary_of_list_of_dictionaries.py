#!/usr/bin/python3
"""Script to use a REST API"""

import json
import requests
from sys import exit

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/users'
    user_response = requests.get(base_url)

    if user_response.status_code == 200:
        users_data = user_response.json()

        todos_data_all_employees = {}

        for user in users_data:
            employee_id = user['id']
            employee_name = user['name']
            emp_username = user['username']
            todos_url = f'{base_url}/{employee_id}/todos'
            todos_response = requests.get(todos_url)
            if todos_response.status_code == 200:
                todos_data = todos_response.json()
                employee_tasks = []
                for todo in todos_data:
                    task_info = {"username": emp_username,
                                 "task": todo['title'],
                                 "completed": todo['completed']}
                    employee_tasks.append(task_info)
                todos_data_all_employees[employee_id] = employee_tasks

        file_name = 'todo_all_employees.json'

        with open(file_name, 'w') as json_file:
            json.dump(todos_data_all_employees, json_file)

    else:
        print(f"Error: Unable to fetch user data")
        exit(1)
