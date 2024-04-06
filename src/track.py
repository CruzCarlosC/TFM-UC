import numpy as np
import matplotlib.pyplot as plt

#Define track class
class Track():
    def __init__(self):
        """
        Definir constantes y variables
        """
        self.phi = np.pi/2 #np.random.uniform(0,np.pi)
        self.eta = 1.5 #pseudorapidity
        self.k=0.29979 #GeV/(cTm)
        self.q=-1 #negative or positive factor of e
        self.pt=50 #GeV/c
        self.pz=20 #GeV/c
        self.m=0.106 #GeV/c**2
        self.beta= np.sqrt(self.pt**2 + self.pz**2)/np.sqrt(self.pt**2 + self.pz**2 + self.m**2)
        self.gama=1/(np.sqrt(1-self.beta**2))
        self.B=3.88 #T
        self.r=self.pt/(self.k*self.q*self.B)
        self.w=self.k*self.q*self.B/(self.gama*self.m)
        self.x0=0
        self.y0=0
        self.z0=0

    def motion(self,t):
        """
        Puntos de la trayectoria de la partícula cargada en un campo magnético
        """
        x=self.x0 + self.r * (np.sin(self.w*t - self.phi) + np.sin(self.phi))
        y=self.y0 + self.r * (np.cos(self.w*t - self.phi) - np.cos(self.phi))
        z=self.z0 + self.pt*np.sinh(self.eta)*t/(self.m * self.gama)
        #return (np.array([x,y,z]))
        return (x,y,z)

    def update_motion(self):
        #Empty ndarray
        x=np.array([])
        y=np.array([])
        #append to the empty ndarray
        i=0
        while i<2e-4:
            x=np.append(x,self.motion(i)[0])
            y=np.append(y,self.motion(i)[1])
            i=i+2e-6
        return (x,y)
        
    def update_and_store(self,x,y,dt):
        x=np.append(x,self.motion(dt)[0])
        y=np.append(y,self.motion(dt)[1])
        return (x,y)

    def plot_motion(self):
        x,y=self.update_motion()
        plt.plot(x,y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Motion of a charged particle in a magnetic field')
        plt.show()
    
    def plot3d(self):
        t=np.linspace(-10,10,100)
        x,y,z=self.motion(t)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x,y,z, label='parametric curve')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend()


 
if __name__ == "__main__":
    print("Track class")
    track=Track()
    track.plot3d()
    plt.show()
