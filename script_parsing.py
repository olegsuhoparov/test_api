import json

json_file = '{"messages": [{"message": "This is the first message", "timestamp": "2021-06-04 16:40:53"}, {"message": "And this is a second message", "timestamp": "2021-06-04 16:41:01"}]}'

obj = json.loads(json_file)

print(obj["messages"][1])
