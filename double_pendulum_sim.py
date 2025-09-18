"""
source of formula: https://web.mit.edu/jorloff/www/chaosTalk/double-pendulum/double-pendulum-en.html

this a double pendulum simulation from the use of mechanical energy, applied to lagragian equation. This website provides a step by step guide of how the lagragian equation is derived for the double pendulum.
"""
import pygame as pg
from math import *

pg.init()

w,h=800,600
win=pg.display.set_mode((w,h))
fps=100

# mass 1
l1=100 # length
t1=pi/2 # angle
m1=25 # mass
v1=0 # angular velocity
a1=0 # angular acceleration

# mass 2
l2=100
t2=pi/2
m2=25
v2=0
a2=0

# another pendulum with a very slight change in position, causing a drastic change due to the double pendulum's chaotic nature
L1=100
T1=pi/2+.0001
M1=30
W1=0
A1=0

L2=100
T2=pi/2+.0001
M2=30
W2=0
A2=0

# origin point for the pendulum position
x=w/2
y=h/2

# gravity
g=9.8/fps

run=True
clock=pg.time.Clock()
while run:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            run=False
    win.fill((0,0,0))

    # theta 1
    num1=-g*(2*m1+m2)*sin(t1)-m2*g*sin(t1-2*t2)-2*sin(t1-t2)*m2*(v2**2*l2+v1**2*l1*cos(t1-t2))
    den1=l1*(2*m1+m2-m2*cos(2*t1-2*t2))
    a1=num1/den1

    # theta 2
    num2=2*sin(t1-t2)*(v1**2*l1*(m1+m2)+g*(m1+m2)*cos(t1)+v2**2*l2*m2*cos(t1-t2))
    den2=l2*(2*m1+m2-m2*cos(2*t1-2*t2))
    a2=num2/den2

    # change of angular velocity
    v1+=a1
    v2+=a2

    # change of angle
    t1+=v1
    t2+=v2


    # second pendulum
    den=(2*M1+M2-M2*cos(2*T1-2*T2))
    NUM1=-g*(2*M1+M2)*sin(T1)-M2*g*sin(T1-2*T2)-2*sin(T1-T2)*M2*(W2**2*L2+W1**2*L1*cos(T1-T2))
    DEN1=L1*den
    A1=NUM1/DEN1

    NUM2=2*sin(T1-T2)*(W1**2*L1*(M1+M2)+g*(M1+M2)*cos(T1)+W2**2*L2*M2*cos(T1-T2))
    DEN2=L2*den
    A2=NUM2/DEN2


    W1+=A1
    W2+=A2
    T1+=W1
    T2+=W2


    # postions for both pendulums
    x1,y1=(l1*sin(t1)+x,l1*cos(t1)+y)
    x2,y2=(l2*sin(t2)+x1,l2*cos(t2)+y1)
  
    X1,Y1=(L1*sin(T1)+x,L1*cos(T1)+y)
    X2,Y2=(L2*sin(T2)+X1,L2*cos(T2)+Y1)


    # second pendulum
    pg.draw.line(win,(255,255,255),(x,y),(X1,Y1))
    pg.draw.line(win,(255,255,255),(X1,Y1),(X2,Y2))
    pg.draw.circle(win,(0,255,0),(X1,Y1),M1)
    pg.draw.circle(win,(0,0,255),(X2,Y2),M2)

    # first pendulum
    pg.draw.line(win,(255,255,255),(x,y),(x1,y1))
    pg.draw.line(win,(255,255,255),(x1,y1),(x2,y2))
    pg.draw.circle(win,(255,0,0),(x1,y1),m1)
    pg.draw.circle(win,(0,255,0),(x2,y2),m2)


    pg.display.update()
    clock.tick(fps)
    
pg.quit()
