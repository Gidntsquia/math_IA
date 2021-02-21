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
Rockville = Robot("Rockville", 0.9, 50)
Epost = Robot("Epost", 0.33, 500)
Items = Robot("Items", 0.7, 1000)
Plainview = Robot("Plainview", 0.5, 300)
Unic = Robot("Unic", 0.6, 900)
Los_Altos = Robot("Los Altos", 0.7, 900)
Norman = Robot("Norman Advanced", 0.9, 300)



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
        battle(robot1, robot2)

    return(points_scored1 > points_scored2)
 

def do_tournament_between(tourneyRobots):
    winners = tourneyRobots.copy()
    random.shuffle(winners)
    while len(winners) > 1:
        for robot in range(0, int((len(winners)) / 2), 1):
            # Adds winning robot to the winning list and losers to the losers list.
            if battle(winners[robot], winners[robot + 1]):
                del winners[robot + 1]
                
            else:
                del winners[robot]
    return winners[0].name



def main():
    print("Starting code!")
    print()
    total_tournaments = 0
    robot_to_track = "Rockville"
    tourney_robots = robots.copy()
    robot_wins = 0
    for i in range(0, 100000):
        if do_tournament_between(tourney_robots) == robot_to_track:
            robot_wins += 1
        total_tournaments += 1
    win_chance = int(robot_wins / total_tournaments * 10000) / 100
    print(robot_to_track + " win chance: " + str(win_chance) + "%")
    print()
    print("Finished code!")


main()

