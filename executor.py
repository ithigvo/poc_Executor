#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Gustavo Veríssimo'

import base64
import cx_Oracle

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

print user
print passwd
print banco



