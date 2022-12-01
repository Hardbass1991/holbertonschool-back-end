#!/usr/bin/python3
"""Module that fetches data and exports it in csv format
"""
import json
from sys import argv
import urllib.request

# First we get the name of the employee
url = "https://jsonplaceholder.typicode.com/users/"
webURL = urllib.request.urlopen(url)
data = webURL.read()
JSON_object = json.loads(data.decode('utf-8'))

username = JSON_object[int(argv[1]) - 1]["username"]

# Then we fetch the tasks
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
webURL = urllib.request.urlopen(url)
data = webURL.read()

tasks = json.loads(data.decode('utf-8'))

dct = {}
task_list = []
for task in tasks:
    d_task = {}
    d_task["task"] = task["title"]
    d_task["completed"] = task["completed"]
    d_task["username"] = username
    
    task_list.append(d_task)

dct[argv[1]] = task_list

with open("{}.json".format(argv[1]), "w") as f:
    f.write(json.dumps(dct))
