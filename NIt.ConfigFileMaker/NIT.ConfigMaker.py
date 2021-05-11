# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#******************************************************************************
#
# NIT.ConfigMaker.py
# This File Makes INI-file with Settings for NIT.Zlovred
#
#******************************************************************************

import os
import errno
import base64
import shutil
import platform
import win32api

try:
    import configparser
except ImportError:
    import ConfigParser as configparser


# FTP options
ftpip = "127.0.0.1"	# IP to connect to FTP server
ftpport = 21		# Port to connect to FTP Server
ftpkey = ""		# FTP password
ftpuser = "anonymous"	# FTP User
ftp_root_dir = "/"	# An ftp Root Directory with Files

# Path options
pathPubDistr = "c:\\pub1\\Util"		# Path to Executable Files and Settings
pathLogs = "C:\\Users\\Public\\Intel\\Logs"		# Path to Worked Files

# directories_and_files names

# Credential data
myLogin = "MSSQLSR"
myPassword = "Admin01234"

# None Hidden Variables
settings_file = "settings-reverse.ini"
settings_fname = "c:\\pub1\\Util" + "\\" + settings_file

# Temprorary Variables

s_ftpport = "21"

# Derivative Variables
settings_fname = pathPubDistr + "\\" + settings_file

# Test
print myLogin," ",pathLogs," ",myPassword


# Functiom for Encoding Global Variables
def globalEncoder():
# Credential data
	global myLogin
	global myPassword
# Path options
	global pathLogs
	global pathPubDistr
# directories_and_files names
# FTP options
	global ftpuser
	global ftpkey
	global ftpport
	global ftpip
	global ftp_root_dir
	global s_ftpport
	global ssmtpPort
# Credential data
	myLogin = base64.b64encode( myLogin )
	myPassword = base64.b64encode( myPassword )
# Path options
	pathLogs = base64.b64encode(pathLogs)
	pathPubDistr = base64.b64encode(pathPubDistr)
# directories_and_files names
# FTP options
	s_ftpport = str(ftpport)
	ftpuser = base64.b64encode(ftpuser)
	ftpkey = base64.b64encode(ftpkey)
	s_ftpport = base64.b64encode(s_ftpport)
	ftpip = base64.b64encode(ftpip)
	ftp_root_dir = base64.b64encode(ftp_root_dir)
	#Test
	print myLogin," ",pathLogs," ",myPassword


# Function is Decode Config File Data
def globalDecoder():
# Credential data
	global myLogin
	global myPassword
# pathLogs options
	global pathLogs
	global pathPubDistr
# directories_and_files names
# FTP options
	global ftpuser
	global ftpkey
	global ftpport
	global ftpip
	global ftp_root_dir
	global s_ftpport
	global ssmtpPort
# Credential data
	myLogin = base64.b64decode( myLogin )
	myPassword = base64.b64decode( myPassword )
# Path options
	pathLogs = base64.b64decode(pathLogs)
	pathPubDistr = base64.b64decode(pathPubDistr)
# directories_and_files names
# FTP options
	ftpuser = base64.b64decode(ftpuser)
	ftpkey = base64.b64decode(ftpkey)
	s_ftpport = base64.b64decode(s_ftpport)
	ftpip = base64.b64decode(ftpip)
	ftp_root_dir = base64.b64decode(ftp_root_dir)
	try:
		ftpport = int(s_ftpport)
	except Exception as e:
		ftpport = 21
	#Test
	print myLogin," ",pathLogs," ",myPassword


# Function to Create Config File
def createConfig( filepath ):
# Credential data
	global myLogin
	global myPassword
# Path options
	global pathLogs
	global pathPubDistr
# directories_and_files names
# FTP options
	global ftpuser
	global ftpkey
	global ftpport
	global ftpip
	global ftp_root_dir
	global s_ftpport
	global ssmtpPort
	config =  configparser.ConfigParser()
	# Credential data
	config.add_section("Credentials")
	config.set("Credentials","myLogin", myLogin)
	config.set("Credentials","myPassword", myPassword)
	# directories_and_files names
	config.add_section("directories_and_files")
	# Path options
	config.add_section("Paths")
	config.set("Paths","main", pathLogs)
	config.set("Paths","Install", pathPubDistr)
	# FTP options
	config.add_section("FTP")
	config.set("FTP","Server", ftpip)
	config.set("FTP","Port", s_ftpport)
	config.set("FTP","User", ftpuser)
	config.set("FTP","Pass", ftpkey)
	config.set("FTP","Root", ftp_root_dir)
	with open(filepath, "wb") as config_file:
		config.write(config_file)
		config_file.close()


# Function to Read Config File
def globalReadConfig( filepath ):
# Credential data
	global myLogin
	global myPassword
# Path options
	global pathLogs
	global pathPubDistr
# directories_and_files names
# FTP options
	global ftpuser
	global ftpkey
	global ftpport
	global ftpip
	global ftp_root_dir
	global s_ftpport
	global ssmtpPort
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
	pathLogs = config.get("Paths","main")
	pathPubDistr = config.get("Paths","Install")
	# Directories and Files Section
	# FTP Section
	ftpip = config.get("FTP","Server")
	s_ftpport = config.get("FTP","Port")
	ftpuser = config.get("FTP","User")
	ftpkey = config.get("FTP","Pass")
	ftp_root_dir = config.get("FTP","Root")
	#Test
	print myLogin," ",pathLogs," ",myPassword
	return True


if __name__ == '__main__':
	globalEncoder()
	createConfig( settings_fname )
	if globalReadConfig( settings_fname ):
		#pass
		globalDecoder()

