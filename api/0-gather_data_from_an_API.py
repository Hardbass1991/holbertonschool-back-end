#!/usr/bin/python3
"""Module that fetches data from online api"""
import json
import urllib.request
from sys import argv

"""First we get the name of the employee"""
url = "https://jsonplaceholder.typicode.com/users/"
webURL = urllib.request.urlopen(url)
data = webURL.read()
JSON_object = json.loads(data.decode('utf-8'))

employee_name = JSON_object[int(argv[1]) - 1]["name"]

"""Then we fetch the tasks"""
url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
webURL = urllib.request.urlopen(url)
data = webURL.read()

all_tasks = json.loads(data.decode('utf-8'))
done_tasks = [x for x in all_tasks if x["completed"] is True]

print("Employee {} is done with tasks({}/{}):".format(
    employee_name, len(done_tasks), len(all_tasks)
))
for done_task in done_tasks:
    print("\t {}".format(done_task["title"]))
