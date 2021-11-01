import json

file = open('InitialPro.csv',"r")

lines = file.readlines()

index = lines[0][1:-1].split(',')
payload = lines[1:]
values = [];

for v in payload:
  temp = v[:-1].split(',')
  values.append(temp)

def getIndex(c):
  try:
    return index.index(c)
  except:
    return -1

def getValue(a,b):
  index_a = getIndex(a)
  index_b = getIndex(b)
#  if index_a < 0 or index_b < 0:
  return values[index_a][index_b]


_json = {
  'index': index,
  'values': values
}

output = json.dumps(_json)
print(output)