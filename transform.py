
# transform.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains the transform function that converts the robot arm map
to the maze.
"""
import copy
from arm import Arm
from maze import Maze
from search import *
from geometry import *
from const import *
from util import *

def transformToMaze(arm, goals, obstacles, window, granularity):
    """This function transforms the given 2D map to the maze in MP1.

        Args:
            arm (Arm): arm instance
            goals (list): [(x, y, r)] of goals
            obstacles (list): [(x, y, r)] of obstacles
            window (tuple): (width, height) of the window
            granularity (int): unit of increasing/decreasing degree for angles

        Return:
            Maze: the maze instance generated based on input arguments.
    """
    # set maze size
    armRanges = arm.getArmLimit()
    # Col = (alpha range)/granularity + 1
    alphaRange = armRanges[0]
    cols = (alphaRange[1]-alphaRange[0])/granularity + 1
    # Row = (beta range)/granularity + 1
    betaRange = armRanges[1]
    rows = (betaRange[1]-betaRange[0])/granularity + 1

    minAngleValues = []
    minAngleValues.append(armRanges[0][0])
    minAngleValues.append(armRanges[1][0])

    startAngles = arm.getArmAngle()

    # create Maze map
    mazeMap = []
    alpha = minAngleValues[0]
    beta = minAngleValues[1]

    for alpha in range(alphaRange[0], alphaRange[1]+1, granularity):
        rowMap = []
        for beta in range(betaRange[0], betaRange[1]+1, granularity):
            arm.setArmAngle((alpha, beta))
            armPos = arm.getArmPos()
            armEnd = arm.getEnd()
            # check is its the start
            if alpha == startAngles[0] and beta == startAngles[1]:
                rowMap.append('P')
            elif doesArmTouchObstacles(armPos, obstacles) or not isArmWithinWindow(armPos, window):
                rowMap.append('%')
            elif doesArmTouchGoals(armEnd, goals):
                rowMap.append('.')
            else:
                rowMap.append(' ')
        mazeMap.append(rowMap)

    # initialize Maze
    transformedMaze = Maze(mazeMap, minAngleValues, granularity)

    return transformedMaze
