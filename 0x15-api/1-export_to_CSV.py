#!/usr/bin/python3

"""
Python script that exports data in the CSV format
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    # Get the TODO list
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    # Get the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    # Find the employee name
    for i in data2:
        if i['id'] == int(argv[1]):
            employee = i['username']

    # Write the data to a CSV file
    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for i in data:

            row = []
            if i['userId'] == int(argv[1]):
                row.append(i['userId'])
                row.append(employee)
                row.append(i['completed'])
                row.append(i['title'])

                writ.writerow(row)
