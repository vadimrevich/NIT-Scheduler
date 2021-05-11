# -*- coding: cp866 -*-
from __future__ import unicode_literals

# Преобразование файла в строку Unicode

import os
import errno
import shutil
import platform
import win32api
import sys
import locale
import six

from io import open


# None Hidden Variables
read_file = "asdf"
text_lines = []
read_ext = "txt"
write_ext = "1.txt"

# Temprorary Variables
currentdir = os.getcwd()

# Function for read files with Credentials
def readFile_Cred( file_name, ext, read_lines ):
	global currentdir
	iread_line = 0
	full_file_name = currentdir + "\\" + file_name + "." + ext
	print full_file_name
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
			print "Lines = " + str(iread_line)
			for i in xrange(0,iread_line):
				read_lines.append(file_lines[i])
				#print read_lines[i]
	return iread_line


# Function for Write files with Credential
def writeFile_Cred( file_name, ext, read_lines ):
	global currentdir
	full_file_name = currentdir + "\\" + file_name + "." + ext
	print full_file_name
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
		write_line = read_lines[i]
		file.write( write_line )
	file.close()
	del read_lines[:]
	return True


if __name__ == '__main__':
	print "locale: "+locale.getpreferredencoding(False)
	iread = readFile_Cred( read_file, read_ext, text_lines)
	if not iread == 0:
		print "True"
		if writeFile_Cred( read_file, write_ext, text_lines):
			print "True"
		else:
			print "False"
	else:
		print "False"
