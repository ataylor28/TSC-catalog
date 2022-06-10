import tableauserverclient as TSC
import os
import requests
from read import read_func
from edit import edit_func

# name functions
read = read_func()
edit = edit_func()

# define list of available functions
def list_functions(x):
    x_list = [method for method in dir(x) if method.startswith('_') is False]
    str_x = str('read' if x==read else 'edit')
    print("\nThere are {} functions within the ".format(len(x_list))+str_x+" class.")
    print(*x_list, sep = '\n')

# print list of available functions
list_functions(edit)
list_functions(read)

# call functions using class.func()
# ex: read.datasource()

print('\n')
read.groups()
