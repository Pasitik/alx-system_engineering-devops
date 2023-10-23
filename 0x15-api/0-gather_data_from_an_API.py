#!/usr/bin/python3
import requests
import sys

base = "https://jsonplaceholder.typicode.com"
id = sys.argv[1]
users = "/users/{}".format(id)
todos = "/todos?userId={}".format(id)

rEmp = requests.get(base + users)
rTodos = requests.get(base + todos)
tasks = rTodos.json()
EMPLOYEE_NAME = rEmp.json()["name"]
completed_tasks = 0
for task in tasks:
    if task["completed"] is True:
        completed_tasks += 1
print("Employee {} is done with tasks({}/{})"
      .format(EMPLOYEE_NAME, completed_tasks, len(tasks)))
for task in tasks:
    if task["completed"] == True:
        print("\t {}\n".format(task["title"]))
