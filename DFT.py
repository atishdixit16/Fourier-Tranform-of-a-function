#!/usr/bin/python

import sys
import cmath as m

f = range(5000)

# Discrete Fourier Transform
def DFT(f) :
	N = len(f)
	F = [0]*N
	for i in range(N) :
		for j in range(N) :
			complexNum = 0 - 1j
			term2 = m.exp(complexNum * (  (2*m.pi*i*j) / N )  )
			F[i] = F[i] + ( f[j]* term2 )
	return F

F = DFT(f)

# Inverse Discrete Fourier Transform
def IDFT(F) :
	N = len(F)
	f = [0]*N
	for i in range(N) :
		for j in range(N) :
			complexNum = 0 + 1j
			term2 = m.exp(complexNum * (  (2*m.pi*i*j) / N )  )
			f[i] = f[i] + ( F[j]* term2 )
		f[i] = f[i]/N
	return f

#f = IDFT(F)
#print f

# Convolution: DFT

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

def DFTconvolution(x,y) :
	N = len(x)
	conv = [0]*N
	for k in range(N) :
		for m in range(N) :
			conv[k] = conv[k] + x[m] * y[k-m]
	return conv

#x_y = DFTconvolution(x,y)
#print x_y
