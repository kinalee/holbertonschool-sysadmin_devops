#!/usr/bin/python3
"""
Returns infomation about an employee's todo list progress when ID is given
"""
import sys
import requests

if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com'
    if len(sys.argv) == 2:
        name = requests.get(api + '/users/' + sys.argv[1]).json().get("name")
        todos = requests.get(api + '/todos?userId=' + sys.argv[1]).json()
        completed = requests.get(api + '/todos?completed=true&userId=' +
                                 sys.argv[1]).json()

        print("Employee {} is done with tasks({:d}/{:d}):".
              format(name, len(completed), len(todos)))
        for task in completed:
            print("\t", end="")
            print(task.get("title"))
    else:
        pass
