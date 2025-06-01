import openrouteservice
import time
import pprint

locations = {
    0: "-1.286389,36.817223",  # Nairobi
    1: "0.0463,37.6559",       # Meru
    2: "-0.4167,36.95",        # Nyeri
    3: "0.1037,34.8911",       # Nandi
    4: "-0.3675,35.2833",      # Kericho
    5: "-0.3031,36.0800",      # Nakuru
}

city_list = list(locations.keys())
API_KEY = "5b3ce3597851110001cf6248003d912fee2b424e92335888a836dcc7"
client = openrouteservice.Client(key=API_KEY)

distance_cache = {}

def get_distance_matrix():
    size = len(locations)
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            key = (city_list[i], city_list[j])
            if key in distance_cache:
                dist = distance_cache[key]
            else:
                try:
                    coords = [
                        list(map(float, locations[city_list[i]].split(',')))[::-1],  # lon, lat
                        list(map(float, locations[city_list[j]].split(',')))[::-1]
                    ]
                    res = client.directions(
                        coordinates=coords,
                        profile='driving-car',
                        format='geojson'
                    )
                    dist = res['features'][0]['properties']['segments'][0]['distance'] / 1000  # km
                    distance_cache[key] = dist
                    time.sleep(1)  # avoid rate limiting
                except Exception as e:
                    print(f"❌ Error fetching distance for {key}: {e}")
                    dist = 1e6  # large value to discourage impossible paths
            matrix[i][j] = dist

    print("✅ Distance Matrix:")
    pprint.pprint(matrix)
    return matrix
