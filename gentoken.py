import numpy as np

#dummy class with 1 discrete random variable on {-1,1}
#prob1 is the probability that an object is 1
#type should be changed to ID
class dummyObj(object):
    def __init__(self, prob1,objtype):
        self.prob1 = prob1
        self.objtype = objtype
    def getprob1(self):
        return self.prob1
    def getobjtype(self):
        return self.objtype

#generate a list of length nums
#uniformly choose between 2 dummy objects
def generateObj(nums, dObj1, dObj2):
    rngObj = np.random.choice([dObj1,dObj2], nums)
    return rngObj

#given a dummy object, generate an IS statement
def generateIs(dObj):
    return dObj.getobjtype() + '$' + np.random.choice(['l','r'], p = [1. - dObj.getprob1(), dObj.getprob1()])

#given two dummy objects, generate a relation statement
def generaterel(dObj1, dObj2):
    dObj1val = np.random.choice([-1,1], p = [1. - dObj1.getprob1(), dObj1.getprob1()])
    dObj2val = np.random.choice([-1,1], p = [1. - dObj2.getprob1(), dObj2.getprob1()])
    if dObj1val > dObj2val:
        return dObj1.getobjtype() + '>'+ dObj2.getobjtype()
    elif dObj1val == dObj2val:
        return dObj1.getobjtype() + '='+ dObj2.getobjtype()
    else:
        return dObj1.getobjtype() + '<'+ dObj2.getobjtype()
