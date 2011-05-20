#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       zadatak8.py
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

def zadatak8(x, y, z, q):
	e1 = y - x
	e2 = z - x
	n = cross(e1, e2)
	d = dot(n, x)
	a = dot(e1, e1)
	b = dot(e1, e2)
	c = dot(e2, e2)
	D = a * c - pow(b, 2)
	A = a / D
	B = b / D
	C = c / D
	ubeta = C*e1 - B*e2
	ugama = A*e2 - B*e1
	
	r = q - x
	beta = dot(ubeta, r)
	gama = dot(ugama, r)
	alpha = 1 - beta - gama
	return (alpha, beta, gama)

def main():
	#x = array(input("Unesi točku x: "))
	#y = array(input("Unesi točku y: "))
	#z = array(input("Unesi točku z: "))
	#q = array(input("Unesi točku q: "))
	x = array([2,-1,3])
	y = array([3,2,1])
	z = array([0,3,-2])
	q = array([1.92307692,-0.46153846,2.46153846])
	
	rez = zadatak8(x, y, z, q)
	if rez is not None:
		print "Baricentrične koordinate su: ", rez[0], ",", rez[1], ",", rez[2]
	return 0

if __name__ == '__main__':
	main()

