import numpy as np
import matplotlib.pyplot as plt

#Define tracker class
class Tracker():
    def __init__(self, sides, radi):
        """
            La entrada es el numero de lados
            Y el radio de una circunferencia circunscrita en el poligono
        """
        self.sides = sides
        self.radi = radi

    def polygon_points(self):
        """
            Generar puntos del poligono
            Array
        """
        theta = np.linspace(0, 2*np.pi, self.sides+1)
        x = self.radi*np.cos(theta)
        y = self.radi*np.sin(theta)
        return (np.round(x,3),np.round(y,3))

    def line(self,x1,y1,x2,y2):
        """
            Calcular parametros de una recta
            Pendiente y ordenada
            Dados dos puntos
        """
        #slope
        if x2-x1 == 0:
            m=0
        else:
            m=(y2-y1)/(x2-x1)
        #y-intercept
        b=y1-m*x1
        return (np.round(m,3),np.round(b,3))

    def plot_line(self,x1,y1,x2,y2):
        """
            Graficar una recta dados dos puntos
        """
        a,b=self.line(x1,y1,x2,y2)
        if x2-x1 == 0:
            plt.plot(x1*np.ones(100),np.linspace(y1,y2,100),color="black")
        else:
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
        return (np.round(c,3),np.round(k,3))
    
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
            c=np.cross(p2-p1,p3-p1)/np.linalg.norm(np.cross(p2-p1,p3-p1))
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

    def inter(self,x,y):
        """
            Prueba interseccion de un punto con el poligono
        """
        
        #Puntos del poligono
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
            for i in cx:
                for j in cy:
                    if i==j:
                        c=i
                        break
        if c>=0:
            plan,k=self.plane(px[c],py[c],px[c+1],py[c+1])
            if int(plan[0]*x+plan[1]*y+plan[2]*1+k)==0:
                return (x,y)

    def inter2(self,x,y,z):
        plane=self.plane_points()
        xp,yp=self.polygon_points()
        for i in range(self.sides):
            cc=np.argwhere((plane[i][0]*x+plane[i][1]*y+plane[i][3]).astype(int)==0)
            if cc.size>0:
                a=x[cc].mean()
                b=y[cc].mean()
                c=z[cc].mean()
                if (xp[i]<=a and xp[i+1]>=a) or (xp[i]>=a and xp[i+1]<=a):
                    if (yp[i]<=b and yp[i+1]>=b) or (yp[i]>=b and yp[i+1]<=b):
                        return (a,b,c,i)

    def Kal_init(self):
        """
            Inicializar Kalman
        """
        x0=np.array([x[0],y[0],z[0],0,0,0])
        P0=np.eye(6)
        Q=np.eye(6)
        R=np.eye(3)
        A=np.array([[1,0,0,1,0,0],
                    [0,1,0,0,1,0],
                    [0,0,1,0,0,1],
                    [0,0,0,1,0,0],
                    [0,0,0,0,1,0],
                    [0,0,0,0,0,1]])
        H=np.array([[1,0,0,0,0,0],
                    [0,1,0,0,0,0],
                    [0,0,1,0,0,0]])
        return (x0,P0,Q,R,A,H)

    def Kal_filter(self,x0,P0,Q,R,A,H,x,y,z):
        """
            Filtro de Kalman
        """
        x_hat=x0
        P=P0

        x_hat_minus=A@x_hat
        P_minus=A@P@A.T + Q
        K=P_minus@ H.T @ np.linalg.inv(H@P_minus@H.T + R)
        x_hat=x_hat_minus + K@(np.array([x,y,z]) - H@x_hat_minus)
        P=(np.eye(6) - K@H)@P_minus

        return x_hat

if __name__ == "__main__":
    print("Tracker class")