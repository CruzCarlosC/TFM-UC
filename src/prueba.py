import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker

#Particle track
track=Track()
x,y,z=track.eq_motion(np.linspace(0,10,100))

t1=Tracker(20,5)

for i in range(x.size):
    if t1.inter_2(x[i],y[i],z[i])!=None:
        print(t1.inter_2(x[i],y[i],z[i]))
        break





t1.plot_polygon()
plt.plot(x,y, color='blue')

plt.show()