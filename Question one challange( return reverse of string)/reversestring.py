import random
import json

def reverse_string(str_input):
    return str_input[1:]

def generate_random_number():
    num = random.randint(1,10000)
    return num


input_json = {"message": "abcdef"}

output = {}


get_reverse_str = reverse_string(input_json["message"])
output["message"] = get_reverse_str

random_number = generate_random_number()

output["random"] = random_number
print(json.dumps(output))
