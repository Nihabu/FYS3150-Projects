# -*- coding: utf-8 -*-
"""
FYS3150
Warmup Exercise
Created on Fri Aug 26 11:42:25 2016

@author: henrikbjonerlie
"""
from numpy import *
import matplotlib.pyplot as plt

#Compute first derivative for decreasing steplengths

steplength = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14, 1e-15, 1e-16]
f2c = zeros(len(steplength))
f3c = zeros(len(steplength))

f_exact = 1./3

def f(x):
    return arctan(x)

for i in range(len(steplength)):
    x = sqrt(2)
    x_plus = x + steplength[i]
    x_minus = x - steplength[i]
    
    f2c[i] = (f(x_plus) - f(x))/steplength[i]               #2point-formula
    f3c[i] = (f(x_plus) - f(x_minus))/(2*steplength[i])     #3point-formula

#Compute log of relative error

error2 = zeros(len(f2c))
error3 = zeros(len(f3c))

for i in range(len(error2)):
    error2[i] = abs((f2c[i]-f_exact)/f_exact)
    error3[i] = abs((f3c[i]-f_exact)/f_exact)
    
er2 = log10(error2)
er3 = log10(error3)
lgsl = log10(steplength)

#Plot errors for comparison

plt.plot(lgsl, er2, label='Error2P')
plt.plot(lgsl, er3, label='Error3P')
plt.legend(loc=('lowerleft'))
plt.show()

#Write derivative-results to file

f = open('WarmupExercise', 'w')

f.write('2P-formula            3P-formula               Exact\n')
f.write('                                                1/3\n')
for i in xrange(len(f2c)):
    f.write('%-18s %s\n' %(str(f2c[i]), str(f3c[i])))
f.close()