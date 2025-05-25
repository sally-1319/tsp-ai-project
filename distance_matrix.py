import openrouteservice
import pprint

# Your OpenRouteService API key
API_KEY = "5b3ce3597851110001cf6248003d912fee2b424e92335888a836dcc7"

client = openrouteservice.Client(key=API_KEY)

# Coordinates of towns [longitude, latitude]
towns = {
    "Nairobi": [36.8219, -1.2921],
    "Meru": [37.6498, 0.0471],
    "Nyeri": [36.9476, -0.4197],
    "Nandi": [35.1130, 0.2136],
    "Kericho": [35.2831, -0.3677],
    "Nakuru": [36.0800, -0.3031]
}

locations = list(towns.values())

# Get distance matrix (in meters)
matrix = client.distance_matrix(
    locations=locations,
    profile='driving-car',
    metrics=['distance'],
    resolve_locations=True
)

print("Distance matrix (meters):")
pprint.pprint(matrix['distances'])

print("\nIndex mapping of towns:")
for i, town in enumerate(towns.keys()):
    print(f"{i}: {town}")

# Optional: convert to kilometers and print
dist_km = [[round(d/1000, 2) for d in row] for row in matrix['distances']]
print("\nDistance matrix (kilometers):")
pprint.pprint(dist_km)
