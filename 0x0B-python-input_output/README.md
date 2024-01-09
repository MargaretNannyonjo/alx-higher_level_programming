Python - Input/Output
0. file = 0-read_file.py
Prototype: def read_file(filename=""):
This is a function that reads a text file (UTF8) and prints it to stdout

1. file = 1-write_file.py
Prototype: def write_file(filename="", text=""):
This is a function that writes a string to a text file (UTF8) and returns the number of characters written

2. file =2-append_write.py
Prototype: def append_write(filename="", text=""):
This is a function that appends a string at the end of a text file (UTF8) and returns the number of characters added

3. file = 2-append_write.py
Prototype: def append_write(filename="", text=""):
This is a function that returns the JSON representation of an object (string)

4. file = 4-from_json_string.py
Prototype: def from_json_string(my_str):
This is a function that returns an object (Python data structure) represented by a JSON string

5. file = 5-save_to_json_file.py
Prototype: def save_to_json_file(my_obj, filename):
This is a function that writes an Object to a text file, using a JSON representation

6. file = 6-load_from_json_file.py
Prototype: def load_from_json_file(filename):
This is a function that creates an Object from a “JSON file”

7. file = 7-add_item.py
This is a script that adds all arguments to a Python list, and then save them to a file:
You must use your function save_to_json_file from 5-save_to_json_file.py
You must use your function load_from_json_file from 6-load_from_json_file.py
The list must be saved as a JSON representation in a file named add_item.json
If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.

8. file = 8-class_to_json.py
Prototype: def class_to_json(obj):
A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object
obj is an instance of a Class
All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
You are not allowed to import any module

9. file = 9-student.py
A class Student that defines a student by:

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
You are not allowed to import any module

10. file = 10-student.py
A class Student that defines a student by: (based on 9-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attribute names contained in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

11. file = 11-student.py
A class Student that defines a student by: (based on 10-student.py)

Public instance attributes:
first_name
last_name
age
Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
You can assume json will always be a dictionary
A dictionary key will be the public attribute name
A dictionary value will be the value of the public attribute
You are not allowed to import any module
Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

12. file = 12-pascal_triangle.py
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module

13. file = 100-append_after.py
Prototype: def append_after(filename="", search_string="", new_string=""):
A function that inserts a line of text to a file, after each line containing a specific string (see example)
You must use the with statement
You don’t need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module

14. file = 101-stats.py
A script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
