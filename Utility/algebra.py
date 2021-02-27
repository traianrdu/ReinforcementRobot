import math


def findX(distance, xA, yA, yB):
    """find the xB"""
    xB = xA + math.sqrt(pow(distance, 2) - pow(yB-yA, 2))
    return xB
