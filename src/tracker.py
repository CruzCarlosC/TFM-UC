import numpy as np
import matplotlib.pyplot as plt

#Define tracker class
class Tracker():
    def __init__(self, sides, radi):
        self.sides = sides
        self.radi = radi

    def polygon_points(self):
        #generate n points on a circle
        theta = np.linspace(0, 2*np.pi, self.sides+1)
        x = self.radi*np.cos(theta)
        y = self.radi*np.sin(theta)
        return (x,y)
        #return (np.array([x,y]))

    def line(self,x1,y1,x2,y2):
        #slope
        m=(y2-y1)/(x2-x1)
        #y-intercept
        b=y1-m*x1
        return (m,b)

    def plot_line(self,x1,y1,x2,y2):
        #plot a line
        a,b=self.line(x1,y1,x2,y2)
        t=np.linspace(x1,x2,100)
        f=a*t+b
        plt.plot(t,f,color='black')

    def plot_polygon(self):
        x,y=self.polygon_points()
        for i in range(self.sides):
            self.plot_line(x[i],y[i],x[i+1],y[i+1])
    
    def plane_points(self):
        x,y=self.polygon_points()
        cut=[]
        for i in range(self.sides):
            p1=np.array([x[i],y[i],1])
            p2=np.array([x[i+1],y[i+1],3])
            p3=np.array([x[i],y[i],3])
            #Normal vector
            c=np.cross(p2-p1,p3-p1)
            k=(c[0]*p1[0]+c[1]*p1[1]+c[2]*p1[2])*-1
            cut.append([c,k])
        return cut



if __name__ == "__main__":
    print("Tracker class")
    #Create object
    track = Tracker(6,5)
    #Plot polygon
    track.plot_polygon()
    plt.show()