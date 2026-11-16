Web VPython 3.2

#canvas(background=color.white)

import random

box(pos=vec(0, 0, 0.4), size=vec(1,1,0.1), texture="https://static.wikia.nocookie.net/p__/images/0/0f/Usagi.png/revision/latest?cb=20250724170841&path-prefix=protagonist")
cylinder(pos=vec(0, 0.2, 0.45), axis=vec(0,0.3,0), size=vec(0.5,0.4,0.4))
h = cylinder(pos=vec(0.25,-0.25,0.5), color=vec(0.6,0.4,0.3), size=vec(0.3,0.1,0.1), axis = vec(0,0,1))
p = cylinder(pos=vec(0.25,-0.25,0.8), color=vec(0.6,0.4,0.3), size=vec(1,0.05,1), axis = vec(0,0,1))

x = compound([h, p])

y = ellipsoid(pos=vec(0.25, 1, 1.3), size=vec(0.04, 0.3, 0.3), axis=vec(0,1,0), color=color.yellow, emissive=True)
w = cylinder(pos=vec(0.25, 0.98, 1.3), size=vec(0.025, 0.6, 0.6), axis=vec(0,1,0), emissive=True)

e = compound([y, w])

g = vec(0, -9.8, 0)

e.v = vec(0, 0, 0)
dt = 0.01

#e.pos = e.pos + e.v * dt

#e.v = e.v + g * dt

while True :
    rate(100)
    e.pos = e.pos + e.v *dt
    if e.pos.y <= -0.18 : 
        e.v.y = -e.v.y
    e.v = e.v + g * dt
    
    if e.pos.y <= 0.1 :
        for i in range(10) : 
            rate(500)
            e.color=vec(i/9,i/9,i/9)
    else :
        e.color=color.white
