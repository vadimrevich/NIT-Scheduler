# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import os
import errno
import socket
import base64
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
myLogin = "MSSQLSR"
myPassword = "Admin01234"

# None Hidden Variables
settings_file = "settings-reverse.ini"
settings_fname = "c:\\pub1\\Util" + "\\" + settings_file

# None Hidden Variables

string1 = "This is a string"
string2 = "This is MSSQLSR a Password01234 string password"
string3 = "This is MSSQLSR a mssqlsr Password01234 MSSQLSR string Password01234 password01234 "

# Derivative Variables
settings_fname = pathPubDistr + "\\" + settings_file

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
	myOldPassword = "Password01234"
	myOldLogin = "MSSQLSR"
	print "\n" + string1 + "\n" + fnReplaceStr( string1 )
	print "\n" + string2 + "\n" + fnReplaceStr( string2 )
	print "\n" + string3 + "\n" + fnReplaceStr( string3 )
