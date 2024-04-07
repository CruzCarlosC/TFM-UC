import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker

track=Track()
tracker=Tracker(6,5)
x,y,z=track.eq_motion(np.linspace(-10,10,100))
a=tracker.intersection(x,y,z)
tracker.plot_polygon()
track.transverse_plot()
#track.zy_plot()
for i in range(len(a)):
    plt.plot(a[i][0],a[i][1],"rx", label='Intersection')
plt.show()