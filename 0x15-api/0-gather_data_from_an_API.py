#!/usr/bin/python3
import requests  # Import the requests module to make HTTP requests
import sys  # Import the sys module to access command-line arguments

if __name__ == '__main__':  # Check if this script is being run as the main program
    if len(sys.argv) != 2:  # Check if the number of command-line arguments is correct
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))  # Print usage instructions
        sys.exit(1)  # Exit the program with an error code

    employee_id = sys.argv[1]  # Get the employee ID from the command-line argument
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)  # Construct the URL for the user data API endpoint
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)  # Construct the URL for the TODO list API endpoint

    user_response = requests.get(user_url)  # Make an HTTP GET request to get the user data
    todo_response = requests.get(todo_url)  # Make an HTTP GET request to get the TODO list data

    if user_response.status_code != 200:  # Check if the user data API returned an error
        print('User not found')  # Print an error message
        sys.exit(1)  # Exit the program with an error code

    if todo_response.status_code != 200:  # Check if the TODO list API returned an error
        print('TODO list not found')  # Print an error message
        sys.exit(1)  # Exit the program with an error code

    user_data = user_response.json()  # Parse the JSON response from the user data API
    todo_data = todo_response.json()  # Parse the JSON response from the TODO list API

    total_tasks = len(todo_data)  # Get the total number of tasks in the TODO list
    done_tasks = sum([1 for task in todo_data if task['completed']])  # Get the number of completed tasks in the TODO list

    print('{} is done with tasks({}/{}):'.format(user_data['name'], done_tasks, total_tasks))  # Print a message showing how many tasks are done and how many are left

    for task in todo_data:  # Loop through each task in the TODO list
        if task['completed']:  # Check if this task is completed
            print('\t {}'.format(task['title']))  # Print this task's title with a tab character at the beginning
