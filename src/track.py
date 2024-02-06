import numpy as np
import matplotlib.pyplot as plt

#Define track class
class Track():
    def __init__(self):
        """
        Definir constantes y variables
        """
        self.phi = np.pi/2 #np.random.uniform(0,np.pi)
        self.eta = 2 #pseudorapidity
        self.k=0.29979 #GeV/(cTm
        self.q=-1 #negative or positive factor of e=1.6e-19
        self.beta=0.8 #units of c
        self.gama=1/(np.sqrt(1-self.beta**2))
        self.pt=10 #GeV/c
        self.B=4 #T
        self.m=0.5e-3 #GeV/c**2
        self.r=self.pt/(self.k*self.q*self.B)
        self.w=self.k*self.q*self.B/(self.gama*self.m)

    def motion(self,t):
        """
        Puntos de la trayectoria de la partícula cargada en un campo magnético
        """
        x=self.r * (np.cos(self.w*t - self.phi) - np.cos(self.phi))
        y=self.r * (np.sin(self.w*t - self.phi) + np.sin(self.phi))
        z=np.sinh(self.eta)*t*self.pt/(self.m * self.gama)
        return (np.array([x,y,z]))

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
 
if __name__ == "__main__":
    print("Track class")
