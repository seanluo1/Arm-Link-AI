# geometry.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains geometry functions that relate with Part1 in MP2.
"""

import math
#import numpy as np
from const import *

def computeCoordinate(start, length, angle):
    """Compute the end cooridinate based on the given start position, length and angle.

        Args:
            start (tuple): base of the arm link. (x-coordinate, y-coordinate)
            length (int): length of the arm link
            angle (int): degree of the arm link from x-axis to couter-clockwise

        Return:
            End position of the arm link, (x-coordinate, y-coordinate)
    """
    angleInRadians = math.radians(angle)
    changeInX = math.cos(angleInRadians)*length
    changeInY = math.sin(angleInRadians)*length
    return (start[0]+changeInX, start[1]-changeInY)

def doesArmTouchObstacles(armPos, obstacles):
    """Determine whether the given arm links touch obstacles

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            obstacles (list): x-, y- coordinate and radius of obstacles [(x, y, r)]

        Return:
            True if touched. False it not.
    """

    for arm in armPos:

        yDist = arm[1][1]-arm[0][1] # y dist from end to end of each arm
        xDist = arm[1][0]-arm[0][0] # x dist from end to end of each arm

        x2y1 = arm[1][0]*arm[0][1]
        y2x1 = arm[1][1]*arm[0][0]
        yDistSquared = (yDist)**2
        xDistSquared = (xDist)**2
        distOfArm = math.sqrt(yDistSquared + xDistSquared) # length of arm

        for obst in obstacles:
            # law of cosines to find angles of triangle formulated by arm points and obstacle
            xDistObst = abs(arm[0][0] - obst[0])
            yDistObst = abs(arm[0][1] - obst[1])
            a = math.hypot(xDistObst, yDistObst)           # dist from start to obst
            xDistObst = abs(arm[1][0] - obst[0])
            yDistObst = abs(arm[1][1] - obst[1])
            b = math.hypot(xDistObst, yDistObst)           # dist from end to obst

            a2 = a**2
            b2 = b**2
            c2 = distOfArm**2

            alpha = math.acos((a2 - b2 - c2)/(-2*b*distOfArm))
            gamma = math.acos((b2 - a2 - c2)/(-2*a*distOfArm))

            alpha = math.degrees(alpha)
            gamma = math.degrees(gamma)

            endXDist = arm[1][0] - obst[0]
            endYDist = arm[1][1] - obst[1]

            # this is necessary for the case where the obstacle lies on the line
            if math.hypot(endXDist, endYDist) <= obst[2]:
                return True

            # check obstacles within range of segment (arm) length
            elif alpha <= 90 and gamma <= 90:
                distFromArmToObst = abs(yDist*obst[0] - xDist*obst[1] + x2y1 - y2x1) # calculates dist of obstacle to LINE
                distFromArmToObst /= distOfArm
                if distFromArmToObst < obst[2]:
                    return True

    return False

def doesArmTouchGoals(armEnd, goals):
    """Determine whether the given arm links touch goals

        Args:
            armEnd (tuple): the arm tick position, (x-coordinate, y-coordinate)
            goals (list): x-, y- coordinate and radius of goals [(x, y, r)]

        Return:
            True if touched. False it not.
    """
    for goal in goals:
        xDist = abs(armEnd[0] - goal[0]) # x and y distance of tick to center circle
        yDist = abs(armEnd[1] - goal[1])
        if math.hypot(xDist, yDist) <= goal[2]: # if the tip is within the goal circle, ret true
            return True
    return False


def isArmWithinWindow(armPos, window):
    """Determine whether the given arm stays in the window

        Args:
            armPos (list): start and end position of all arm links [(start, end)]
            window (tuple): (width, height) of the window

        Return:
            True if all parts are in the window. False it not.
    """
    for arm in armPos:
        if arm[0][0] > window[0] or arm[0][0] < 0:
            return False
        if arm[0][1] > window[1] or arm[0][1] < 0:
            return False
        if arm[1][0] > window[0] or arm[1][0] < 0:
            return False
        if arm[1][1] > window[1] or arm[1][1] < 0:
            return False
    return True
