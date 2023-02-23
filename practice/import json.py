import json

d = {
    "name":"Sam",
    "age":26,
    "married":True,
    "city":"Berlin",
    "languages":["English","Dutch"]

}
with open('output.json','w') as f:
    json.dump(d, f)


