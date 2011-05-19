#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       zadatak7.py
#       
#       Copyright 2011 David Jelic <djelic@buksna.net>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from __future__ import division
from math import sqrt, pow
from numpy import *

def zadatak7(p, u, n, d):
	c = dot(u, n)
	if (c == 0):
		return
	else:
		alpha = (d - dot(p, n)) / c
		if (alpha < 0): return
		else:
			q = p + (alpha * u)
			return q

def main():
	p = array(input("Unesi početnu točku p: "))
	u = array(input("Unesi vektor smjera u: "))
	n = array(input("Unesi normalu n: "))
	d = input("Unesi d: ")
	
	rez = zadatak7(p, u, n, d)
	if rez is not None:
		print "Zraka siječe ravninu u točki\n", rez
	else:
		print "Zraka ne siječe ravninu!"
	
	return

if __name__ == "__main__":
	main()
