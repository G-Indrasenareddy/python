import json
emp={
    'eid' : 101,
    'ename' : 'Rahul',
    'esal':45000,
    'avail':True,
    'discount':None
}
emp_json_str=json.dumps(emp)
print(emp_json_str)