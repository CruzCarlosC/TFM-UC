import numpy as np
import matplotlib.pyplot as plt

#Equation of motion
def eq_motion(t):
    x=0 + 5 * (np.sin(t - np.pi/2) + np.sin(np.pi/2))
    y=0 + 5 * (np.cos(t - np.pi/2) - np.cos(np.pi/2))
    z=0 + 3 * t
    return (x,y,z)

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
xt,yt,zt=eq_motion(np.linspace(0,10,100))
x,y,z=eq_motion(np.linspace(0,10,10))
x1,y1,z1=eq_motion(np.linspace(0,10,30))
x_hat=kalman_filter(x,y,z)
x_hat1=kalman_filter(x1,y1,z1)

#Plot
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(xt,yt,zt,label='True', color="blue")
ax.plot(x_hat[:,0],x_hat[:,1],x_hat[:,2],label='Kalman 10 points', color="red")
ax.plot(x_hat1[:,0],x_hat1[:,1],x_hat1[:,2],color="orange",label='Kalman 30 points')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()
