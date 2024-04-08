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
        plane=[]
        for i in range(self.sides):
            p1=np.array([x[i],y[i],1])
            p2=np.array([x[i+1],y[i+1],3])
            p3=np.array([x[i],y[i],3])
            #Normal vector
            c=np.cross(p2-p1,p3-p1)
            k=(c[0]*p1[0]+c[1]*p1[1]+c[2]*p1[2])*-1
            #Add k to the normal vector
            c=np.append(c,k)
            plane.append(c)
        return plane

    def plot_plane(self):
        x,y=self.polygon_points()
        plane=self.plane_points()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        #color=['blue','red','green','yellow','purple','orange']
        for i in range(self.sides):
            xs=np.linspace(-25,25,100)
            zs=np.linspace(-25,25,100)
            X, Z = np.meshgrid(xs, zs)
            Y = (plane[i][3] - plane[i][0]*X)/plane[i][1]
            ax.plot_surface(X, Y, Z, color='blue')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
        plt.show()

    def intersection(self,x,y,z):
        """
        Intersection of the plane with the particle track
        Busca en cada plano del poligono si hay interseccion con la trayectoria de la particula
        """
        plane=self.plane_points()
        cut=[]
        for i in range(self.sides):
            for j in range(x.size):
                if int(plane[i][0]*x[j]+ plane[i][1]*y[j]+ plane[i][2]*z[j] + plane[i][3]) == 0:
                    cut.append([x[j],y[j],z[j]])
                    break
        return cut

    def inter_2(self,x,y,z):
        """
        Interseccion de un punto con el poligono
        """
        plane=self.plane_points()
        for i in range(self.sides):
            if int(plane[i][0]*x+ plane[i][1]*y+ plane[i][2]*z + plane[i][3]) == 0:
                return i


if __name__ == "__main__":
    print("Tracker class")