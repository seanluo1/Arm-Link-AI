# Arm-Link-AI
This was one of my projects in my Artificial Intelligence course. It plays a game where you navigate around obstacles to reach a goal with the robot arm. It uses BFS to find an optimal path to the goal.

Pygame must be installed to run the game. Z and X move the first link, A and S move the second link.
To play the game, run
"python mp2.py --map BasicMap --human"
where BasicMap can be replaced with Map1, Map2, Map3, and Map4.

To watch the AI play the game, run
"python mp2.py --map BasicMap --trajectory 1 --method bfs --granularity 1"
Note that granularity is the angle that the arm moves when a key is pressed. I recommended using 1 so that the AI can navigate through tight spaces. Trajectory traces the path that the AI takes, smaller numbers will give more refined traces. Note that Map3 is unsolveable and has no possible solution.
