"""
Challenge B

Create a program that will read the generated file above and print to the console the object and
its type. Spaces before and after the alphanumeric object must be stripped.
"""

import sys

def identify_obj_type(obj):
    obj = obj.strip()

    if obj.isalpha():
        return "Alphabetical String"
    
    elif obj.isdigit():
        return "Integer"
    
    try:
        float(obj)
        return "Real Number" if '.' in obj else "Integer"
    
    except ValueError:
        return "Alphanumeric" if obj.isalnum() else "Unknown"

    

def read_file(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    obj = content.split(',')

    with open(output_file, 'w') as output_file:
        for i in obj[:5]:
            i = i.strip()
            obj_type = identify_obj_type(i)
            output_file.write(f"Object: '{i}', Type: {obj_type}")


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    read_file(input_file, output_file)
    