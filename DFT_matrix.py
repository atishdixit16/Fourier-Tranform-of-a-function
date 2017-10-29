#!/usr/bin/python

import sys
import cmath as m
import numpy as np

f = range(5000)

def DFT_matrix(f) :
	N = len(f)
	DFT_matrix = CreateDFTmatrix(N)
	f = np.matrix(f)
	f = f.transpose()
	return DFT_matrix*f

def CreateDFTmatrix(N) :
	matrix = [[0+0j]*N]*N
	matrix = np.matrix(matrix)
	complexNum = 0 - 1j
        omegaN = m.exp(complexNum * (  (2*m.pi) / N )  )
	for i in range(N) :
		for j in range(N) :
			matrix[i,j] = omegaN**(i*j)
	return matrix

F = DFT_matrix(f)
