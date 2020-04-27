from glumpy import app
from vpython import *
from math import cos, sin, pi
from numpy import arange

"""s = sphere(pos = vector(1, 0, 0), radius=0.1, make_trail=True)
for theta in arange(0, 10*pi, 0.1):
    rate(30)
    x = cos(theta)
    y = sin(theta)
    s.pos = [x, y, 0]"""

window = app.Window()

@window.event
def on_draw(dt):
    window.clear()

app.run()
