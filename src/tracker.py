import numpy as np
import matplotlib.pyplot as plt

#Define tracker class
class Tracker():
    def __init__(self, sides, radi):
        self.sides = sides
        self.radi = radi

    def polygon_points(self,r):
        #generate n points on a circle
        theta = np.linspace(0, 2*np.pi, self.sides+1)
        x = r*np.cos(theta)
        y = r*np.sin(theta)
        return (np.array([x,y]))

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

    def plot_polygon(self,r):
        x,y=self.polygon_points(r)
        for i in range(self.sides):
            self.plot_line(x[i],y[i],x[i+1],y[i+1])

    def layers(self):
        for i in self.radi:
            self.plot_polygon(i)

    def intersection(self,x_0,y_0,r):
        x,y=self.polygon_points(r)
        for i in range(self.sides):
            a,b=self.line(x[i],y[i],x[i+1],y[i+1])
            f=a*x_0+b
            if (np.around(y_0,decimals=1) == np.around(f,decimals=1)):
                plt.plot(x_0,y_0,"g+", markersize=18)
                #break
                #print(x_0,y_0)

    def int_layers(self,x_0,y_0):
        for i in self.radi:
            self.intersection(x_0,y_0,i)

if __name__ == "__main__":
	print("Tracker class")
