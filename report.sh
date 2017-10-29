#!/bin/bash

echo "Time for DFT (array of length 5000):"
time ./DFT.py
echo "Time for DFT with matrix multiplication (array of length 5000):"
time ./DFT_matrix.py
echo "Time for FFT (array only of length 50 !):"
time ./FFT.py


