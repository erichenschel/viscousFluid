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

import numpy as np

class calc:

    def __init__(self):
        self.step = 0.01 # -- time step
        self.mass = 1.0 #kg -- mass
        self.g = 9.81 #m/s/s -- gravity
        self.vo = 5.0 #m/s -- initial velocity
        self.yo = 0.0 #m -- initial position
        self.to = 0.0 #s -- initial time
        self.mu = 8.9 * 10**(-4) #Pa s -- viscosity (water at 25 deg celsius)
        self.radius = 0.01 #m (1 cm) -- radius
    
    # params:: r - radius, mu - viscosity
    def b(r, mu):
        return (6 * np.pi * self.mu * self.radius)

    # y'' = f(v) = acceleration
    def f(v):
        zo = self.b(self.r, self.mu) * v / self.mass
        return (-self.g - zo)

    # y = velocity
    def euler_vel(self):
        time = []
        vel = [self.vo]
        for i in range(0, 100):
            v = vel[i]
            a = f(v)
            vn = v + a * self.step
            vel.append(vn)
            time.append(self.step*i)

        return time, est
            
    def euler_pos(self):
        time = []
        est = [self.vo]
        for i in range(0, 100):


    def rkMethod(self):

    # analytical equation for velocity
    def vel(t):
        z1 = ((-5.0*self.mass/self.b) - (self.g*self.mass*self.mass/(self.b*self.b)))
        e = np.exp(-self.b*t/self.mass)
        z2 = 5.0*self.mass/self.b
        z3 = self.g*self.mass*self.mass/(self.b*self.b)
        z4 = -self.g*self.mass*t/self.b
        return z1 * e + z2 + z3 + z4



