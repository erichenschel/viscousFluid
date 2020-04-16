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
import pandas as pd

class calc:

    def __init__(self):
        self.step = 0.01 # -- time step
        self.mass = 1.0 #kg -- mass
        self.g = 9.81 #m/s/s -- gravity
        
        self.vo = 5.0 #m/s -- initial velocity
        self.yo = 0.0 #m -- initial position
        self.to = 0.0 #s -- initial time
        
        self.density = 1000 #kg/m3 -- density of water
        self.mu = 8.9 * 10**(-4) #Pa s -- viscosity (water at 25 deg celsius)
        self.radius = 0.01 #m (1 cm) -- radius
    
    # coeff
    def b(self):
        return (6 * np.pi) * self.mu * self.radius
    
    # y'' = f(v) = acceleration (changed return to addition from subtraction)
    def f(self, v):
        zo = self.b() * v / self.mass
        return (-self.g + zo)

    # velocity calculated with Euler
    def euler_vel(self):
        time = [self.to]
        vel = [self.vo]
        
        for i in range(75):
            v = vel[i]
            a = self.f(v)
            vn = v + a * self.step
            
            if vn <=0:
                vel.append(0)
            else:
                vel.append(vn)

            time.append(self.step*float(i+1))
        
        return time, vel
            
    # position calculated with Euler
    def euler_pos(self, v):
        pos = [self.yo]
        
        for i in range(75):
            y = pos[i]
            f = v[i]
            yn = y + f * self.step
            pos.append(yn)
        
        return pos

    # analytical position model 
    def pos(self, t):
        position = []
        
        for i in range(len(t)):
            zo = (-5.0) * self.mass / self.b()
            z1 = -self.g * (self.mass**2) / (self.b()**2)
            
            e = np.exp(-self.b() * t[i] / self.mass)
            z2 = (5.0 * self.mass) / self.b()
            z3 = (self.g * self.mass**2) / (self.b()**2)
            z4 = (-self.g * self.mass * t[i]) / self.b()
            
            y = ((zo + z1) * e + z2 + z3 + z4)
            
            if y<=0:            
                position.append(0)
            else:
                position.append(y)
        
        return position

    # analytical velocity model
    def vel(self, t):
        velocity = []
        
        for i in range(len(t)):
            zo = (-5.0) * self.mass / self.b()
            z1 = -self.g * (self.mass**2) / (self.b()**2)
            z2 = (-self.b()/self.mass)
            
            e = np.exp(-self.b() * t[i] / self.mass)
            z3 = -self.g * self.mass / self.b()
            
            v = (zo + z1) * z2 * e + z3
            
            if v<=0:
                velocity.append(0)
            else:
                velocity.append(v)
        
        return velocity

    # euler error eval
    def euler_err(self):
        t = self.euler_vel()[0]
        vel = self.vel(t)
        pos = self.pos(t)
        
        v = self.euler_vel()[1]
        y = self.euler_pos(v)

        df = pd.DataFrame({'time': t, 'Velocity': v, 'Euler_vel': vel})
        e_y = []
        e_v = []
        
        for i in range(df.shape[0]):
            e_v.append(np.abs(df['Velocity'][i]-df['Euler_vel'][i]))
        
        df['Euler_vel_err'] = e_v
        df['Position'] = pos
        df['Euler_pos'] = y
        
        for i in range(df.shape[0]):
            e_y.append(np.abs(df['Position'][i]-df['Euler_pos'][i]))
        
        df['Euler_pos_err'] = e_y
        
        return df
    
    # quality control
    def rk_vel(self):
        time = [self.to]
        vel = [self.vo]
        
        for i in range(75):
            v = vel[i]
            vn = v + self.f(v+self.step*self.f(v)) * self.step
            if vn<=0:
                vel.append(0)
            else:
                vel.append(vn)
        
        return vel
    
    # re-examine this function
    def rk_pos(self, v):
        time = [self.to]
        pos = [self.yo]
        
        for i in range(75):
            y = pos[i]
            a = v[i]
            yn = y + a * self.step
            pos.append(yn)
        
        return pos

    #rk error eval
    def rk_err(self):
        t = self.euler_vel()[0]
        vel = self.vel(t)
        pos = self.pos(t)
        
        v = self.rk_vel()
        y = self.rk_pos(v)
        
        df = pd.DataFrame({'time': t, 'Velocity': vel, 'rk_vel': v})
        e_y = []
        e_v = []
        
        for i in range(df.shape[0]):
            e_v.append(np.abs(df['Velocity'][i]-df['rk_vel'][i]))
        
        df['rk_vel_error'] = e_v
        df['Position'] = pos
        df['rk_pos'] = y
        
        for i in range(df.shape[0]):
            e_y.append(np.abs(df['Position'][i]-df['rk_pos'][i]))
        
        df['rk_pos_err'] = e_y
        
        return df


if __name__=="__main__":
    C = calc()
    print(C.euler_err())
    print(C.rk_err())
