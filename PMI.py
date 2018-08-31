"""
This script is to compute the PMI given input strings.

It will be refactored in the future. Currently it computes the PMI matrix
"""

import numpy as np
import math


def splitStrings(inputList):
    return np.array([list(i) for i in inputList])


def buildDict(inputList):
    return np.unique(inputList)


def buildDictIndices(inputList):
    tokenDict = buildDict(inputList)
    dictIndex = dict(((el, el1), 0) for el in tokenDict for el1 in tokenDict)
    return dictIndex


def wordCountList(inputList, dictIndex, cWin=1):
    numV = len(dictIndex)
    countMatrix = np.zeros((numV, numV))
    for i in inputList:
        leni = len(i)
        for j in range(leni):
            wWin = i[max(0, j-cWin):min(leni, j+cWin+1)]
            unique, count = np.unique(wWin, return_counts=True)
            uniquek = len(unique)
            for k in range(uniquek):
                countMatrix[dictIndex[i[j]]][dictIndex[unique[k]]] += count[k]
            countMatrix[dictIndex[i[j]]][dictIndex[i[j]]] -= 1
    return countMatrix


def computeTot(countMatrix):
    countSum = 0
    for i in countMatrix:
        countSum += np.sum(i)
    return countSum


def computeJoint(countMatrix):
    tots = computeTot(countMatrix)
    return [[countMatrix[i][j]/tots for j in range(len(countMatrix))]
            for i in range(len(countMatrix))]


def computeMarg1(countMatrix):
    tots = computeTot(countMatrix)
    return [np.sum(i)/tots for i in countMatrix]


def computePMI(countMatrix):
    numV = len(countMatrix)
    PMIMatrix = np.zeros((numV, numV))
    tots = computeTot(countMatrix)
    marg = [np.sum(i) for i in countMatrix]
    for i in range(numV):
        for j in range(numV):
            eij = countMatrix[i][j]*tots/marg[i]/marg[j]
            PMIMatrix[i][j] = round(math.log(eij), 2) if eij > 0 else 0
    return PMIMatrix
