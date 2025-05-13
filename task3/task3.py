import sys
import json

path_values = sys.argv[1]
path_tests = sys.argv[2]
path_report = sys.argv[3]

with open(path_values, 'r') as file:
    data_values = json.load(file)

with open(path_tests, 'r') as file:
    data_tests = json.load(file)


result = {i['id']: i['value'] for i in data_values['values']}

def recurs(test):
    id_number = test.get('id')
    if id_number in result:
        test['value'] = result[id_number]
    if 'values' in test:
        for test_1 in test['values']:
            recurs(test_1)


for i in data_tests['tests']:
    recurs(i)



with open(path_report, 'w') as f:
    json.dump(data_tests, f, indent=2)