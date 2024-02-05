import numpy as np
import matplotlib.pyplot as plt

#Define track class
class Track():
    def __init__(self):
        self.phi = np.pi/2 #np.random.uniform(0,np.pi)
        self.eta = 2 #np.around(np.random.uniform(0,2), decimals=3)
        self.q=-1.6e-19  #np.random.choice([1,-1])
        self.B=4
        self.m=1.5e-31
        self.v_0=0.3e5
        self.gam=1/(np.sqrt(1- (self.v_0**2 / 3e8**2) ))
        self.wB=self.q* self.B / (self.m * 3e8) *self.gam

    def motion(self,t):
        #t=np.linspace(0,2e-4,100)
        x=self.v_0/self.wB * (np.cos(self.wB*t - self.phi) - np.cos(self.phi))
        y=self.v_0/self.wB * (np.sin(self.wB*t - self.phi) + np.sin(self.phi))
        z=np.sinh(self.eta)*t*self.v_0/(self.m * self.gam)
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
