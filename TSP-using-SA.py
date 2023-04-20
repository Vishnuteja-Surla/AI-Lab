import random
import math
import numpy as np
import matplotlib.pyplot as plt

class City:
    
    def __init__(self):
        self.x = random.randint(1,9)
        self.y = random.randint(1,9)
        
    def get_city(self):
        return [self.x, self.y]

cities = []
        
while len(cities) != 15:
    new_city = City()
    if new_city.get_city() not in cities:
        cities.append(new_city.get_city())
        

def dist_bw_cities(city1, city2):
    x_diff = city1[0] - city2[0]
    y_diff = city1[1] - city2[1]
    x_diff = x_diff**2
    y_diff = y_diff**2
    dist = x_diff + y_diff
    dist = math.sqrt(dist)
    return dist
    
path = []

start_city = random.choice(cities)
path.append(start_city)

while len(path) != 15:
    rand_city = random.choice(cities)
    if rand_city not in path:
        path.append(rand_city)
        
        
def total_distance(path):
    dist = 0
    for i in range(0,14):
        dist += dist_bw_cities(path[i], path[i+1])
    return dist

best_distance = total_distance(path)

data = np.array(path)
plt.plot(data[:, 0], data[:, 1], marker="o")
plt.show()

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

T = 1e+10
gamma = 0.97
T0 = 1

def simulated_annealing(T, T0, gamma, path, best_distance):
    iteration = 0
    it_list = []
    cost_list = []
    while T > T0:
        path_copy = path.copy()
        select_cities = random.sample(range(0,15), 2)
        swapPosition(path_copy, select_cities[0], select_cities[1])
        
        new_dist = total_distance(path_copy)
        
        if new_dist <= best_distance:
            path = path_copy.copy()
            best_distance = new_dist
        else:
            factor = math.exp((new_dist - best_distance)*-1/T)
            v = random.random()
            if v<= factor:
                path = path_copy.copy()
                best_distance = new_dist
        
        iteration += 1
        it_list.append(iteration)
        cost_list.append(best_distance)
        T *= gamma
        
    x_axis = np.array(it_list)
    y_axis = np.array(cost_list)
    plt.plot(x_axis, y_axis)
    plt.xlabel("Iteration")
    plt.ylabel("Best Distance")
    plt.show()
    return [path, best_distance]
        
ans = simulated_annealing(T, T0, gamma, path, best_distance)
print("Path : ", ans[0])
print("Best Distance : ", ans[1])