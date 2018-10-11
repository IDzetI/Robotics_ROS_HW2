import numpy as np
import math


# Calculates Rotation Matrix given angles
def eulerAnglesToRotationMatrix(angles):
    R_x = np.array([[1, 0, 0],
                    [0, math.cos(angles[0]), -math.sin(angles[0])],
                    [0, math.sin(angles[0]), math.cos(angles[0])]
                    ])

    R_y = np.array([[math.cos(angles[1]), 0, math.sin(angles[1])],
                    [0, 1, 0],
                    [-math.sin(angles[1]), 0, math.cos(angles[1])]
                    ])

    R_z = np.array([[math.cos(angles[2]), -math.sin(angles[2]),0],
                    [math.sin(angles[2]), math.cos(angles[2]),0],
                    [0, 0, 1],
                    ])

    return np.dot(R_x, np.dot(R_y, R_z))


# Calculates Rotation Matrix given euler angles X Y X.
def eulerAnglesXYXToRotationMatrix(angles):
    R_x = np.array([[1, 0, 0],
                    [0, math.cos(angles[0]), -math.sin(angles[0])],
                    [0, math.sin(angles[0]), math.cos(angles[0])]
                    ])

    R_y = np.array([[math.cos(angles[1]), 0, math.sin(angles[1])],
                    [0, 1, 0],
                    [-math.sin(angles[1]), 0, math.cos(angles[1])]
                    ])

    R_x2 = np.array([[1, 0, 0],
                    [0, math.cos(angles[2]), -math.sin(angles[2])],
                    [0, math.sin(angles[2]), math.cos(angles[2])]
                    ])

    return np.dot(R_x, np.dot(R_y, R_x2))

# Calculates Rotation Matrix given angles.
def eulerAnglesZYYToRotationMatrix(angles):
    R_z = np.array([[math.cos(angles[0]), -math.sin(angles[0]), 0],
                    [math.sin(angles[0]), math.cos(angles[0]), 0],
                    [0, 0, 1],
                    ])

    R_y = np.array([[math.cos(angles[1]), 0, math.sin(angles[1])],
                    [0, 1, 0],
                    [-math.sin(angles[1]), 0, math.cos(angles[1])]
                    ])

    R_y2 = np.array([[math.cos(angles[2]), 0, math.sin(angles[2])],
                    [0, 1, 0],
                    [-math.sin(angles[2]), 0, math.cos(angles[2])]
                    ])

    return np.dot(R_z, np.dot(R_y, R_y2))


# Calculates Rotation Matrix given euler angles Z Y Z.
def eulerAnglesZYZToRotationMatrix(angles):
    R_z = np.array([[math.cos(angles[0]), -math.sin(angles[0]), 0],
                    [math.sin(angles[0]), math.cos(angles[0]), 0],
                    [0, 0, 1],
                    ])

    R_y = np.array([[math.cos(angles[1]), 0, math.sin(angles[1])],
                    [0, 1, 0],
                    [-math.sin(angles[1]), 0, math.cos(angles[1])]
                    ])

    R_z2 = np.array([[math.cos(angles[2]), -math.sin(angles[2]), 0],
                    [math.sin(angles[2]), math.cos(angles[2]), 0],
                    [0, 0, 1],
                    ])

    return np.dot(R_z, np.dot(R_y, R_z2))


# Checks if a matrix is a valid rotation matrix.
def isRotationMatrix(R):
    shouldBeIdentity = np.dot(np.transpose(R), R)
    return np.linalg.norm(np.identity(3, dtype=R.dtype) - shouldBeIdentity) < 1e-6


# Calculates rotation matrix to euler angles X Y X
def RMatrixXYXToEulerAngles(R):
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[1, 0]**2 + R[2, 0]**2)

    if not sy < 1e-6:
        phi = math.atan2(R[1, 0], -R[2, 0])
        theta = math.atan2(sy,R[0, 0])
        psi = math.atan2(R[0, 1], R[0, 2])
    else:
        phi = math.atan2(R[2, 1], R[2, 2])
        theta = 0
        psi = 0

    return np.array([phi, theta, psi])

# Calculates rotation matrix to euler angles Z Y Z
def RMatrixZYZToEulerAngles(R):
    assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 2]**2 + R[1, 2]**2)

    if not sy < 1e-6:
        phi = math.atan2(R[1, 2], R[0, 2])
        theta = math.atan2(sy,R[2, 2])
        psi = math.atan2(R[2, 1], -R[2, 0])
    else:
        phi = math.atan2(R[0, 1], R[0, 0])
        theta = 0
        psi = 0

    return np.array([phi, theta, psi])
