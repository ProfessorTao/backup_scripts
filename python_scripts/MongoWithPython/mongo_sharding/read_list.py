
import sys

file_name = sys.argv[1]

fp = open(file_name, 'r')

str_output = ""
for line in fp:
    str_output += line.replace("\n", ",") 

if "," == str_output[-1]:
    str_output = str_output[0:-1]

print str_output
