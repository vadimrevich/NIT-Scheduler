# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import os
import errno
import base64
import socket
import shutil
import platform
import win32api
import re
import sys
import locale
import six

from io import open

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


# Path options
pathPubDistr = "c:\\pub1\\Util"		# Path to Executable Files and Settings

# directories_and_files names

# Credential data
myLogin = ""
myPassword = ""

# None Hidden Variables
settings_file = "settings-reverse.ini"
myOldPassword = "Password01234"
myOldLogin = "MSSQLSR"
text_lines = []

# Temprorary Variables

# Derivative Variables
settings_fname = "c:\\pub1\\Util" + "\\" + settings_file
try:
	currenthost = socket.gethostname()
except:
	pass

# Function is Decode Config File Data
def globalDecoder():
# Credential data
	global myLogin
	global myPassword
# pathLogs options
	global pathPubDistr
# Credential data
	myLogin = base64.b64decode( myLogin )
	myPassword = base64.b64decode( myPassword )
# Path options
	pathPubDistr = base64.b64decode(pathPubDistr)
# directories_and_files names


# Function to Read Config File
def globalReadConfig( filepath ):
# Credential data
	global myLogin
	global myPassword
# Path options
	global pathPubDistr
	config =  configparser.ConfigParser()
	if not os.path.exists( filepath ):
		return False
	config = configparser.ConfigParser()
	try:
		config.read( filepath )
	except Exception as e:
		print e
		return False
	# Credential data
	myLogin = config.get("Credentials","myLogin")
	myPassword = config.get("Credentials","myPassword")
	# Paths Section
	pathPubDistr = config.get("Paths","Install")
	return True


# Function for read files with Credentials
def readFile_Cred( file_name, ext, read_lines ):
	iread_line = 0
	full_file_name = pathPubDistr + "\\" + file_name + "." + ext
	#print full_file_name
	if not os.path.exists(full_file_name):
		print "File Not Found: " + full_file_name
		del read_lines[:]
		return 0
	with open( full_file_name, mode="r", encoding="cp866" ) as file:
		file_lines = file.readlines()
		iread_line = len(file_lines)
		if iread_line == 0:
			print "The File is Empty"
			del read_lines[:]
			return 0
		else:
			#print "Lines = " + str(iread_line)
			for i in xrange(0,iread_line):
				read_lines.append(file_lines[i])
				#print read_lines[i]
	return iread_line


# Function for Write files with Credential
def writeFile_Cred_Uni( file_name, ext, read_lines ):
	full_file_name = pathPubDistr + "\\" + file_name + "." + ext
	#print full_file_name
	if os.path.exists(full_file_name):
		os.remove(full_file_name)
	iread_line = len(read_lines)
	if iread_line == 0:
		return False
	try:
		file = open( full_file_name, mode="w+", encoding="UTF-16" )
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			print exception
			return False
	for i in xrange(0,iread_line):
		write_line = fnReplaceStr(read_lines[i])
		file.write( write_line )
	file.close()
	del read_lines[:]
	return True


# Function for Write files with Credential
def writeFile_Cred( file_name, ext, read_lines ):
	full_file_name = pathPubDistr + "\\" + file_name + "." + ext
	#print full_file_name
	if os.path.exists(full_file_name):
		os.remove(full_file_name)
	iread_line = len(read_lines)
	if iread_line == 0:
		return False
	try:
		file = open( full_file_name, mode="w+", encoding="cp866" )
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			print exception
			return False
	for i in xrange(0,iread_line):
		write_line = fnReplaceStr(read_lines[i])
		file.write( write_line )
	file.close()
	del read_lines[:]
	return True


# Function for Search and Replasew Strings
def fnReplace(pattern,repl,string):
	#re.IGNORECASE
	return re.sub(pattern, repl, string, count = 0)


def fnReplaceStr(string):
	global myOldLogin
	global myPassword
	global myNewLogin
	global myOldPassword
	string0 = fnReplace(myOldLogin, myNewLogin, string)
	return fnReplace(myOldPassword, myPassword, string0)


if __name__ == '__main__':
	if globalReadConfig( settings_fname ):
		#pass
		globalDecoder()
	myNewLogin = currenthost + "\\" + myLogin
	iread = readFile_Cred( "Register_Schedule_Reverse", "ba_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred( "Register_Schedule_Reverse", "bat", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Daily", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Daily", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Half", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Half", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Hourly", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Hourly", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Kwint", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Kwint", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Mounthly", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Mounthly", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Quart", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Quart", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Weekly", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Weekly", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
	iread = readFile_Cred( "Task_Write", "xm_", text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred_Uni( "Task_Write", "xml", text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"


