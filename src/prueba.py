import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker



#Particle track
track=Track()
x,y,z=track.eq_motion(np.linspace(0,10,100))

t1=Tracker(10,4.4)
t2=Tracker(10,7.3)
t3=Tracker(10,10.2)
t4=Tracker(8,20)
t5=Tracker(8,30)

t=[t1,t2,t3,t4,t5]

pl=[]
for j in t:
    for i in range(x.size):
        if j.inter_2(x[i],y[i],z[i])!=None:
            p,x1,x2,x3=j.inter_2(x[i],y[i],z[i])
            pl.append([x1,x2,x3])
            break

print(pl)


t1.plot_polygon()
t2.plot_polygon()
t3.plot_polygon()
t4.plot_polygon()
t5.plot_polygon()
plt.plot(x,y, color='blue')
for i in pl:
    plt.plot(i[0],i[1],'rx')
plt.title("Transverse Plane")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-30,30)
plt.ylim(-30,30)
plt.show()
