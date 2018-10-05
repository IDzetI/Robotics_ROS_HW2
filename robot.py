import numpy as np

class robot:
    def __init__(self,links,joints):
        self.links = links
        self.joints = joints

    def get_link_translation(self,number):
        for link in self.links:
            if link.origin_frame == number:
                return link.lenght
        return np.zeros(3)

    def get_joint_asix(self,number):
        for joint in self.joints:
            if joint.connections[0] == number:
                return joint.axis
        return np.zeros(3)

    def get_links(self):
        return self.links

    def get_joints(self):
        return self.joints

    def get_parent(self,number):
        for joint in self.joints:
            if joint.connections[0] == number:
                return joint.get_parent()
        return -1

    def check_limit(self, number_of_joint,value):
        for joint in self.joints:
            if joint.connections[0] == number_of_joint:
                if value < joint.limints[0]:
                    return joint.limints[0]
                else:
                    if value > joint.limints[1]:
                        return joint.limints[1]
                    else: return value
        return value