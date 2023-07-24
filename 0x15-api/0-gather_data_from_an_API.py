#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns  TODO list progress.
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    # Get the TODO list
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []

    # Get the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Find the employee name
    for i in data2:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')

    # Count the number of completed tasks and total tasks
    for i in data:
        if i.get('userId') == int(argv[1]):
            total += 1

            if i.get('completed') is True:
                completed += 1
                tasks.append(i.get('title'))

    # Print the results
    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
