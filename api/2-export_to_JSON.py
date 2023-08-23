#!/usr/bin/python3
"""Script to use a REST API"""

import json
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

        emp_username = user_data['username']
        user_id = user_data['id']
        file_name = f'{user_id}.json'
        user_info = []

        for value in todos_data:
            task_info = {'task': value['title'],
                         'completed': value['completed'],
                         'username': emp_username}
            user_info.append(task_info)

        json_data = {user_id: user_info}

        with open(file_name, 'w') as json_file:
            json.dump(json_data, json_file)

    else:
        print(f"Error: Unable to fetch data for employee ID {employee_id}")
        exit(1)
