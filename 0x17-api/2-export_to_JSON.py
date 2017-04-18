#!/usr/bin/python3
"""
Using task #0, export data in the JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        api = 'https://jsonplaceholder.typicode.com'
        username = requests.get(api + '/users/' +
                                sys.argv[1]).json().get("username")
        todos = requests.get(api + '/users/' + sys.argv[1] +
                             '/todos').json()

        taskList = list()
        for task in todos:
            tasks = dict()
            tasks["completed"] = task.get("completed")
            tasks["task"] = task.get("title")
            tasks["username"] = username
            taskList.append(tasks)

        filename = "{}.json".format(sys.argv[1])
        with open(filename, mode='w') as jf:
            json.dump({sys.argv[1]: taskList}, jf)
