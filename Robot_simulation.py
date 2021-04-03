import random
import math

robots = []
class Robot:
    def __init__(self, name, points, success_rate, minimum_points = 0):
        self.name = name
        self.success_rate = success_rate
        self.points = points
        self.minimum_points = minimum_points
        self.wins = 0
        self.win_chance = 0
        robots.append(self)

    def __repr__(self):
        return repr((self.name, self.success_rate, self.points, self.wins, self.win_chance))


# Ordered based on seeding bracket                              # Seed
Los_Altos = Robot("Los Altos", 878, 0.5)                        # 1
Guardians = Robot("Guardians of the Garden Grove", 186, 0.875)  # 16

Noble = Robot("Noble", 204, 0.375)                              # 8
Tron = Robot("CWKA Tron", 292, 0.625)                           # 9

DRS = Robot("Dead Robot Society", 601, 0.625)                   # 4
Malden_Cath = Robot("Malden Cath", 234, 0.375)                  # 13

Hanalani = Robot("Hanalani", 342, 0.5)                          # 5 
Joker = Robot("Joker", 255, 0.5)                                # 12

Unic = Robot("HTL Unic", 672, 0.75)                             # 2
Crane = Robot("CWKA Crane", 201, 0.5)                           # 15

Malden = Robot("Malden", 309, 0.5)                              # 7
EPost = Robot("Explorer Post 1010", 286, 0.625)                 # 10

Radiant = Robot("Radiant HT", 633, 0.5)                         # 3
G_Force = Robot("G-Force", 212, 0.625)                          # 14

Warriors = Robot("Warriors", 317, 0.375)                        # 6
Incredibots = Robot("Incredibots", 280, 0.875)                  # 11






"""
# Smaller Tournament

Warriors = Robot("Warriors", 317, 0.375)
Incredibots = Robot("Incredibots", 280, 0.875)

Radiant = Robot("Radiant HT", 633, 0.5)
G_Force = Robot("G-Force", 212, 0.625)




# Demonstration robots

RobotA = Robot("Robot A", 200, 0.25)
RobotB = Robot("Robot B", 100, 0.5)
RobotC = Robot("Robot C", 50, 0.75)
RobotD = Robot("Robot D", 250, 0.125)
"""

# Battles robot1 and robot2. Returns True if robot1 wins and False if robot2 wins.
def battle(robot1, robot2):
    using_redo_method = True
    if random.random() < robot1.success_rate:
        points_scored1 = robot1.points
    else:
        points_scored1 = robot1.minimum_points
    if random.random() < robot2.success_rate:
        points_scored2 = robot2.points
    else:
        points_scored2 = robot2.minimum_points
    if points_scored1 == points_scored2:
        if using_redo_method:
            return(battle(robot1, robot2))
        else:
            if(random.randint(0, 1) == 0):
                return True
            else:
                return False
    return(points_scored1 > points_scored2)
 

def do_tournament_between(tourneyRobots):
    winners = tourneyRobots.copy()
    #random.shuffle(winners)
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
    tourney_robots = robots.copy()
    for robot in tourney_robots:
            robot.wins = 0
    for i in range(0, 10000000):
        winner = do_tournament_between(tourney_robots)
        for robot in tourney_robots:
            if robot.name == winner:
                robot.wins += 1
        total_tournaments += 1
    for robot in tourney_robots:
        win_chance = int(robot.wins / total_tournaments * 1000000) / 10000
        robot.win_chance = win_chance
    tourney_robots.sort(key=lambda roboguy: roboguy.win_chance, reverse=True)
    
    for robot in tourney_robots:
        print(robot.name + " win chance: " + str(robot.win_chance) + "%")

    print()
    print("Finished code!")


main()

