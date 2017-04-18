#!/usr/bin/python3
"""
Using task #0, export data in the JSON format for all employees
"""
import requests
import json


if __name__ == "__main__":
    api = 'https://jsonplaceholder.typicode.com'
    users = requests.get(api + '/users').json()

    allDict = dict()
    for user in users:
        taskList = list()
        todos = requests.get(api + 'users/{}/todos'.format(user.get('id')))
        for task in todos:
            tasks = dict()
            tasks["completed"] = task.get("completed")
            tasks["task"] = task.get("title")
            tasks["username"] = user.get('username')
            taskList.append(tasks)
        allDict[user.get('id')] = taskList

    with open("todo_all_employees.json", mode='w') as jf:
        json.dump(allDict, jf)
