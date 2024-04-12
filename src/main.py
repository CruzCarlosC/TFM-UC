import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker


#Particle track
track=Track()
x,y,z=track.eq_motion(np.linspace(0,10,100))

t1=Tracker(20,5)
t2=Tracker(10,7)
t3=Tracker(10,9)

t=[t1,t2,t3]


for i in range(x.size):
    for j in t:
        if j.inter(x[i],y[i])!=None:
            x0,y0=j.inter(x[i],y[i])
            plt.plot(x0,y0,'rx')


plt.plot(x,y,color='blue')
t1.plot_polygon()
t2.plot_polygon()
t3.plot_polygon()
plt.title("Transverse Plane Intersection")
plt.show()
