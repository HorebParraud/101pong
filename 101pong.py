#!/usr/bin/env python3

from sys  import argv, stderr
from math import fabs, sqrt, atan, pow, degrees, acos

if len(argv) != 8:
        stderr.write("Bad numbers of argument.\n")
        exit (84)
if int(argv[7]) < 0:
        stderr.write("Bad time shift.\n")
        exit (84)
try:
        x0 = float(argv[1])
        y0 = float(argv[2])
        z0 = float(argv[3])
        x1 = float(argv[4])
        y1 = float(argv[5])
        z1 = float(argv[6])
        n  = int(argv[7])
except ValueError:
        stderr.write("Bad type of argument.\n")
        exit (84)

velocity_x = x1 - x0
velocity_y = y1 - y0
velocity_z = z1 - z0
coordi_n_x = velocity_x * n + x1
coordi_n_y = velocity_y * n + y1
coordi_n_z = velocity_z * n + z1
velocity   = sqrt(pow(velocity_x, 2) + pow(velocity_y, 2) + pow(velocity_z, 2))
if velocity == 0:
        incid_angle = 0
else:
        incid_angle = abs(90 - degrees(acos(velocity_z / velocity)))

print("The velocity vector of the ball is:")
print("(%.2f, %.2f, %.2f)" %(velocity_x, velocity_y, velocity_z))
print("At time t + ", n,", ball coordinates will be:")
print("(%.2f, %.2f, %.2f)" %(coordi_n_x, coordi_n_y, coordi_n_z))

if (z1 >= 0 and velocity_z < 0) or (z1 < 0 and velocity_z >= 0):
        print("The incidence angle is:")
        print("%.2f" % incid_angle, "degrees")
else:
        print("The ball won't reach the bat.")
exit (0)
