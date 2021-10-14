# import os

# print('getcwd:      ', os.getcwd())
# print('__file__:    ', __file__)
# print('basename:    ', os.path.basename(__file__))
# print('dirname:     ', os.path.dirname(__file__))
# print('abspath:     ', os.path.abspath(__file__))
# print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))
# print('[change directory]')
# os.chdir(os.path.dirname(os.path.abspath("monk.cpp")))
# print('getcwd:      ', os.getcwd())
# pythonfile = 'monk.cpp'
  
# # if the file is present in current directory,
# # then no need to specify the whole location
# print("Path of the file..", os.path.abspath(pythonfile))
  
# for root, dirs, files in os.walk(r'D:'):
#     for name in files:
        
#           # As we need to get the provided python file, 
#         # comparing here like this
#         if name == pythonfile:  
#             print(os.path.abspath(os.path.join(root, name)))
import os
os.system('color')

# Python program to print
# colored text and background
import sys
from termcolor import colored, cprint
 
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')
 
print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')
 
for i in range(10):
    cprint(i, 'magenta', end=' ')
 
cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)
input()