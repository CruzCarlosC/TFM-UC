import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker

#Particle track
track=Track()
x,y,z=track.eq_motion(np.linspace(0,10,100))

#Detector
t1=Tracker(10,5)
t2=Tracker(10,7)

a1=t1.intersection(x,y,z)
a2=t2.intersection(x,y,z)

t1.plot_polygon()
t2.plot_polygon()
track.transverse_plot()

for i in range(len(a1)):
    plt.plot(a1[i][0],a1[i][1],"rx")

for i in range(len(a2)):
    plt.plot(a2[i][0],a2[i][1],"rx")
plt.plot(0,0,"go", label='Origin')
plt.legend()
plt.show()