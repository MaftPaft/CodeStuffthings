"""
This forces_kinematics calculator finds the unknown variables when given at least 3 variables (None for unknown parameters)

the equation is chosen and rearanged based on what variables are given, and what the unknowns are.

the output gives you answers for each unknown if possible


for example:

A 1580kg car is traveling with a speed of 15m/s. What is the net force that is required to bring the car to a halt in a distance of 50.0m?

mass=1580
Fnet=None
acceleration=None
time=None
displacement=50
initial_velocity=15
final_velocity=0

for solutions in kinematic_solver(time,displacement,acceleration,initial_velocity,final_velocity,Fnet,mass):
    print(solutions)

output:
[2.0689655172413794, 'acceleration', 'v2=v1+at']
[121.8, 'displacement', 'd=(v1+v2)/2*t']   
[3268.9655172413795, 'Fnet', 'Fnet=mass*acc']
"""
import math

def e1(v2,v1,a,t):
    if [v2,v1,a,t].count(None) ==1:
        if v2==None:
            return [v1+a*t,"final_velocity","v2=v1+at"]
        elif v1==None:
            return [v2-a*t,"initial_velocity","v2=v1+at"]
        elif a==None:
            return [(v2-v1)/t,"acceleration","v2=v1+at"]
        elif t==None:
            return [(v2-v1)/a,"time","v2=v1+at"]
def e2(d,t,v1,a):
    if [d,t,v1,a].count(None)==1:
        if t==None:
            #d=v1t+1/2a(t^2) -> 1/2a(t^2)+v1t-d=0
            # quadratic formula --> (-v1 +- sqrt[ v1^2 - 4(1/2a)(-d) ])/a
            root=math.sqrt(v1**2-4*(a/2)*(-d)) 
            t1=(-v1+root)/a
            t2=(-v1-root)/a
            return [t1 if t1>t2 else t2, "time","d=v1t+1/2(t^2)"]
        elif d==None:
            return [v1*t + a/2 * (t**2), "displacement","d=v1t+1/2a(t^2)"]
        elif v1==None:
            # v1t + a/2*t^2
            # d=v1t+1/2a(t^2)
            # (d-(1/2a*t^2))/t
            return [(d-(a/2*(t**2)))/t,"initial_velocity","d=v1t+1/2a(t^2)"]
        elif a==None:
            # (d-v1t)/t^2*2
            # d=v1t+1/2a(t^2)
            # (d-v1t)/(t**2)*2=1/2a(t^2)
            return [(d-v1*t)/(t**2)*2,"acceleration","d=v1t+1/2a(t^2)"]
def e3(d,t,v2,a):
    if [d,t,v2,a].count(None)==1:
        if t==None:
            root=math.sqrt(v2**2-4*(-a/2)*(-d))
            t1=(-v2+root)/a
            t2=(-v2-root)/a
            return [t1 if t1>t2 else t2, "time","d=v2t-1/2a(t^2)"]
        elif d==None:
            return [v2*t - a/2 * (t**2), "displacement","d=v2t-1/2a(t^2)"]
        elif v2==None:
            # v2t - a/2*t^2
            # d=v2t-1/2a(t^2)
            # (d+(1/2a(t^2)))/t
            return [(d+(a/2*(t**2)))/t,"final_velocity","d=v2t-1/2a(t^2)"]
        elif a==None:
            # d=v2t-1/2a(t^2)
            # (d-v2t)/(t**2)*-2=a
            return [(d-v2*t)/(t**2)*-2,"acceleration","d=v2t-1/2a(t^2)"]
def e4(d,v1,v2,t):
    if [d,v1,v2,t].count(None) ==1:
        if d==None:
            return [(v1+v2)/2*t,"displacement","d=(v1+v2)/2*t"]
        elif v1==None:
            #d=(v1+v2)/2*t
            #d*2/t-v2=v1
            return [d*2/t-v2,"initial_velocity","d=(v1+v2)/2*t"]
        elif v2==None:
            #d*2/t=v1+v2
            #d*2/t-v1=v2
            return [d*2/t-v1,"final_velocity","d=(v1+v2)/2*t"]
        elif t==None:
            #d=(v1+v2)/2*t
            
            return [2*d/(v1+v2),"time","d=(v1+v2)/2*t"]
def e5(v2,v1,a,d): #v2^2=v1^2+2ad
    if [v2,v1,a,d].count(None)==1:
        if v2==None:
            return [math.sqrt(v1**2+2*a*d),"final_velocity","v2^2=v1^2+2ad"]
        elif v1==None:
            return [math.sqrt(v2**2-2*a*d),"initial_velocity","v2^2=v1^2+2ad"]
        elif a==None:
            return [(v2**2-v1**2)/(2*d),"acceleration","v2^2=v1^2+2ad"]
        elif d==None:
            return [(v2**2-v1**2)/(2*a),"displacement","v2^2=v1^2+2ad"]
        


def f1(mass,acceleration,Fnet):
    if [mass,acceleration,Fnet].count(None)==1:
        if mass==None:
            return [Fnet/acceleration,"mass","mass=Fnet/acc"]
        elif acceleration==None:
            return [Fnet/mass,"acc","acc=Fnet/mass"]
        elif Fnet==None:
            return [mass*acceleration,"Fnet","Fnet=mass*acc"]

def kinematic_solver(time=None,displacement=None,acceleration=None,initial_velocity=None,final_velocity=None,Fnet=None,mass=None):
    """
    set the parameter to None if it is unknown

    returns a list of 2 lists giving 3 items:
     - the value of the missing variable
     - the name of the missing variable
     - what type of equation was used
    """
    solved=[]
    f=f1(mass,acceleration,Fnet)
    if f:
        if "acc" in f:
            acceleration=f[0]
            solved.append(f)
    
    Big5=[
        e1(final_velocity,initial_velocity,acceleration,time), # v2=v1+at
        e2(displacement,time,initial_velocity,acceleration),#d=v1t+1/2a(t^2)
        e3(displacement,time,final_velocity,acceleration), #d=v2t-1/2a(t^2)
        e4(displacement,initial_velocity,final_velocity,time), #d=(v1+v2)/2*t
        e5(final_velocity,initial_velocity,acceleration,displacement) # v2^2=v1^2+2ad
    ]
    for i in Big5:
        if i:
            if "acceleration" in i:
                acceleration=i[0]
            solved.append(i)
    
    forces=f1(mass,acceleration,Fnet)
    if forces: solved.append(forces)
    
    return solved

mass=1580
Fnet=None
acceleration=None
time=None
displacement=50
initial_velocity=15
final_velocity=0

for solutions in kinematic_solver(time,displacement,acceleration,initial_velocity,final_velocity,Fnet,mass):
    print(solutions)
