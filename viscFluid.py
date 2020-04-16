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
    def b(self, r, mu):
        return (6 * np.pi * self.mu * self.radius)

    # y'' = f(v) = acceleration
    def f(self, v):
        zo = self.b(self.radius, self.mu) * v / self.mass
        return (-self.g - zo)

    # y = velocity
    def euler_vel(self):
        time = []
        vel = [self.vo]
        for i in range(0, 50):
            v = vel[i]
            a = f(v)
            vn = v + a * self.step
            vel.append(vn)
            time.append(self.step*i)

        return time, vel
            
    def euler_pos(self, v):
        time = [0.0]
        pos = [self.yo]
        for i in range(0, 50):
				y = pos[i]
				f = v[i]
				yn = 

    #def rkMethod(self):

    # analytical equation for velocity
    def vel(t):
	velocity = []
	for i in range(len(t)):
		zo = -5.0 * self.mass / self.b(self.radius, self.mu)
		z1 = -self.g * self.mass**2 / (self.b(self.radius, self.mu)**2)
		e = np.exp(-self.b(self.radius, self.mu) * t / self.mass)
		z2 = 5.0 * self.mass / self.b(self.radius, self.mu)
		z3 = self.g * self.mass**2 / (self.b(self.radius, self.mu)**2)
		z4 = -self.g * self.mass * t / self.b(self.radius, self.mu)
		v =  (zo + z1) * e + z2 + z3 + z4
		velocity.append(v)


if __name__=="__main__":

	C = calc()
	v = C.euler_vel()[1]
	for i in range(len(v)):
		print(v[i])
