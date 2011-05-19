#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       zadatak3.py
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

def zadatak3(n, s, i_loma):
	#tlat = true_divide((((dot(s, n)) * n) - s), i_loma)
	tlat = (((dot(s, n)) * n) - s) / i_loma
	tprep = sqrt(1 - (pow(i_loma, -2) * (1 - pow(dot(s, n),2)))) * n
	t = tlat - tprep
	return t

def main():
	n = array(input("Unesi normalu n: "))
	s = array(input("Unesi vektor smjera s: "))
	i_loma = input("Unesi index loma η: ")
	print zadatak3(n, s, i_loma)
	
	return

if __name__ == "__main__":
	main()
