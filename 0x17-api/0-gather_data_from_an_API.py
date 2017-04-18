#!/usr/bin/python3
"""
Returns infomation about an employee's todo list progress when ID is given
"""
import requests
import sys


def gather_api_data(userId):
    api = 'https://jsonplaceholder.typicode.com'
    name = requests.get(api + '/users/' + sys.argv[1]).json().get("name")
    todos = requests.get(api + '/todos?userId=' + sys.argv[1]).json()
    completed = requests.get(api + '/todos?completed=true&userId=' +
                             sys.argv[1]).json()

    print("Employee {} is done with tasks({:d}/{:d}):".
          format(name, len(completed), len(todos)))
    for task in completed:
        print("\t ", end="")
        print(task.get("title"))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            userId = int(sys.argv[1])
            gather_api_data(userId)
        except:
            pass
