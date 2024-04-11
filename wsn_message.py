from enum import Enum

BROADCAST = -1

WSNMessageType = Enum("WSNMessage", ("Data", "Advertisement"))

class WSNMessage:
    def __init__(self, src=None, dest=None, message_type=None, data=None, src_link=None, dest_link=None):
        self.src = src
        self.dest = dest
        self.src_link = src_link
        self.dest_link = dest_link
        self.type = WSNMessageType[message_type]
        self.data = data
    
    # Check if self is the forwarded message of m
    def is_forward_of(self, m):
        if (WSNMessageType.Data == m.type and 
            self.type == m.type and
            self.src == m.src and
            self.dest == m.dest and
            self.dest_link == m.src_link and
            self.data == m.data):
            return True
        return False
    
    def __str__(self):
        ret = 'src : '+str(self.src) + ", "
        ret += 'dest : '+str(self.dest) + ", "
        ret += 'message_type : '+str(self.type) + ", "
        ret += 'data : '+str(self.data) + ", "
        ret += 'src_link : '+str(self.src_link) + ", "
        ret += 'dest_link : '+str(self.dest_link)
        return ret

    def __eq__(self, other):
        return isinstance(other, WSNMessage) and\
                all([getattr(self, attr) == getattr(other, attr) for attr in vars(self)])
