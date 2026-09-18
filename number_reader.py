import json

filename = 'number.json'
with open(filename) as f_obj:
    number_1 = json.load(f_obj)

print(number_1)