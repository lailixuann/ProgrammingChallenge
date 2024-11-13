"""
Challenge B

Create a program that will read the generated file above and print to the console the object and
its type. Spaces before and after the alphanumeric object must be stripped.
"""

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

    

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    obj = content.split(',')

    for i in obj[:5]:
        obj_type = identify_obj_type(i)
        print(f"Object: '{i}', Type: {obj_type}")


read_file('output.txt')
    
    