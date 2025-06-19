import json

from string import ascii_lowercase

alphabet = {key: value for value, key in enumerate(ascii_lowercase, 1)}
json_data = json.dumps(alphabet)

print(json_data)