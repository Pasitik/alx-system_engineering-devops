#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import requests
import csv
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    filename = id + ".csv"
    base = "https://jsonplaceholder.typicode.com"
    users = "/users/{}".format(id)
    todos = "/todos?userId={}".format(id)

    rEmp = requests.get(base + users)
    rTodos = requests.get(base + todos)
    tasks = rTodos.json()
    EMPLOYEE_NAME = rEmp.json()["name"]

    with open(filename, "w") as file:
        csv_file = csv.writer(file)
        for task in tasks:
            csv_file.writerow([id, rEmp.json()["username"],
                               task["completed"], task["title"]])
