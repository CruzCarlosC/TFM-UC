import numpy as np
import matplotlib.pyplot as plt

#Define track class
class Track():
    def __init__(self,phi=np.pi/2,eta=1.5,q=-1,pt=50,d0=0.5,z0=0):
        """
        Definir constantes y variables
        """
        self.phi = phi #initial phase
        self.eta = eta #pseudorapidity
        self.k=0.29979 #GeV/(cTm)
        self.q=q #negative or positive factor of e
        self.pt=pt #GeV/c
        self.pz=pt*np.sinh(self.eta) #GeV/c
        self.m=0.106 #GeV/c**2
        self.beta= np.sqrt(self.pt**2 + self.pz**2)/np.sqrt(self.pt**2 + self.pz**2 + self.m**2)
        self.gamma=1/(np.sqrt(1-self.beta**2))
        self.B=3.88 #T
        self.r=self.pt/(self.k*self.q*self.B)
        self.w=self.k*self.q*self.B/(self.gamma*self.m)
        self.d0=d0
        self.xp=-d0*np.sin(self.phi)
        self.yp=d0*np.cos(self.phi)
        self.zp=z0
  
    def eq_motion(self,t):
        #Ecuaciones originales
        x=self.xp + self.r * (np.sin(self.w*t - self.phi) + np.sin(self.phi))
        y=self.yp + self.r * (np.cos(self.w*t - self.phi) - np.cos(self.phi))
        z=self.zp + self.pz*t/(self.m * self.gamma)
        return (x*100,y*100,z*100)

    def transverse_plot(self,t):
        x,y,z=self.eq_motion(t)
        plt.plot(x,y,color='blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Transverse plane')
        plt.show()
    
    def zy_plot(self,t):
        x,y,z=self.eq_motion(t)
        plt.plot(z,y)
        plt.xlabel('z')
        plt.ylabel('y')
        plt.title('Z-Y plane')
        plt.show()
    
    def plot3d(self,t):
        x,y,z=self.eq_motion(t)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x,y,z, label='parametric curve')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.legend()
        plt.show()

    def test(self,t):
        rt=self.pt / (self.q * self.B) * (1000.0/2.998)
        wt=self.q * 0.089880 * self.B / (self.gamma * self.m)
        x = rt * (np.sin(wt * t - self.phi) + np.sin(self.phi))+ self.xp     
        y = rt * (np.cos(wt * t - self.phi) - np.cos(self.phi))+ self.yp
        z = 29.98 * self.pz / (self.gamma*self.m) * t + self.zp
        return (x,y,z)
 
if __name__ == "__main__":
    print("Track class")
    """
    t=Track(phi=np.pi/4,eta=1.5,q=-1,pt=50,d0=0,z0=0)
    time=np.arange(0,10,0.03)

    x1,y1,z1=t.eq_motion(time)
    x2,y2,z2=t.test(time)

    plt.plot(x1,y1,color='blue',label='Original')
    plt.plot(x2,y2,color='red', label='Test', linestyle='dashed')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title('Transverse plane')
    plt.show()

    plt.plot(z1,y1,color='blue',label='Original')
    plt.plot(z2,y2,color='red', label='Test', linestyle='dashed')
    plt.xlabel('z')
    plt.ylabel('y')
    plt.legend()
    plt.title('Z-Y plane')
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x1,y1,z1, label='Original')
    ax.plot(x2,y2,z2, label='Test', linestyle='dashed')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.legend()
    plt.show()
    """