import math
import numpy as np

from euler_angles import eulerAnglesXYXToRotationMatrix, RMatrixXYXToEulerAngles
from kinematics import forward_kinematics, inverse_kinematics
from joints import joint
from links import link
from robot import robot
from util import deg_to_rad

#set robot
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
r6Robot = robot(links, joints)

#forward forward_kinematics
T = forward_kinematics(np.array([deg_to_rad(45), deg_to_rad(-45), deg_to_rad(-45), deg_to_rad(45), deg_to_rad(0), deg_to_rad(-45)]), r6Robot)
print ("T = ")
print (T)
print ()

#inverse_kinematics
q = inverse_kinematics(T)
print ("joints")
print ([i / math.pi * 180 for i in q])
print ()

#check
T1 = forward_kinematics(np.array(q), r6Robot)
print ("T1 = ")
print (T1)
print ()

pi = math.pi
angles  = [-pi/3,pi/6,pi/2]
R = eulerAnglesXYXToRotationMatrix(angles)
print("euler angles = ")
print(angles)
print()
print("R matrix for X Y X =")
print(R)
print()
print("euler angles from R matrix= ")
print(RMatrixXYXToEulerAngles(R))