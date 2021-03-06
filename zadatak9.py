#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       zadatak9.py
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
from zadatak7 import zadatak7
from zadatak8 import zadatak8

def zadatak9(p, u, v0, v1, v2):
	e1 = v1 - v0
	e2 = v2 - v0
	n = cross(e1, e2)
	d = dot(n, v0)
	
	q = zadatak7(p, u, n, d)
	if q is None:
		return
	else:
		alpha, beta, gama = zadatak8(v0, v1, v2, q)
		
		if (beta < 0) or (gama < 0) or (alpha < 0):
			return
		return q

def main():
	#p = array(input("Unesi početnu točku p: "))
	#u = array(input("Unesi vektor smjera u: "))
	#v0 = array(input("Unesi točku v0: "))
	#v1 = array(input("Unesi točku v1: "))
	#v2 = array(input("Unesi točku v2: "))
	p = array([1,0,2])
	u = array([2,-1,1])
	v0 = array([2,-1,3])
	v1 = array([3,2,1])
	v2 = array([0,3,-2])
	
	rez = zadatak9(p, u, v0, v1, v2)
	if rez is not None:
		print "Zraka siječe trokut u točki q=", rez
	else:
		print "Zraka ne siječe trokut!"
	
	return

if __name__ == '__main__':
	main()
