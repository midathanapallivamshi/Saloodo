#!/usr/bin/env python3
import random
# Json module import only if we are reading json input reading and currently we are not reading json input and hence commenting out
# import json

def reverse_string(str_input):
    """
    This method is used to reverse a string
    """
    reverse_string = str_input[1:]
    return reverse_string

def generate_random_number():
    """
    This method is used to generate random number between 1 and 10000
    """
    random_number = random.randint(1,10000)
    return random_number

# defining in dict format and later required to replace with json input readable code. 
input_json = {"message": "abcdef"}

# empty dict to store output
output = {}

# Get reverse string 
get_reverse_str = reverse_string(input_json["message"])
output["message"] = get_reverse_str

# Get a random number
random_number = generate_random_number()
output["random"] = random_number

# Print output to console
print(json.dumps(output))
