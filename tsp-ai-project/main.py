# main.py in C:\Users\kamau\tsp-ai-project

from data.locations import get_distance_matrix, city_list
from project.TSP import solve_tsp_with_ortools
from visualizations.map_plot import visualize_route

def main():
    print("🚀 Starting TSP Route Optimization...")

    # Get distance matrix from your locations data
    distance_matrix = get_distance_matrix()

    # Solve TSP using OR-Tools
    route, total_distance = solve_tsp_with_ortools(distance_matrix)

    print("\n✅ Optimal Route:")
    print(" → ".join(route))
    print(f"🛣️  Total Distance: {total_distance:.2f} km")

    # Visualize the route on a map
    visualize_route(route)

if __name__ == "__main__":
    main()
