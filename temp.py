INF = float('inf')

def add_to_queue(queue, tpl):
    path, g_cost, f_cost = tpl
    for i in range(len(queue)):
        if f_cost >= queue[i][-1]:
            queue.insert(i, tpl)
            break
    else:
        queue.append(tpl)


def calculate_tsp(city_map, starting_point):
    total_cities = len(city_map)
    queue = [([starting_point], 0, 0)]
    minimum_cost = INF
    shortest_path = []

    while queue:
        path, cost, heuristic = queue.pop(0)
        current_city = path[-1]
        if len(path) == total_cities:
            cost += city_map[current_city][starting_point]
            if cost < minimum_cost:
                minimum_cost = cost
                shortest_path = path + [starting_point]
        else:
            for neighbor_city in range(total_cities):
                if city_map[current_city][neighbor_city] and neighbor_city not in path:
                    g_cost = cost + city_map[current_city][neighbor_city]
                    h_cost = calculate_remaining_mst(city_map, path + [neighbor_city])
                    f_cost = g_cost + h_cost
                    add_to_queue(queue, (path + [neighbor_city], g_cost, f_cost))

    return shortest_path, minimum_cost


def calculate_remaining_map(city_map, path):
    total_cities = len(city_map)
    new_map = [[0 if i in path[1:-1] or j in path[1:-1] else city_map[i][j] for i in range(total_cities)] for j in range(total_cities)]
    return new_map


def calculate_remaining_mst(city_map, path):
    total_cities = len(city_map)
    remaining_cities = total_cities - len(path[1:-1])
    city_map = calculate_remaining_map(city_map, path)
    selected = [False for i in range(total_cities)]
    selected[path[0]] = True

    cost = 0
    count = 0
    for i in range(remaining_cities-1):
        minimum = INF
        a, b = 0, 0
        for i in range(total_cities):
            if selected[i]:
                for j in range(total_cities):
                    if not selected[j] and city_map[i][j]:
                        if minimum > city_map[i][j]:
                            minimum = city_map[i][j]
                            a, b = i, j
        cost += city_map[a][b]
        selected[b] = True
        count += 1
        return cost


if __name__=="__main__":
    city_map = [
        [0, 12, 10, 19, 8],
        [12, 0, 3, 7, 6],
        [10, 3, 0, 2, 20],
        [19, 7, 2, 0, 4],
        [8, 6, 20, 4, 0]
    ]
    ans = calculate_tsp(city_map, 0)
    print("TSP Route using A* : ", end="")
    print(*ans[0], sep="->")
    print("Cost of the Route :", ans[1])