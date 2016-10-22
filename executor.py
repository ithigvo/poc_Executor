#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Gustavo Veríssimo'

import base64
import cx_Oracle
import sys
import getopt
from subprocess import Popen,PIPE

with open('executor.hash') as f:
	content = f.readlines()

i = base64.b64decode(content[0])
user = content[1]
passwd = content[2]
banco  = content[3]

for x in xrange(0,int(i)):
  user = base64.b64decode(user)
  passwd = base64.b64decode(passwd)
  banco = base64.b64decode(banco)



opts, args = getopt.getopt(sys.argv[1:],"u:d:")

###############################
# o == option
# a == argument passed to the o
###############################
for o, a in opts:
	if o == '-u':
		dbuser=a
	elif o == '-d':
		dbname=a
	else:
		print("Usage: %s -u username -p password -d database -f filehash [-q qtd] " % sys.argv[0])

dbpasswd = ''

db = cx_Oracle.connect(user+'/'+passwd+'@'+banco)
qry = db.cursor()
binds = {'dbname':dbname, 'dbuser':dbuser}
qry.execute('select username, password from mag_v_cad_dbusers where nome = :dbname and username = :dbuser', binds)

( dbuser, dbpasswd ) = qry.fetchone()

db.close()

print dbname
print dbuser
print dbpasswd

dbstring = dbuser+'/'+dbpasswd+'@'+dbname
print dbstring

sqlp = Popen(["sqlplus", dbstring], stdin=PIPE, stdout=PIPE, stderr=PIPE)
sqlp.stdin.write("spool teste_vollo.log\n")
sqlp.stdin.write("select user, sysdate from dual;\n")
sqlp.stdin.write("spool off\n")

stdout, stderr = sqlp.communicate()
print stdout
print stderr

#Git não funciona
