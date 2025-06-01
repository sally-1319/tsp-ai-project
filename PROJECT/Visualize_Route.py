import folium
import os
import webbrowser
from folium import plugins
from TSP  import solve_tsp_with_ortools
from Distances import locations, city_list, get_distance_matrix

def visualize_route(route):
    m = folium.Map(location=[-0.1, 37.0], zoom_start=7)

    # Mark all cities
    for city in city_list:
        lat, lon = map(float, locations[city].split(','))
        folium.Marker([lat, lon], popup=city, icon=folium.Icon(color='green')).add_to(m)

    coords = [list(map(float, locations[city].split(','))) for city in route]

    # Add animated route polyline
    plugins.PolyLineTextPath(
        folium.PolyLine(coords, color="blue", weight=5, opacity=0.9).add_to(m),
        '➔',
        repeat=True,
        offset=7,
        attributes={'fill': 'blue', 'font-weight': 'bold', 'font-size': '18'}
    ).add_to(m)

    # Numbered markers along route
    for i, city in enumerate(route):
        lat, lon = map(float, locations[city].split(','))
        folium.Marker(
            location=[lat, lon],
            icon=folium.DivIcon(
                html=f"""<div style="font-size: 12px; color: white; background:blue; border-radius:50%; padding:4px;">{i+1}</div>"""
            )
        ).add_to(m)

    file_path = "tsp_ortools_map.html"
    m.save(file_path)
    print("✅ Map saved to tsp_ortools_map.html")

    # Open in Google Chrome (adjust path if needed)
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    abs_file_path = os.path.abspath(file_path)
    try:
        webbrowser.get(chrome_path).open(f"file://{abs_file_path}")
        print("🌐 Opening map in Chrome...")
    except webbrowser.Error as e:
        print(f"❌ Could not open Chrome: {e}")

if __name__ == "__main__":
    matrix = get_distance_matrix()
    route, total_dist = solve_tsp_with_ortools(matrix)
    print("\n✅ Optimal Route:")
    print(" → ".join(route))
    print(f"🛣️  Total Distance: {total_dist:.2f} km")
    visualize_route(route)
