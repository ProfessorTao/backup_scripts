
import time
import sys

print sys.argv

# t = time.gmtime()
# time_struct = time.struct_time(t)
# time.struct_time(tm_year=2013, tm_mon=6, tm_mday=8, tm_hour=7, tm_min=16, tm_sec=33, tm_wday=5, tm_yday=159, tm_isdst=0)

if len(sys.argv) >= 7 :
    #year = int(sys.argv[1])
    #month = int(sys.argv[2])
    #day = int(sys.argv[3])
    #hour = int(sys.argv[4])
    #minute = int(sys.argv[5])
    #second = int(sys.argv[6])

    #time_struct.tm_year = year
    #time_struct.tm_mon = month
    #time_struct.tm_mday = day
    #time_struct.tm_hour = hour
    #time_struct.tm_min = minute
    #time_struct.tm_sec = second
    
    strTime = '%s-%s-%s %s:%s:%s' % (sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    time_struct = time.strptime(strTime, '%Y-%m-%d %X')

    print time_struct

    t = time.mktime(time_struct)
    print t

