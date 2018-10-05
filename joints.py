class joint:
    def __init__(self,type_of_joint, axis,limints,connection):
        self.type_of_joint = type_of_joint  # 0 - revolute; 1 - prismatic
        self.axis = axis                    # x - 0; y - 1; z - 2;
        self.limints = limints              # [max, min]
        self.connections = connection       # [parent, child]

    def get_parent(self):
        return self.connections[1]