#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
import json

if __name__ == "__main__":
    # Get the TODO list
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    
    # Get the user data
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    new_dict1 = {}

    # Loop through each user
    for j in data2:

        row = []
        
        # Loop through each task
        for i in data:

            new_dict2 = {}

            if j['id'] == i['userId']:

                new_dict2['username'] = j['username']
                new_dict2['task'] = i['title']
                new_dict2['completed'] = i['completed']
                row.append(new_dict2)

        new_dict1[j['id']] = row

    # Write the data to a JSON file
    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
