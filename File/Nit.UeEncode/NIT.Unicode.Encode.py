# -*- coding: cp1251 -*-
from __future__ import unicode_literals

# Преобразование файла в строку Unicode

import os
import errno
import shutil
import platform
import win32api
import sys
import locale


# None Hidden Variables
read_file = "NIT.Unicode.Encode"
read_lines = []
read_ext = "py"
write_ext = "txt"

# Temprorary Variables
currentdir = os.getcwd()

# Function for read files with Credentials
def readFile_Cred( file_name, ext ):
	global read_lines
	global currentdir
	iread_line = 0
	full_file_name = currentdir + "\\" + file_name + "." + ext
	print currentdir, full_file_name
	if not os.path.exists(full_file_name):
		print "File Not Found: " + full_file_name
		del read_lines[:]
		return 0
	with open( full_file_name, "rb" ) as file:
		file_lines = file.readlines()
		iread_line = len(file_lines)
		if iread_line == 0:
			print "Wrong iread_line"
			return 0
		else:
			print "Lines = " + str(iread_line)
			for i in xrange(1,iread_line):
				read_lines.append(file_lines[i])
	return iread_line


# Function for Write files with Credential
def writeFile_Cred_uni( file_name, ext ):
	global read_lines
	global currentdir
	full_file_name = currentdir + "\\" + file_name + "." + ext
	print currentdir, full_file_name
	#if os.path.exists(full_file_name):
	#	os.remove(full_file_name)
	iread_line = len(read_lines)
	if iread_line == 0:
		return False
	try:
		file = open( full_file_name, "wb+" )
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			print exception
			return False
	for i in xrange(1,iread_line):
		read_line = read_lines[i]
		write_line = read_line.decode("cp1251")
		file.writeline( write_line )
	file.close()
	del read_lines[:]
	return True


if __name__ == '__main__':
	print "locale: "+locale.getpreferredencoding(False)
	iread = readFile_Cred( read_file, read_ext)
	if not iread == 0:
		print "True"
		if readFile_Cred( read_file, write_ext):
			print "True"
			print "file:\n"+read_line
		else:
			print "False"
	else:
		print "False"
