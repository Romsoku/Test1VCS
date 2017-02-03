#! Insert the current directory path to Python Path
import sys
import os
cwd = os.getcwd() # Current Working Directory

sys.path.append(cwd)
# print (sys.path)

# Test the module: generate_list
from generate_list import printIt
printIt()