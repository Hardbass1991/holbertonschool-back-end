#!/usr/bin/python3
"""Module that fetches data and exports it in csv format"""
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

text = ""
i = 0
for task in tasks:
    i += 1

    text += "\"{}\",\"{}\",\"{}\",\"{}\"".format(
    argv[1], username, task["completed"], task["title"]
    )
    if i != len(tasks):
        text += "\n"

with open("{}.csv".format(argv[1]), "w") as f:
    f.write(text)
