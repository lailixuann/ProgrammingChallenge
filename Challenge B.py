"""
Challenge B

Create a program that will read the generated file above and print to the console the object and
its type. Spaces before and after the alphanumeric object must be stripped.
"""

def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    