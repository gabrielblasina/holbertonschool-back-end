#!/usr/bin/python3
"""Script to use a REST API"""

import requests
from sys import argv
from sys import exit

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py employee_id")
        exit(1)

    employee_id = argv[1]

    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo['completed'])

        print(f'Employee {employee_name} is done with tasks'
              f'({completed_tasks}/{total_tasks}):')

        for todo in todos_data:
            if todo['completed']:
                print(f'\t{todo["title"]}')

    else:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        exit(1)
