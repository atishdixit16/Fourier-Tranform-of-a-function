# Fourier-Tranform-of-a-function
python codes written to execute discrete and fast fourier transforms(DFT and FFT)

Execution was done using a shell script. comparison on the basis of computational time was done.

Following is the out put of report.sh shell script:

Time for DFT (array of length 5000):

real	0m14.041s
user	0m14.040s
sys	0m0.004s
Time for DFT with matrix multiplication (array of length 5000):

real	0m10.835s
user	0m10.796s
sys	0m0.040s
Time for FFT (array only of length 50 !):

real	0m10.873s
user	0m10.860s
sys	0m0.012s


To my surprise, Time taken by FFT is way too much if compared with DFT and SDT with matrix multiplication execution.
