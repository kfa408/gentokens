import gentoken as gt
import PMI
import numpy as np


Obj1 = gt.dummyObj(0.85, 'a')
Obj2 = gt.dummyObj(0.15, 'b')
rngObj = gt.generateObj(5000, Obj1, Obj2)
rngObj1 = gt.generateObj(5000, Obj1, Obj2)
rngObj2 = gt.generateObj(5000, Obj1, Obj2)
tokenStrList = [gt.generateIs(i) for i in rngObj]
tokenStrList += [gt.generaterel(rngObj1[i], rngObj2[i]) for i in range(5000)]
splittedTokens = PMI.splitStrings(tokenStrList)
countMatrix = PMI.wordCountList(splittedTokens, cWin=2)
PMIM = PMI.computePMI(countMatrix)
print(PMIM)
