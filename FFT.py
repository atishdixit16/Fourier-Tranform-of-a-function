#!/usr/bin/python

import sys
import cmath as m

f = range(4096)

def FFT(f) :
	N = len(f)
	if (N == 1) :
		return f
	F = [0]*N
	M = N/2
	f_odd = f[1::2]
	f_even = f[::2]
	F_even = FFT(f_even)
	F_odd = FFT(f_odd)
	complexNum = 0 - 1j
	omega = m.exp(complexNum * (  (2*m.pi) / N )  )
	for i in range(M) :
		F[i] = F_even[i] + (omega**i)*F_odd[i]
		F[i+M] = F_even[i] - (omega**i)*F_odd[i]
	return F

F = FFT(f)
print F
