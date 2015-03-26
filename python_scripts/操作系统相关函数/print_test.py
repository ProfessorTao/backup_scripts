
import sys

print("from print")

print_1 = sys.stdout.write
print_2 = sys.stderr.write

print_1("from sys.stdout.write\n")
print_2("from sys.stderr.write\n")


