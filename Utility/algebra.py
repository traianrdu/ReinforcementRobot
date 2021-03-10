import math


def findD(xA, xB, yA, yB):
    """Finds the distance between 2 points"""
    d = math.sqrt(pow(xB - xA, 2) + pow(yB-yA, 2))
    return d


def findX(distance, xA, yA, yB):
    """find the xB"""
    xB = xA + math.sqrt(pow(distance, 2) - pow(yB-yA, 2))
    return xB
