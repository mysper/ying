import json

file = open('InitialPro.csv',"r")

lines = file.readlines()

index = lines[0][1:-1].split(',')
payload = lines[1:]
values = [];

for v in payload:
  temp = v[:-1].split(',')
  values.append(temp)


_json = {
  'index': index,
  'values': values
}

output = json.dumps(_json)
print(output)