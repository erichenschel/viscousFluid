# dynamic viscosity (Pa*s=kg/m/s):: molasses is highly viscous -- water is medium viscous -- gas is low viscous
# params::
# Force -- (N)
# step -- 
# mass -- (kg)
# vo -- (m/s) initial velocity
# yo -- (m) initial position
# to -- (s) initial time
# mu -- (Pa s) dynamic viscosity
# r -- (m) radius
# Re -- Reynolds number


import numpy as np

class calc:

    def __init__(self):
        self.step = 0.01 # -- time step
        self.mass = 1.0 #kg -- mass
        self.g = 9.81 #m/s/s -- gravity
        self.vo = 5.0 #m/s -- initial velocity
        self.yo = 0.0 #m -- initial position
        self.to = 0.0 #s -- initial time
        self.density = 1000 #kg/m3
        self.mu = 8.9 * 10**(-4) #Pa s -- viscosity (water at 25 deg celsius)
        self.radius = 0.01 #m (1 cm) -- radius
    
    # Reynolds number using 
    #density (kg/m^3) * fluid flow velocity (m/s) * 
    #length ((m) :: i.e. the diameter of our sphere) / viscosity (Pa s)
    def Re(self):
        return self.density * (1) * (self.radius * 2) / self.mu
    
    def Cd(self):
        return 24 / self.Re() + 6/(1+np.sqrt(self.Re())) + 0.4

    # accounting for half the surface area of a sphere,
    # since the majority of the friction felt will be determined
    # by only one side
    def A(self, r):
        return (0.5) * 4 * np.pi * (self.radius**2)

    def b(self):
        return (0.5) * self.density * self.Cd() * self.A(self.radius)

    """# params:: r - radius, mu - viscosity
    def b(self, r, mu):
        return (6 * np.pi * self.mu * self.radius)
        #return (0.5) * self.density * """

    # y'' = f(v) = acceleration
    def f(self, v):
        zo = self.b() * v / self.mass
        return (-self.g - zo)

    # y = velocity
    def euler_vel(self):
        time = [self.to]
        vel = [self.vo]
        for i in range(0, 50):
            v = vel[i]
            a = self.f(v)
            vn = v + a * self.step
            if vn <=0:
                vel.append(0)
            else:
                vel.append(vn)

            time.append(self.step*float(i+1))

        return time, vel
            
    def euler_pos(self, v):
        pos = [self.xo]
        for i in range(0, 50):
            y = pos[i]
            f = v[i]
            yn = y + f * self.step
            pos.append(yn)
        return pos

    #def rk_Method(self):

    # analytical equation for velocity
    def pos(self, t):
        position = [self.yo]
        for i in range(len(t)):
            zo = (-5.0) * self.mass / self.b()
            z1 = -self.g * (self.mass**2) / (self.b()**2)
            e = np.exp(-self.b() * t[i] / self.mass)
            z2 = (-5.0 * self.mass) / self.b()
            z3 = (-self.g * self.mass**2) / (self.b()**2)
            z4 = (-self.g * self.mass * t[i]) / self.b()
            v = ((zo + z1) * e + z2 + z3 + z4)
            if v<=0:            
                position.append(0)
            else:
                position.append(v)

        return position

    def vel(self, t):
        velocity = []
        for i in range(len(t)):
            zo = (-5.0) * self.mass / self.b()
            z1 = -self.g * (self.mass**2) / (self.b()**2)
            z2 = (-self.b()/self.mass)
            e = np.exp(-self.b() * t[i] / self.mass)
            z3 = -self.g * self.mass / self.b()
            v = (zo + z1) * z2 * e + z3
            velocity.append(v)
        return velocity

    
    def euler_err(self):
        v = self.euler_vel()[1]
        t = self.euler_vel()[0]
        est = self.vel(t)
        print(len(v), len(est))
        print(" Time ", " Pred_Velocity ", " Analytic_Velocity ")
        for i in range(len(t)):
            e = np.abs(v[i]-est[i])
            print(t[i], v[i], est[i], e)


if __name__=="__main__":
    C = calc()
    C.euler_err()
