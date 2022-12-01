#!/usr/bin/python3
"""Module that fetches data from all tasks and all employees.
And exports that into a json file
"""
import json
import urllib.request

# First we get the name of the employee
url = "https://jsonplaceholder.typicode.com/users/"
webURL = urllib.request.urlopen(url)
data = webURL.read()
users = json.loads(data.decode('utf-8'))



dct = {}
for user in users:
    task_list = []

    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
    user["id"])
    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    tasks = json.loads(data.decode('utf-8'))

    for task in tasks:
        d_task = {}
        d_task["username"] = user["username"]
        d_task["task"] = task["title"]
        d_task["completed"] = task["completed"]
    
        task_list.append(d_task)

    dct[user["id"]] = task_list

with open("todo_all_employees.json", "w") as f:
    f.write(json.dumps(dct))
