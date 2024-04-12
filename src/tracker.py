import numpy as np
import matplotlib.pyplot as plt

#Define tracker class
class Tracker():
    def __init__(self, sides, radi):
        self.sides = sides
        self.radi = radi

    def polygon_points(self):
        """
        Puntos de poligono
        """
        theta = np.linspace(0, 2*np.pi, self.sides+1)
        x = self.radi*np.cos(theta)
        y = self.radi*np.sin(theta)
        return (x,y)

    def line(self,x1,y1,x2,y2):
        """
        Ecuacion de una recta
        """
        #slope
        m=(y2-y1)/(x2-x1)
        #y-intercept
        b=y1-m*x1
        return (m,b)

    def plot_line(self,x1,y1,x2,y2):
        """
        Grafica una linea
        """
        a,b=self.line(x1,y1,x2,y2)
        t=np.linspace(x1,x2,50)
        f=a*t+b
        plt.plot(t,f,color='black')

    def plot_polygon(self):
        """
        Graficar el poligono
        """
        x,y=self.polygon_points()
        for i in range(self.sides):
            self.plot_line(x[i],y[i],x[i+1],y[i+1])
    
    def plane(self,x1,y1,x2,y2):
        """
        Ecuacion del plano
        """
        #vector normal
        c=np.cross(np.array([x2-x1,y2-y1,2]),np.array([0,0,2]))
        #constante
        k=(c[0]*x1+c[1]*y1+c[2]*1)*-1
        return (c,k)
    
    def plane_points(self):
        """
        Ecuacion de los planos
        ax+by+cz+k=0
        c[0]*x+c[1]*y+c[2]*z+c[3]=0
        """
        x,y=self.polygon_points()
        plane=[]
        for i in range(self.sides):
            p1=np.array([x[i],y[i],1])
            p2=np.array([x[i+1],y[i+1],3])
            p3=np.array([x[i],y[i],3])
            #vector normal
            c=np.cross(p2-p1,p3-p1)
            #constante
            k=(c[0]*p1[0]+c[1]*p1[1]+c[2]*p1[2])*-1
            c=np.append(c,k)
            plane.append(c)
        return plane

    def plot_plane(self):
        """
        Graficar los planos
        """
        x,y=self.polygon_points()
        plane=self.plane_points()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
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

    def inter(self,x,y):#,x,y,z):
        """
        Prueba interseccion de un punto con el poligono
        """
        px,py=self.polygon_points()

        cx=[]
        cy=[]
        #Ubicar x
        for i in range(self.sides):
            if (px[i]<=x and px[i+1]>=x) or (px[i]>=x and px[i+1]<=x):
                cx.append(i)
        #Ubicar y
        for i in range(self.sides):
            if (py[i]<=y and py[i+1]>=y) or (py[i]>=y and py[i+1]<=y):
                cy.append(i)
        c=-1
        if cx and cy:
            for i in range(len(cx)):
                if cx[i]==cy[i]:
                    c=cx[i]
                    #plt.plot(x,y,'rx')
        if c>=0:
            plan,k=self.plane(px[c],py[c],px[c+1],py[c+1])
            if int(plan[0]*x+plan[1]*y+plan[2]*1+k)==0:
                return (x,y)






if __name__ == "__main__":
    print("Tracker class")