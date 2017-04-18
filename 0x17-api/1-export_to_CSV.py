#!/usr/bin/python3
"""
Using task #0, export data in the CSV format
"""
import sys
import requests
import csv


if __name__ == "__main__":
    if len(sys.argv) == 2:
        api = "https://jsonplaceholder.typicode.com"
        username = requests.get(api + '/users/' +
                                sys.argv[1]).json().get("username")
        todos = requests.get(api + '/users/' + sys.argv[1] +
                             '/todos').json()
        filename = "{}.csv".format(sys.argv[1])

        with open(filename, mode='w') as cf:
            writer = csv.writer(cf, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([sys.argv[1], username, task.get("completed"),
                                 task.get("title")])
