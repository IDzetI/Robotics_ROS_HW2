import math
import numpy as np

from euler_angles import eulerAnglesZYZToRotationMatrix, RMatrixZYZToEulerAngles, eulerAnglesXYXToRotationMatrix, \
    RMatrixXYXToEulerAngles
from kinematics import forward_kinematics, inverse_kinematics
from joints import joint
from links import link
from robot import robot
from util import deg_to_rad

links = [link(np.array([0,0,287]),0),
         link(np.array([-180,0,70]),1),
         link(np.array([0, 0, 370]),2),
         link(np.array([0, 0, 179.5]),3),
         link(np.array([0, 0, 256]), 4),
         link(np.array([0, 0, 124]), 5)]

joints = [joint(0, np.array([0,0,1]), [-180,180], [0,1]),
          joint(0, np.array([0,1,0]), [-138,64], [1,2]),
          joint(0, np.array([0,1,0]), [-124, 124], [2, 3]),
          joint(0, np.array([0,0,1]), [-180, 180], [3, 4]),
          joint(0, np.array([0,1,0]), [-140, 141], [4, 5]),
          joint(0, np.array([0,0,1]), [-math.inf, math.inf], [5, -1])
          ]

arkodim = robot(links,joints)
T = forward_kinematics(np.array([deg_to_rad(45), deg_to_rad(-45), deg_to_rad(-45), deg_to_rad(45), deg_to_rad(0), deg_to_rad(-45)]), arkodim)
print ("T = ")
print (T)
print ()
q = inverse_kinematics(T)
print ("joints")
print ([i / math.pi * 180 for i in q])
print ()
T1 = forward_kinematics(np.array(q), arkodim)
print ("T1 = ")
print (T1)
print ()
#print(np.matmul(T,np.array([0,0,0,1]))[0:3])
print ()
print ()
pi = math.pi
angles  = [-pi/3,pi/6,pi/2]
'''
R = eulerAnglesXYXToRotationMatrix(angles)
print(R)
print()
print(angles)
print(RMatrixXYXToEulerAngles(R))
'''