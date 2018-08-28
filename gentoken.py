import numpy as np

class dummyObj(object):
    def __init__(self, prob1,objtype):
        self.prob1 = prob1
        self.objtype = objtype
    def getprob1(self):
        return self.prob1
    def getobjtype(self):
        return self.objtype

def generateObj(nums, dObj1, dObj2):
    rngObj = np.random.choice([dObj1,dObj2], nums)
    return rngObj

def generateIs(dObj):
#    return (dObj.getobjtype(), np.random.choice(['l','r'], p = [1. - dObj.getprob1(), dObj.getprob1()]))
    return dObj.getobjtype() + '$' + np.random.choice(['l','r'], p = [1. - dObj.getprob1(), dObj.getprob1()])

def generaterel(dObj1, dObj2):
    dObj1val = np.random.choice([-1,1], p = [1. - dObj1.getprob1(), dObj1.getprob1()])
    dObj2val = np.random.choice([-1,1], p = [1. - dObj2.getprob1(), dObj2.getprob1()])
#    if dObj1val > dObj2val:
#        return (dObj1val, ">", dObj2val)
#    elif dObj1val == dObj2val:
#        return (dObj1val, "=", dObj2val)
#    else:
#        return (dObj1val, "<", dObj2val)
    if dObj1val > dObj2val:
        return dObj1.getobjtype() + '>'+ dObj2.getobjtype()
    elif dObj1val == dObj2val:
        return dObj1.getobjtype() + '='+ dObj2.getobjtype()
    else:
        return dObj1.getobjtype() + '<'+ dObj2.getobjtype()
