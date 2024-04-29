import numpy as np
import matplotlib.pyplot as plt

#Define track class
class Track():
    def __init__(self,phi=np.pi/2,eta=1.5,q=-1,pt=50,pz=20,x0=1,y0=1,z0=0):
        """
        Definir constantes y variables
        La entrada son los parametros de la helice
        """
        self.phi = phi #initial phase
        self.eta = eta #pseudorapidity
        self.k=0.29979 #GeV/(cTm)
        self.q=q #negative or positive factor of e
        self.pt=pt #GeV/c
        self.pz=pz #GeV/c
        self.m=0.106 #GeV/c**2
        self.beta= np.sqrt(self.pt**2 + self.pz**2)/np.sqrt(self.pt**2 + self.pz**2 + self.m**2)
        self.gamma=1/(np.sqrt(1-self.beta**2))
        self.B=3.88 #T
        self.r=self.pt/(self.k*self.q*self.B)
        self.w=self.k*self.q*self.B/(self.gamma*self.m)
        self.x0=x0
        self.y0=y0
        self.z0=z0

    def poca_points(self):
        """
        Punto de aproximación más cercano
        """
        
        den=(self.y0 - (self.r)*(np.cos(self.phi)))
        if den == 0:
            print("no solution")

        num=(self.x0 + (self.r)*(np.sin(self.phi)))
        #Tiempo
        t_poca=(self.phi + np.arctan2(num,den)) / self.w
        
        #Posicion
        x_poca=self.x0+(self.r)*(np.sin(self.w*t_poca-self.phi)+np.sin(self.phi))
        y_poca=self.y0+(self.r)*(np.cos(self.w*t_poca-self.phi)-np.cos(self.phi))
        z_poca=self.z0+(self.pt/(self.gamma*self.m))*np.sinh(self.eta)*t_poca
        
        #Momentum
        px=self.pt*np.cos(self.w*t_poca-self.phi)
        py=-self.pt*np.sin(self.w*t_poca-self.phi)
        
        #Angulo
        phi_poca= np.arctan2(py, px)

        return (x_poca,y_poca,z_poca,phi_poca,t_poca)
    
    def eq_motion(self,t,poca_flag=True):
        """
        Puntos de la trayectoria de la partícula cargada en un campo magnético
        En función del tiempo, t puede ser un escalar o un array
        La variable booleana permite escoger la parametrizacion
        """
        if poca_flag:
            #Ecuaciones con el punto de aproximación más cercano
            xp,yp,zp,phi_poca,t_poca=self.poca_points()
            
            tm=np.linspace(t_poca,t[-1],t.size)
            
            x=xp+(self.r)*(np.sin(self.w*(tm-t_poca)-phi_poca)+np.sin(phi_poca))
            y=yp+(self.r)*(np.cos(self.w*(tm-t_poca)-phi_poca)-np.cos(phi_poca))
            z=zp+(self.pt/(self.gamma*self.m))*np.sinh(self.eta)*(tm-t_poca)
            return (x,y,z)

        if not poca_flag:
            #Ecuaciones originales
            x=self.x0 + self.r * (np.sin(self.w*t - self.phi) + np.sin(self.phi))
            y=self.y0 + self.r * (np.cos(self.w*t - self.phi) - np.cos(self.phi))
            z=self.z0 + self.pt*np.sinh(self.eta)*t/(self.m * self.gamma)
            return (x,y,z)

    def transverse_plot(self,t,poca_flag=True,lab="track", col="blue"):
        """
            Grafico transversal de la curva
            Plano XY
        """
        x,y,z=self.eq_motion(t,poca_flag)
        plt.plot(x,y,label=lab, color=col)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Transverse plane')
        plt.legend()
        #plt.show()
    
    def zy_plot(self,t,poca_flag=True,lab="track", col="blue"):
        """
            Plano ZY
        """
        x,y,z=self.eq_motion(t,poca_flag)
        plt.plot(z,y,label=lab, color=col)
        plt.xlabel('z')
        plt.ylabel('y')
        plt.legend()
        plt.title('Z-Y plane')
        #plt.show()
    
    def plot3d(self,t,poca_flag=True):
        """
            Grafico 3D de la curva
            En función del tiempo, t puede ser un escalar o un array
            La variable booleana permite escoger la parametrizacion
        """
        if poca_flag:
            xp,yp,zp,phi_poca,t_poca=self.poca_points()
            t=np.linspace(t_poca,10,100)
            x,y,z=self.eq_motion(t,poca_flag=True)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(x,y,z, label='parametric curve')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.legend()
            #plt.show()
        if not poca_flag:
            x,y,z=self.eq_motion(t,poca_flag)
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(x,y,z, label='parametric curve')
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.legend()
            #plt.show()


 
if __name__ == "__main__":
    print("Track class")