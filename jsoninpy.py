import json
x='{"name":"Krishna","age":18,"city":"New York"}'
y=json.loads(x)
print(y["age"])                                    #for the specific loding of a variable 



import json
x = {
  "name": "Krishna",
  "age": 18,
  "city": "New York"
}
y = json.dumps(x)
print(y)                                             #for dumping the whole json dict. made



import json
print(json.dumps({"name": "Krishna", "age": 18}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))



import json
x = {
  "name": "Krishna",
  "age": 18,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Porsche 911", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))              # use four indents to make it easier to read the result
 



import json
x = {
  "name": "Krishna",
  "age": 18,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, separators=(". ", " = ")))   # use . and a space to separate objects, and a space, a = and a space to separate keys from their values



import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, sort_keys=True))  # sort the result alphabetically by keys
