"""
Challenge A

Write a program that will generate four (4) types of printable random objects and store them in a
single file, each object will be separated by a ",". 

These are the 4 objects: 
- alphabetical strings
- real numbers
- integers
- alphanumerics

The alphanumerics should contain a random number of spaces before and after it (not exceeding 10 spaces). The output should be 10MB in size.
"""

import random
import string

def generate_alphabetical_string():
    return str(random.choice(string.ascii_letters))

def generate_real_number():
    return str(random.uniform(-1e6, 1e6))

def generate_integer():
    return str(random.randint(-1e6, 1e6))
    
def generate_alphanumerics():
    alphanumeric = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    spaces_before = ' ' * random.randint(0, 10)
    spaces_after = ' ' * random.randint(0, 10)
    return str(spaces_before + alphanumeric + spaces_after)

def save_file(filename, target_size = 10 * 1024 * 1024):
    current_size = 0
    with open(filename, "w") as file:
        while current_size < target_size:
            data = random.choice([generate_alphabetical_string, generate_real_number, generate_integer, generate_alphanumerics])()
            file.write(data + ',')
            current_size += len(data) + 1
        
save_file('output.txt')

