import numpy as np
import matplotlib.pyplot as plt
from track import Track
import csv

n=100

"""
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for i in range(n):
    #Valores iniciales aleatorios
    x0=1#np.random.uniform(1,2)
    y0=1#np.random.uniform(1,2)
    z0=1#np.random.uniform(1,2)
    phi=np.random.uniform(-np.pi,np.pi)
    eta=np.random.uniform(0.2,2.4)
    q=-1 #Usar 1 da putnos muy lejanos, revisar!
    pt=np.random.normal(100,20)
    pz=np.random.normal(20,5)

    #Instancia de la clase Track
    t=Track(phi,eta,q,pt,pz,x0,y0,z0)
    #Puntos poca
    xp,yp,zp,phi_poca,t_poca=t.poca_points()
    #print(f"phi: {phi}, eta: {eta}, q: {q}, pt: {pt}, pz: {pz}, xp: {xp}, yp: {yp}, zp: {zp}, phi_poca: {phi_poca}, t_poca: {t_poca}")
    x,y,z=t.eq_motion(np.linspace(t_poca,10,100))
    ax.plot(x,y,z,color='blue')
    ax.plot([xp],[yp],[zp],'rx')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
"""
    



with open('tracks.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['phi','eta','q','pt','pz','xp','yp','zp','phi_poca','t_poca'])

    for i in range(n):
        #Valores iniciales aleatorios
        x0=np.random.uniform(1,2)
        y0=np.random.uniform(1,2)
        z0=np.random.uniform(1,2)
        phi=np.random.uniform(-np.pi,np.pi)
        eta=np.random.uniform(0.5,2.4)
        q=-1#np.random.choice([-1,1])
        pt=np.random.normal(50,10)
        pz=np.random.normal(20,5)

        #Instancia de la clase Track
        t=Track(phi,eta,q,pt,pz,x0,y0,z0)
        #Puntos poca
        xp,yp,zp,phi_poca,t_poca=t.poca_points()
        writer.writerow([phi,eta,q,pt,pz,xp,yp,zp,phi_poca,t_poca])
