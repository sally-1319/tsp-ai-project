from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from Distances import get_distance_matrix, city_list

def solve_tsp_with_ortools(distance_matrix):
    size = len(distance_matrix)
    manager = pywrapcp.RoutingIndexManager(size, 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(i, j):
        return int(distance_matrix[manager.IndexToNode(i)][manager.IndexToNode(j)] * 1000)  # meters

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_params = pywrapcp.DefaultRoutingSearchParameters()
    search_params.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solution = routing.SolveWithParameters(search_params)
    if solution is None:
        raise Exception("❌ OR-Tools failed to find a solution.")

    route = []
    index = routing.Start(0)
    total_distance = 0

    while not routing.IsEnd(index):
        node_index = manager.IndexToNode(index)
        route.append(city_list[node_index])
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)

    route.append(city_list[manager.IndexToNode(index)])  # return to start
    return route, total_distance / 1000  # km


if __name__ == "__main__":
    print("🚀 Starting TSP Route Optimization...")
    matrix = get_distance_matrix()
    route, total_dist = solve_tsp_with_ortools(matrix)
    print("\n✅ Optimal Route:")
    print(" → ".join(route))
    print(f"🛣️  Total Distance: {total_dist:.2f} km")
