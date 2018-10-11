from scipy.optimize import fsolve

import robot
import numpy as np
import math
from euler_angles import *

#solve forward kinematics fo robot
def forward_kinematics(q, r):
    k = 0
    T = np.eye(4)
    while k != -1:
        R = eulerAnglesToRotationMatrix(r.get_joint_asix(k) * r.check_limit(k, q[k]))
        P = np.transpose(r.get_link_translation(k))
        H = np.zeros((4, 4))

        for i in range(3):
            for j in range(3):
                H[j][i] = R[j][i]
            H[i][3] = P[i]
        H[3][3] = 1

        T = np.matmul(T, H)
        k = r.get_parent(k)
    return T

#calculate matrix T03
def T03(q):
    global d
    y = np.empty(3)

    s1 = math.sin(q[0])
    c1 = math.cos(q[0])
    s2 = math.sin(q[1])
    c2 = math.cos(q[1])
    s3 = math.sin(q[2])
    c3 = math.cos(q[2])

    y[0] = (- 180 * c1 + 370 * c1 * s2 + 435.5 * (c1 * s2 * c3 + c1 * c2 * s3)) - d[0]
    y[1] = (- 180 * s1 + 370 * s1 * s2 + 435.5 * (s1 * s2 * c3 + s1 * c2 * s3)) - d[1]
    y[2] = (357 + 370 * c2 + 435.5 * (c2 * c3 - s2 * s3)) - d[2]
    return y

#solve invert kinematics fo robot
def inverse_kinematics(T):
    global d

    T0 = np.dot(T, np.linalg.inv(np.array([[1,0,0,0],[0,1,0,0],[0,0,1,124],[0,0,0,1]])))
    d = T0[0:3,3]
    q123 = fsolve(T03, [0, 0, 0])

    R03 = eulerAnglesZYYToRotationMatrix(q123)
    R36 = np.matmul(np.linalg.inv(R03),T0[0:3,0:3])
    q456 = RMatrixZYZToEulerAngles(R36)
    return [q123[0],q123[1],q123[2],q456[0],q456[1],q456[2]]


