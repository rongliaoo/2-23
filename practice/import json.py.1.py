import json

d = {
    "name":"Amy",
    "age":20,
    "married":False,
    "city":"Nee york",
    "languages":["English","French"]

}
with open('data.json','w') as f:
    json.dump(d, f)


