
import time
import sys

print sys.argv

if len(sys.argv) > 1:
    t = time.ctime(float(sys.argv[1]))
else:
    t = time.ctime()


print t

