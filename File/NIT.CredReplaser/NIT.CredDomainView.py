#!py -2.7-64
import os
import win32api

domain = os.environ['userdomain']
user = "MSSQLSR"
current_user = win32api.GetUserNameEx(win32api.NameSamCompatible)
print "\ncurrent user = "+current_user+"; user = "+domain+"\\"+user+";\n"
