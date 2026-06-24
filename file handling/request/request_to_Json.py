'''consume Rest API and write user data into
a) new Json file users.json(uid,uname,city,company name)
b) new csv file users.csv(uid,uname,city,company name)'''

#Extract data from Rest API 
import requests
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
print(users)
#Transform data - for json file and csv file 
users_json = []
for user in users:
    users_json.append({
        "uid": user["id"],
        "name": user["username"],
        "city": user["address"]["city"],
        "company": user["company"]["name"]
    })
    print(len(users_json))
    print(users_json)
    #Load data into new json file and csv file
    import json
    fp1 = open('user.json','w')
    json.dump(users_json,fp1)
    print("Data written into user.json file successfully")

