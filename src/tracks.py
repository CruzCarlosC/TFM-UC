import numpy as np
import matplotlib.pyplot as plt
from track import Track
from tracker import Tracker
import os
import csv

"""
    Generar n tracks aleatorios
    Guardarlos en un archivo csv
    Junto con los parametros de la trayectoria
"""

#Trackers
m=10
tk=[]
for i in range(m):
    tk.append(Tracker(12,10+i*10))


#Tracks
n=150
time=np.arange(0,450,0.03)

#Open file to save tracks in this path
script_dir = os.path.dirname(os.path.abspath(__file__))
name="points_"+str(n)+".csv"
file2_path = os.path.join(script_dir, name)

points_file=open(file2_path,"w")

points_writer=csv.writer(points_file)

#Header
points_writer.writerow(['x','y','z','N_side','N_layer','t_label','p_label','phi','eta','q','pt','d0','z0'])

lab_cont=0
point_cont=0

while lab_cont<n:
    #Random tracks
    d0=np.random.uniform(-0.5,0.5)
    z0=np.random.uniform(-0.5,0.5)
    phi=np.random.uniform(-np.pi,np.pi)
    eta=np.random.uniform(-2.4,2.4)
    q=np.random.choice([-1,1])
    pt=np.random.uniform(25,100)

    t=Track(phi,eta,q,pt,d0,z0)
    x,y,z=t.eq_motion(time)

    #String format "T"+c
    t_lab="T"+str(lab_cont)

    #Intersection
    cont=0
    empt=[]
    for j in tk:
        kk=j.inter2(x,y,z)
        if kk != None:
            a,b,c,d=kk
            p_lab="P"+str(point_cont)
            empt.append([a,b,c,d,cont+1,t_lab,p_lab,t.phi,t.eta,t.q,t.pt,t.d0,t.zp])
            point_cont+=1
            #plt.plot(a,b,"rx")
        cont+=1
    
    if len(empt)==10:
        for j in empt:
            points_writer.writerow(j)
        lab_cont+=1


"""
for i in range(n):
    #Random tracks
    d0=np.random.uniform(-0.5,0.5)
    z0=np.random.uniform(-0.5,0.5)
    phi=np.random.uniform(-np.pi,np.pi)
    eta=np.random.uniform(-2.4,2.4)
    q=np.random.choice([-1,1])
    pt=np.random.uniform(25,100)

    t=Track(phi,eta,q,pt,d0,z0)
    x,y,z=t.eq_motion(time)

    #String format "T"+c
    t_lab="T"+str(lab_cont)

    #Intersection
    cont=0
    empt=[]
    for j in tk:
        kk=j.inter2(x,y,z)
        if kk != None:
            a,b,c,d=kk
            p_lab="P"+str(point_cont)
            empt.append([a,b,c,d,cont+1,t_lab,p_lab,t.phi,t.eta,t.q,t.pt,t.d0,t.zp])
            point_cont+=1
            #plt.plot(a,b,"rx")
        cont+=1
    
    if len(empt)==10:
        for j in empt:
            points_writer.writerow(j)

    lab_cont+=1
"""


#plt.show()

#close file
points_file.close()
