from distances import distances

def greedy_tsp(distances, start_city):
    unvisited = set(distances.keys())
    unvisited.remove(start_city)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(unvisited, key=lambda city: distances[current_city].get(city, float('inf')))
        tour.append(next_city)
        unvisited.remove(next_city)
        current_city = next_city

    # Return to start
    tour.append(start_city)
    return tour

def calculate_total_distance(tour, distances):
    total = 0
    for i in range(len(tour) - 1):
        frm = tour[i]
        to = tour[i+1]
        total += distances[frm][to]
    return total

if __name__ == "__main__":
    start = 'Nairobi'
    route = greedy_tsp(distances, start)
    total_dist = calculate_total_distance(route, distances)

    print("Greedy TSP route:")
    print(" -> ".join(route))
    print(f"\nTotal distance: {total_dist:.2f} km")    