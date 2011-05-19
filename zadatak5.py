#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       zadatak5.py
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

def zadatak5(p, u, c, r):
	v = dot(c-p, u)
	disc = pow(r, 2) - (dot(c-p, c-p) - pow(v, 2))
	if (disc < 0):
		return
	else:
		d = sqrt(disc)
		P1 = p + (v-d)*u
		P2 = p + (v+d)*u
		return (P1, P2)

def main():
	p = array(input("Unesi početnu točku p: "))
	u = array(input("Unesi vektor smjera u: "))
	c = array(input("Unesi centar sfere c: "))
	r = input("Unesi radius sfere r: ")
	#c = array([2,-1,3])
	#p = array([-1,3,1])
	#u = array([2,-4,1])
	#r = 2
	rez = zadatak5(p, u, c, r)
	if rez is not None:
		print "Zraka siječe sferu u točkama\n", rez[0], "\n", rez[1]
	else:
		print "Zraka ne siječe sferu!"
	
	return

if __name__ == "__main__":
	main()
