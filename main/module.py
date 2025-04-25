# two types of modules in python
# 1. Built-in modules
# 2. User-defined modules

import math  # Importing the built-in math module
print(math.sqrt(16))  # This will print 4.0

import os
print(os.getcwd())  # This will print the current working directory



# creating our own modeule
# 1. Create a file named my_module.py in the same directory as this file
import my_module  # Importing the user-defined module
my_module.hello()  # This will call the hello function from my_module.py

# import requests
# r= requests.get("https://www.google.com") 
# print(r.text)  # This will print the response from the Google homepage