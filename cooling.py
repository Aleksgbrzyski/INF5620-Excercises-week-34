from numpy import *
from scitools.std import *

def cooling(T0, k, T_s, t_end, dt, theta=0.5):

    N = int(t_end/float(dt))
    t = zeros(N+1)
    T = zeros(N+1)
    t[0] = 0
    T[0] = T0

    for n in range(N):
        T[n+1] = ((1 - (1 - theta)*k*dt)*T[n] + k*dt*T_s)/float(1+k*dt*theta)
        t[n+1] = t[n] + dt

    return t, T
