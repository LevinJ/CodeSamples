import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  'lines': [[(1,2),(2,5)],[2,3,4]]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)