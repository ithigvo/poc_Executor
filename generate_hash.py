#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Gustavo Veríssimo'

import base64
import sys
import getopt

qtd=6
username=''
password=''
database=''
filename=''

opts, args = getopt.getopt(sys.argv[1:],"u:p:d:q:f:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in opts:
	if o == '-u':
		username=a
	elif o == '-p':
		password=a
	elif o == '-d':
		database=a
	elif o == '-q':
		qtd=a
	elif o == '-f':
		filename=a		
	else:
		print("Usage: %s -u username -p password -d database -f filehash [-q qtd] " % sys.argv[0])

for x in xrange(0,int(qtd)):
	username = base64.b64encode(username)
	password = base64.b64encode(password)
	database = base64.b64encode(database)

qtd = base64.b64encode(qtd)

file = open(filename, 'w')
file.truncate()
file.write(qtd+'\n'+username+'\n'+password+'\n'+database+'\n')
file.close()

print ("%s \n%s \n%s \n%s " % (qtd,username,password,database) )