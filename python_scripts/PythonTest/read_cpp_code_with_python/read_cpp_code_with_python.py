#!/usr/bin/python
#coding=utf-8

import ctypes

SO_PATH = './libErrorCode.so'
ll = ctypes.cdll.LoadLibrary 
lib = ll(SO_PATH)  
result = lib.get_error_code()

print result
print type(result)
