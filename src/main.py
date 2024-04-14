import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker


#Particle track
track=Track(x0=0.5,y0=0.5)
x,y,z=track.eq_motion(np.linspace(0,10,100))

n=5
t,l=[],[]
for i in range(n):
    t.append(Tracker(12,1+i))
    l.append([[],[]])


for i in range(x.size):
    #Bucle sobre los poligonos  
    for j in range(len(t)):
        if t[j].inter(x[i],y[i])!=None:
            x0,y0=t[j].inter(x[i],y[i])
            l[j][0].append(x0)
            l[j][1].append(y0)

for i in range(len(l)):
    plt.plot(np.mean(np.array(l[i][0])),np.mean(np.array(l[i][1])),'rx')

plt.plot(x,y,color='blue')
for i in range(len(t)):
    t[i].plot_polygon()
plt.title("Transverse Plane Intersection")
plt.show()
