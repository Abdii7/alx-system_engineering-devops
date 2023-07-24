#!/usr/bin/python3

"""
Python script that exports data in the JSON format.
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    # Send a GET request to 'https://jsonplaceholder.typicode.com/todos/' 
    # and store the response in a variable called response.
    response = get('https://jsonplaceholder.typicode.com/todos/')
    # Convert the response into JSON format and store it in a variable called data.
    data = response.json()

    # Create an empty list called row.
    row = []
    # Send a GET request to 'https://jsonplaceholder.typicode.com/users' 
    # and store the response in a variable called response2.
    response2 = get('https://jsonplaceholder.typicode.com/users')
    # Convert the response into JSON format and store it in a variable called data2.
    data2 = response2.json()

    # Loop through each item in data2.
    for i in data2:
        # Check whether the 'id' key of the current item matches the 
        # argument passed in from the command line.
        if i['id'] == int(argv[1]):
            # If it does, store the value of its 'username' 
            # key in a variable called u_name and its 'id' key 
            # in a variable called id_no.
            u_name = i['username']
            id_no = i['id']

    # Create an empty list called row.
    row = []

    # Loop through each item in data.
    for i in data:
        # Check whether the 'userId' key of the current 
        # item matches the argument 
        # passed in from the command line.
        if i['userId'] == int(argv[1]):
            # If it does, create a new dictionary with keys 'username', 'task', and 
            # 'completed', and values u_name, i['title'], and i['completed'], respectively.
            new_dict = {}
            new_dict['username'] = u_name
            new_dict['task'] = i['title']
            new_dict['completed'] = i['completed']
            # Append this dictionary to the list called row.
            row.append(new_dict)

    # Create a new dictionary called final_dict with key id_no and value row.
    final_dict = {}
    final_dict[id_no] = row
    # Convert this dictionary into JSON format and store it in a variable called json_obj.
    json_obj = json.dumps(final_dict)

    # Open a file with name argv[1] + ".json" (which is based on the argument passed in 
    # from the command line) and write json_obj to it.
    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
