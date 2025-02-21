# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:16:02 2021

@author: hk3rr
"""
import matplotlib.pyplot as plt
import numpy as np
import math
''''''
k = 1*10**6
m = 200
x = np.arange(0,10,0.01)
''''''
def func(k,m,t,x):
    Fpeak = (1000+(9*(x**2))-183*x)*10**3
    td = (20-(0.12*(x**2))+4.2*x)/10**3
    w = (k/m)**0.5
    if t <= td:
        return (( Fpeak / k ) * ( 1-math.cos( w * t ))) + (( Fpeak / ( k * td )) * ((( math.sin( w * t )) / w) - t ))
    else:      
        return (( Fpeak / ( k * w * td)) * ( math.sin( w * t ) - math.sin( w * ( t - td )))) - (( Fpeak / k ) * math.cos( w * t ))    
vfunc = np.vectorize(func)

t = np.linspace(0,2*(2*np.pi)/((k/m)**0.5),101)
zeemaxes = []
for i in x:
    zeemaxes.append(max(vfunc(k,m,t,i)))

plt.plot(x,zeemaxes)
plt.xlabel("x (m)")
plt.ylabel("Max z (m)")
plt.grid()
