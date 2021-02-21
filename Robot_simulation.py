import random
import math

robots = []
class Robot:
    def __init__(self, name, consistency, points, minimum_points):
        self.name = name
        self.consistency = consistency
        self.points = points
        self.minimum_points = minimum_points
        robots.append(self)



DRS = Robot("DRS", 0.5, 100, 0)
Rockville = Robot("Rockville", 0.8, 50, 25)
Epost = Robot("Epost", 0.33, 500, 0)
Items = Robot("Items", 0.7, 1000, 0)


# Battles robot1 and robot2. Returns True if robot1 wins and False if robot2 wins.
def battle(robot1, robot2):
    if random.randint(1, 100) < robot1.consistency * 100:
        points_scored1 = robot1.points
    else:
        points_scored1 = robot1.minimum_points
    
    
    if random.randint(1, 100) < robot2.consistency * 100:
        points_scored2 = robot2.points
    else:
        points_scored2 = robot2.minimum_points
    print(robot1.name + " points: " + str(points_scored1))
    print(robot2.name + " points: " + str(points_scored2))
    if points_scored1 == points_scored2:
        return("Tie")
    return(points_scored1 > points_scored2)
 
winners = []
losers = []
def do_tournament_between(robots):
    winners = []
    losers = []
    for robot in range(0, len(robots), 2):
        # Adds winning robot to the winning list and losers to the losers list.
        if battle(robots[robot], robots[robot + 1]):
            winners.append(robots[robot])
            losers.append(robots[robot + 1])
        else:
            winners.append(robots[robot + 1])
            losers.append(robots[robot])
    if battle(winners[0], winners[1]):
        return(winners[0].name)
    else:
        return(winners[1].name)



def main():
    print("Starting code!")
    print()
    
    for i in range(0,5):
        print("The winner of the tournament: " + do_tournament_between(robots))
        
    
    print()
    print("Finished code!")


main()
