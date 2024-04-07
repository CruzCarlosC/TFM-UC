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

    def eq_motion(self,t):
        """
        Puntos de la trayectoria de la partícula cargada en un campo magnético
        """
        x=self.x0 + self.r * (np.sin(self.w*t - self.phi) + np.sin(self.phi))
        y=self.y0 + self.r * (np.cos(self.w*t - self.phi) - np.cos(self.phi))
        z=self.z0 + self.pt*np.sinh(self.eta)*t/(self.m * self.gama)
        return (x,y,z)

    def transverse_plot(self):
        t=np.linspace(-10,10,100)
        x,y,z=self.eq_motion(t)
        plt.plot(x,y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Transverse plane')
        #plt.show()
    
    def zy_plot(self):
        t=np.linspace(-10,10,100)
        x,y,z=self.eq_motion(t)
        plt.plot(z,y)
        plt.xlabel('z')
        plt.ylabel('y')
        plt.title('Z-Y plane')
        #plt.show()
    
    def plot3d(self):
        t=np.linspace(-10,10,100)
        x,y,z=self.eq_motion(t)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x,y,z, label='parametric curve')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend()
        plt.show()


 
if __name__ == "__main__":
    print("Track class")