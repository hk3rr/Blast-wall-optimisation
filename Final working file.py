# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:19:04 2021

@author: hk3rr
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import time
start_time = time.time()
''''''
mstep = 50
kstep = 500000
tolerance = 1 / 10**3
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

Ctotal = []
emms = []
kays = []
exes = []
for m in range(200,mstep+1200,mstep):
    for k in range(1000000,kstep+7000000,kstep):
        t = np.linspace(0,(4*np.pi)/((k/m)**0.5),101)
        xs = 0
        xl = 10
        xm = (xs+xl)/2
        z = vfunc(k,m,t,xm)
        while max(z) > 0.1 or 0.1 - max(z) > tolerance:
            if max(z) >= 0.1:
                xs = xm
            else:
                xl = xm
            xm = (xs+xl)/2
            z = vfunc(k,m,t,xm)
        Ctotal.append( 900 + 825 * ( (k/10**6)**2 ) - 1725 * (k/10**6) + 10 * m - 2000 + 2400 * ( ( xm**2 ) / 4) )
        emms.append(m)
        kays.append(k)
        exes.append(xm)
        
# Hard part's over, now to get opimal values and graph
index = Ctotal.index(min(Ctotal))
m = emms[index]
k = kays[index]
xm = exes[index]
print('')
print("Minimum cost of the wall without failing = £",min(Ctotal))
print("Mass which gives minimum cost =",m,'kg')
print("Stiffness which gives minimum cost =",k,'Nm')
print("Distance which gives minimum cost =",xm,'m')
print("Greatest displacement experienced by wall under these conditions =",max(abs(z))*1000,'mm')

print("--- %s seconds ---" % (time.time() - start_time))

plt.plot(t,z,label='Displacement')
plt.plot(t,abs(z),label='Absolute displacement')
plt.grid()
plt.legend(loc="lower left")
plt.ylabel('Displacement of wall (m)')
plt.xlabel('Time after blast (s)')

fig = plt.figure(1)
plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.scatter(kays, emms, Ctotal)
ax.invert_xaxis()
ax.set_xlabel('Stiffness of wall (MN/m)')
ax.set_ylabel('Mass of wall (kg)')
ax.set_zlabel('Cost of wall (£)')
ax.yaxis.labelpad = 10
ax.zaxis.labelpad = 15
ax.view_init(30, 80)

fig = plt.figure(2)
plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.scatter(kays, emms, Ctotal)
ax.invert_xaxis()
ax.set_xlabel('Stiffness of wall (MN/m)')
ax.set_ylabel('Mass of wall (kg)')
ax.set_zlabel('Cost of wall (£)')
ax.zaxis.labelpad = 10
ax.view_init(30, 100)

fig = plt.figure(3)
plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.scatter(kays, emms, Ctotal)
ax.invert_xaxis()
ax.set_ylabel('Mass of wall (kg)')
plt.xticks([])
ax.set_zlabel('Cost of wall (£)')
ax.yaxis.labelpad = 10
ax.zaxis.labelpad = 10
ax.view_init(0, 0)

fig = plt.figure(4)
plt.figure(figsize=(10, 10))
ax = plt.axes(projection='3d')
ax.scatter(kays, emms, Ctotal)
ax.invert_xaxis()
ax.set_xlabel('Stiffness of wall (MN/m)')
plt.yticks([])
ax.set_zlabel('Cost of wall (£)')
ax.xaxis.labelpad = 10
ax.zaxis.labelpad = 15
ax.view_init(0, 90)
