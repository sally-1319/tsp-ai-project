distances = {
    'Nairobi': {
        'Meru': 210,
        'Nyeri': 150,
        'Nandi': 310,
        'Kericho': 290,
        'Nakuru': 160
    },
    'Meru': {
        'Nairobi': 210,
        'Nyeri': 120,
        'Nandi': 380,
        'Kericho': 360,
        'Nakuru': 250
    },
    'Nyeri': {
        'Nairobi': 150,
        'Meru': 120,
        'Nandi': 340,
        'Kericho': 320,
        'Nakuru': 180
    },
    'Nandi': {
        'Nairobi': 310,
        'Meru': 380,
        'Nyeri': 340,
        'Kericho': 90,
        'Nakuru': 130
    },
    'Kericho': {
        'Nairobi': 290,
        'Meru': 360,
        'Nyeri': 320,
        'Nandi': 90,
        'Nakuru': 110
    },
    'Nakuru': {
        'Nairobi': 160,
        'Meru': 250,
        'Nyeri': 180,
        'Nandi': 130,
        'Kericho': 110
    }
}
def route_distance(route, dist):
    return sum(dist[route[i]][route[i + 1]] for i in range(len(route) - 1))

from itertools import permutations

def brute_force_tsp(cities, dist):
    start = "Nairobi"
    other_cities = [city for city in cities if city != start]
    min_route, min_dist = None, float('inf')

    for perm in permutations(other_cities):
        route = [start] + list(perm) + [start]
        total = route_distance(route, dist)
        if total < min_dist:
            min_route, min_dist = route, total

    return min_route, min_dist


def nearest_neighbor_tsp(cities, dist):
    start = "Nairobi"
    unvisited = set(cities)
    unvisited.remove(start)
    route = [start]
    current = start
    total_dist = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: dist[current][city])
        total_dist += dist[current][next_city]
        route.append(next_city)
        current = next_city
        unvisited.remove(current)

    total_dist += dist[current][start]
    route.append(start)
    return route, total_dist

import random, math

def simulated_annealing(route, dist, T=1000, alpha=0.995, stopping_T=1):
    current_route = route[:]
    best_route = route[:]
    current_cost = route_distance(current_route, dist)
    best_cost = current_cost

    while T > stopping_T:
        new_route = current_route[:]
        i, j = sorted(random.sample(range(1, len(route) - 2), 2))
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_cost = route_distance(new_route, dist)
        if new_cost < current_cost or math.exp((current_cost - new_cost) / T) > random.random():
            current_route = new_route
            current_cost = new_cost
            if new_cost < best_cost:
                best_route = new_route
                best_cost = new_cost
        T *= alpha

    return best_route, best_cost

cities = list(distances.keys())

# Brute Force
bf_route, bf_cost = brute_force_tsp(cities, distances)
print("Brute Force:", bf_route, "Cost:", bf_cost)

# Nearest Neighbor
nn_route, nn_cost = nearest_neighbor_tsp(cities, distances)
print("Nearest Neighbor:", nn_route, "Cost:", nn_cost)

# Simulated Annealing (starting from NN route)
sa_route, sa_cost = simulated_annealing(nn_route, distances)
print("Simulated Annealing:", sa_route, "Cost:", sa_cost)

