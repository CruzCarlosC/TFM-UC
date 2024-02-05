import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
from tracker import Tracker
from track import Track


time=np.linspace(0,1e-4,100)

def animate(i):
    x1,y1=tr.update_and_store(x,y,time[i])
    plt.cla()
    t.layers()
    plt.scatter(x1,y1)
    t.int_layers(x1[-1],y1[-1])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Motion of a charged particle in a magnetic field')

#Create an instance of the Track class
t=Tracker(20,[1,2,3])
tr=Track()
dt=2e-6
x=np.array([tr.motion(0)[0]])
y=np.array([tr.motion(0)[1]])
ani=FuncAnimation(plt.gcf(),animate,frames=len(time)-1, repeat=True,interval=50)

#Save the animation usingas a gif
#writer =PillowWriter(fps=15,metadata=dict(artist='Me'),bitrate=1800)
#ani.save('scatter_3.gif', writer=writer)

plt.show()
