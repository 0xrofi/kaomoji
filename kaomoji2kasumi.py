#!/usr/bin/env python
# -*- coding: utf-8 -*-
# kaomoji2kasumi -- Converts 0xrofi's kaomoji format to kasumi dict's format.

# Copyright(c) Terminus-IMRC (also known as mswinvks)
# Mail: i.can.speak.c.and.basic@gmail.com

while True:
	try:
		s=raw_input()
	except EOFError:
		break

	s=s.split()

	#Remove @ prefix #There must be other good way...
	s[0]=s[0].replace("@", "")
	s[0]=s[0].replace("＠", "")

	#There must be other good way...
	print s[0], "T35*500",
	for f in s[1:len(s)-1]:
		print f,
	print
