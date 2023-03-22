# Implement Wumpus World Environment in Python
score = 0

class World:
    def __init__(self):
        self.world = [
            [[],['B'],['P'],['B']],
            [['S'],[],['B'],[]],
            [['W'],['S','B','G'],['P'],['B']],
            [['S'],[],['B'],['P']]
        ]
        self.wumpus = True
        self.final_loc = [0,0]
        self.wumpus_loc = [2,0]

    def print_world(self):
        for i in range(len(self.world)):
            for j in range(len(self.world[i])):
                print(self.world[i][j], end=' ')
            print()

class Agent:
     
     def __init__(self):
        self.current_loc = [0,0]
        self.alive = True
        self.exit = False
        self.arrow = True
        self.gold = False
        self.actions = ['North', 'South', 'East', 'West', 'Shoot', 'Climb']
        self.sensors = {
            'Stench': False, 'Breeze': False, 'Glitter': False, 'Bump': False
            }


if __name__=="__main__":
    
    world = World()
    agent = Agent()

    print("                                                 Welcome the Wumpus World!                                                                       ")
    print()
    print("Rules:-")
    print("The Wumpus World is a 4x4 grid world with 3 pits, 1 Wumpus, 1 Gold and 1 Exit.")
    print("The Agent can move in 4 directions: North, South, East and West.")
    print("The Agent can shoot an arrow in 4 directions: North, South, East and West but can only shoot once.")
    print("The Agent can climb out of the Wumpus World if he is in the Exit with the Gold.")
    print("The Agent can die if he falls into a pit or is eaten by the Wumpus.")
    print("The Agent can sense the Stench, Breeze, Glitter and Bump.")

    while not agent.exit and agent.alive:
        print()
        print("Current Location: ", agent.current_loc)
        print("Current Score: ", score)
        print("Current Sensors: ", agent.sensors)
        print("Current Actions: ", agent.actions)
        print()
        action = input("Enter your action: ")
        if action not in agent.actions:
            print("Invalid Action")
            continue
        else:
            if action == 'North':
                agent.current_loc[0] = agent.current_loc[0]-1
            
            elif action == 'South':
                agent.current_loc[0] = agent.current_loc[0]+1
            
            elif action == 'East':
                agent.current_loc[1] = agent.current_loc[1]+1
            
            elif action == 'Climb':
                if agent.current_loc == world.final_loc and agent.gold:
                    print("You climbed out of the Wumpus World!")
                    agent.exit = True
                    score = score+1000
                else:
                    print("You can't climb out of the Wumpus World!")
            
            elif action == 'Shoot':
                if agent.arrow:
                    print("Enter the direction in which you want to shoot the arrow: ")
                    shoot_dir = input()
                    if shoot_dir == 'North':
                        if world.world[agent.current_loc[0]-1][agent.current_loc[1]] == ['W']:
                            print("You killed the Wumpus!")
                            world.wumpus = False
                            score = score+1000
                        else:
                            print("You missed the Wumpus!")
                            score = score-10
                    elif shoot_dir == 'South':
                        if world.world[agent.current_loc[0]+1][agent.current_loc[1]] == ['W']:
                            print("You killed the Wumpus!")
                            world.wumpus = False
                            score = score+1000
                        else:
                            print("You missed the Wumpus!")
                            score = score-10
                    elif shoot_dir == 'East':
                        if world.world[agent.current_loc[0]][agent.current_loc[1]+1] == ['W']:
                            print("You killed the Wumpus!")
                            world.wumpus = False
                            score = score+1000
                        else:
                            print("You missed the Wumpus!")
                            score = score-10
                    elif shoot_dir == 'West':
                        if world.world[agent.current_loc[0]][agent.current_loc[1]-1] == ['W']:
                            print("You killed the Wumpus!")
                            world.wumpus = False
                            score = score+1000
                        else:
                            print("You missed the Wumpus!")
                            score = score-10
                    else:
                        print("Invalid Direction!")
                    agent.arrow = False
                else:
                    print("You can't shoot the arrow again!")

                if not world.wumpus:
                    world.world[world.wumpus_loc[0]][world.wumpus_loc[1]] = []
            
            else:
                agent.current_loc[1] = agent.current_loc[1]-1

            if agent.current_loc[0]<0 or agent.current_loc[1]<0 or agent.current_loc[0]>3 or agent.current_loc[1]>3:
                print("You hit the wall!")
                if agent.current_loc[0]<0:
                    agent.current_loc[0] = agent.current_loc[0]+1
                elif agent.current_loc[1]<0:
                    agent.current_loc[1] = agent.current_loc[1]+1
                elif agent.current_loc[0]>3:
                    agent.current_loc[0] = agent.current_loc[0]-1
                else:
                    agent.current_loc[1] = agent.current_loc[1]-1
                agent.sensors['Bump'] = True
            else:
                agent.sensors['Bump'] = False

            if 'G' in world.world[agent.current_loc[0]][agent.current_loc[1]]:
                print("You found the Gold!")
                agent.gold = True
                agent.sensors['Glitter'] = True
                score = score+1000
            else:
                agent.sensors['Glitter'] = False

            if 'W' in world.world[agent.current_loc[0]][agent.current_loc[1]]:
                print("You found the Wumpus!")
                agent.alive = False
                print("You are Dead!")
                score = score-1000
            else:
                agent.sensors['Stench'] = False

            if 'P' in world.world[agent.current_loc[0]][agent.current_loc[1]]:
                print("You found a Pit!")
                agent.alive = False
                print("You are Dead!")
                score = score-1000
            else:
                agent.sensors['Breeze'] = False

            if 'S' in world.world[agent.current_loc[0]][agent.current_loc[1]]:
                agent.sensors['Stench'] = True
            else:
                agent.sensors['Stench'] = False

            if 'B' in world.world[agent.current_loc[0]][agent.current_loc[1]]:
                agent.sensors['Breeze'] = True
            else:
                agent.sensors['Breeze'] = False


    print("Final Score: ", score)
    print("Thanks for playing!")