#!/usr/bin/python3
import requests
import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        print('User not found')
        sys.exit(1)

    if todo_response.status_code != 200:
        print('TODO list not found')
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    done_tasks = sum([1 for task in todo_data if task['completed']])

    print('{} is done with tasks({}/{}):'.format(user_data['name'], done_tasks, total_tasks))

    with open('{}.csv'.format(employee_id), mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': user_data['username'],
                'TASK_COMPLETED_STATUS': 'Yes' if task['completed'] else 'No',
                'TASK_TITLE': task['title']
            })

    print('Data exported to {}.csv'.format(employee_id))
