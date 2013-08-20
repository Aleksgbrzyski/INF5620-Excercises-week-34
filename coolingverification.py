from cooling import *

t, T = cooling(T0 = 20, k = 1, T_s = 25, t_end = 10, dt = 2, theta = 1)

plot(t, T)
