# search.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Jongdeog Lee (jlee700@illinois.edu) on 09/12/2018

"""
This file contains search functions.
"""
# Search should return the path and the number of states explored.
# The path should be a list of tuples in the form (alpha, beta, gamma) that correspond
# to the positions of the path taken by your search algorithm.
# Number of states explored should be a number.
# maze is a Maze object based on the maze from the file specified by input filename
# searchMethod is the search method specified by --method flag (bfs,dfs,greedy,astar)
# You may need to slight change your previous search functions in MP1 since this is 3-d maze
import queue
import math
from queue import deque
def search(maze, searchMethod):
    return {
        "bfs": bfs,
    }.get(searchMethod, [])(maze)

def bfs(maze):
    num_states_explored = 0
    path = [] # returns path taken
    explored = [] # keeps track of where we've been
    q = queue.Queue()
    start = maze.getStart()
    dots = maze.getObjectives() # dots holds all the points we need to get to
    parentDict = {} # map that allows us to trace back our path

    q.put(start)
    while dots: # while dots is not empty
        current = q.get()
        flag = False
        # check if reached a dot
        for dot in range(len(dots)):
            if dots[dot] == current:
                num_states_explored += 1
                flag = True
        if flag:
             break
        neighbors = maze.getNeighbors(current[0], current[1])
        for neighbor in neighbors:
            if (maze.isValidMove(neighbor[0], neighbor[1])) and (neighbor not in explored):
                q.put(neighbor) # push unvisted neighbors into queue
                explored.append(neighbor) # mark neighbors as visited
                parentDict[neighbor] = current # keep track of path
        num_states_explored = num_states_explored + 1 # increment steps taken

    # at this point, we've reached all the goals
    backwardsPath = deque() # stack
    backwardsPath.append(current)
    while current != start: # add path in reverse order from goal to start
        current = parentDict[current]
        backwardsPath.append(current)
    backwardsPath.append(start)
    while backwardsPath: # push stack items into path for correct order path
        path.append(backwardsPath.pop())

    return path, num_states_explored
