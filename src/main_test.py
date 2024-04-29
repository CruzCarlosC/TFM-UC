import numpy as np
import matplotlib.pyplot as plt
from track2 import Track
from tracker2 import Tracker

#Kalman filter
def kalman_filter(x,y,z):
    """
    Kalman filter
    """
    #Initial conditions
    x0=np.array([x[0],y[0],z[0],0,0,0])
    P0=np.eye(6)
    #Process noise
    Q=np.eye(6)
    #Measurement noise
    R=np.eye(3)
    #Transition matrix
    A=np.array([[1,0,0,1,0,0],
                [0,1,0,0,1,0],
                [0,0,1,0,0,1],
                [0,0,0,1,0,0],
                [0,0,0,0,1,0],
                [0,0,0,0,0,1]])
    #Measurement matrix
    H=np.array([[1,0,0,0,0,0],
                [0,1,0,0,0,0],
                [0,0,1,0,0,0]])
    #Kalman filter
    x_hat=x0
    P=P0
    x_hat_list=[]
    for i in range(len(x)):
        #Prediction
        x_hat_minus=A@x_hat
        P_minus=A@P@A.T + Q
        #Update
        K=P_minus@ H.T @ np.linalg.inv(H@P_minus@H.T + R)
        x_hat=x_hat_minus + K@(np.array([x[i],y[i],z[i]]) - H@x_hat_minus)
        P=(np.eye(6) - K@H)@P_minus
        x_hat_list.append(x_hat)
    return np.array(x_hat_list)


#Particle track
track=Track(x0=0.5,y0=0.5, phi=np.random.uniform(-np.pi/2,np.pi/2))
x,y,z=track.eq_motion(np.linspace(0,10,100))

n=10
t,l=[],[]
for i in range(n):
    t.append(Tracker(12,1+i*0.5))
    l.append([[],[],[]])


for i in range(x.size):
    #Bucle sobre los poligonos  
    for j in range(len(t)):
        if t[j].inter(x[i],y[i])!=None:
            x0,y0=t[j].inter(x[i],y[i])
            l[j][0].append(x0)
            l[j][1].append(y0)
            l[j][2].append(z[i])


a,b,c=[],[],[]
for i in range(len(l)):
    a.append(np.mean(np.array(l[i][0])))
    b.append(np.mean(np.array(l[i][1])))
    c.append(np.mean(np.array(l[i][2])))


x_hat=kalman_filter(np.array(a),np.array(b),np.array(c))

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(x,y,z,label='True')
ax.scatter(a,b,c,label='Tracker',color='red')
ax.scatter(x_hat[:,0],x_hat[:,1],x_hat[:,2],label='Kalman', color='green', linestyle='dashed')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()

"""

#Plots
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x,y,z,color='blue')
ax.scatter(a,b,c,color='red')
ax.plot(0,0,0,'go')
plt.title("3D Intersection")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

plt.plot(x,y,color='blue')
plt.plot(a,b,'rx')
for i in range(len(t)):
    t[i].plot_polygon()
plt.title("Transverse Plane Intersection")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.plot(z,y,color='blue')
plt.plot(c,b,'rx')
plt.title("Z-Y Plane Intersection")
plt.xlabel('z')
plt.ylabel('y')
plt.show()

plt.plot(x,z,color='blue')
plt.plot(a,c,'rx')
plt.title("X-Z Plane Intersection")
plt.xlabel('x')
plt.ylabel('z')
plt.show()
"""