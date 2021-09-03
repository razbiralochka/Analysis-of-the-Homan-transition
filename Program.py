import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


OrbitData=np.genfromtxt('Mars-Sun_tb.txt')

SSCData=np.genfromtxt('SC-Sun_tb.txt')

MSCData=np.genfromtxt('SC-Mars_tb.txt')



SMX=OrbitData[:,0]
SMY=OrbitData[:,1]
SMZ=OrbitData[:,2]

SSCX=SSCData[:,0]
SSCY=SSCData[:,1]
SSCZ=SSCData[:,2]



SSCDataTeor=OrbitData+MSCData



MSCX=SSCDataTeor[:,0]
MSCY=SSCDataTeor[:,1]
MSCZ=SSCDataTeor[:,2]


u, v = np.mgrid[0:2*np.pi:200j, 0:np.pi:100j]
x = np.cos(u)*np.sin(v)*15*pow(10,6)
y = np.sin(u)*np.sin(v)*15*pow(10,6)
z = np.cos(v)*7*pow(10,1.75)
fig = plt.figure()
ax=Axes3D(fig)
ax.plot_surface(x,y,z, color='yellow')
u=0     #x-position of the center
v=0-2E6   #y-position of the center
a=149598261     #radius on the x-axis
b=149577000   #radius on the y-axis




ax.plot(SMX,SMY,SMZ)
ax.plot(SSCX,SSCY,SSCZ)
ax.plot(MSCX,MSCY,MSCZ)
ax.view_init(45, 45)
plt.show()




plt.plot(SMX,SMY)
plt.plot(SSCX,SSCY)
plt.plot(MSCX,MSCY)
plt.grid(True)
plt.show()


DeltaX=abs(SSCX-MSCX)
DeltaY=abs(SSCY-MSCY)
DeltaZ=abs(SSCY-MSCY)

plt.plot(DeltaX)
plt.show()
plt.plot(DeltaY)
plt.show()
plt.plot(DeltaZ)
plt.show()


EpsX=DeltaX/SSCX*100
EpsY=DeltaY/SSCY*100
EpsZ=DeltaZ/SSCZ*100

plt.plot(EpsX)
plt.plot(EpsY)
plt.plot(EpsZ)
plt.show()


MedEpsX=np.median(EpsX)
MedEpsY=np.median(EpsY)
MedEpsZ=np.median(EpsZ)

print("EpsX =",MedEpsX)
print("EpsY =",MedEpsY)
print("EpsZ =",MedEpsZ)









