import requests
import json
import csv
'''Usage: fetch Users
Rest API URL: https://jsonplaceholder.typicode.com/users
Method Type:GET
Req Fields: None
Access Type:Public

consume and print users

consume Rest API and print all user names'''
res_data = requests.get("https://jsonplaceholder.typicode.com/users")
users = res_data.json()
status_code = res_data.status_code
print(users)
print(status_code)

for user in users:
    print(user["username"])



