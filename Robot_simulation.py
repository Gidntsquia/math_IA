import random
import math

robots = []
class Robot:
    def __init__(self, name, success_rate, points, minimum_points = 0):
        self.name = name
        self.success_rate = success_rate
        self.points = points
        self.minimum_points = minimum_points
        robots.append(self)



DRS = Robot("DRS", 0.5, 100)
Rockville = Robot("Rockville", 0.8, 50)
Epost = Robot("Epost", 0.33, 500)
Items = Robot("Items", 0.7, 1000)


# Battles robot1 and robot2. Returns True if robot1 wins and False if robot2 wins.
def battle(robot1, robot2):
    if random.randint(1, 100) < robot1.success_rate * 100:
        points_scored1 = robot1.points
    else:
        points_scored1 = robot1.minimum_points
    
    
    if random.randint(1, 100) < robot2.success_rate * 100:
        points_scored2 = robot2.points
    else:
        points_scored2 = robot2.minimum_points
    if points_scored1 == points_scored2:
        if(random.random() >= 0.5):
            return True
        else:
            return False
    return(points_scored1 > points_scored2)
 

def do_tournament_between(robots):
    winners = []
    losers = []
    #for i in range(0, int(math.log2(robots.count())) + 1):

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
    total_tournaments = 0
    robot_to_track = "Rockville"
    tourney_robots = robots
    robot_wins = 0
    for i in range(0,10000):
        if do_tournament_between(tourney_robots) == robot_to_track:
            robot_wins += 1
        total_tournaments += 1

    print(robot_to_track + " win chance: " + str(robot_wins / total_tournaments))
    print()
    print("Finished code!")


main()

