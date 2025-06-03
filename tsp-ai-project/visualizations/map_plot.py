import folium
import os
import webbrowser
from folium import plugins
from project.TSP import solve_tsp_with_ortools
from data.locations import city_list, locations, get_distance_matrix

def visualize_route(route):
    m = folium.Map(location=[-0.1, 37.0], zoom_start=7)

    # Mark all cities on map
    for city in city_list:
        lat, lon = map(float, locations[city].split(','))
        folium.Marker([lat, lon], popup=city, icon=folium.Icon(color='green')).add_to(m)

    # Convert route indices to coordinates
    coords = [list(map(float, locations[int(city)].split(','))) for city in route]

    # Add animated route line
    plugins.PolyLineTextPath(
        folium.PolyLine(coords, color="blue", weight=5, opacity=0.9).add_to(m),
        '➔',
        repeat=True,
        offset=7,
        attributes={'fill': 'blue', 'font-weight': 'bold', 'font-size': '18'}
    ).add_to(m)

    # Add numbered markers for the route
    for i, city in enumerate(route):
        lat, lon = map(float, locations[int(city)].split(','))
        folium.Marker(
            location=[lat, lon],
            icon=folium.DivIcon(
                html=f"""<div style="font-size: 12px; color: white; background:blue; border-radius:50%; padding:4px;">{i+1}</div>"""
            )
        ).add_to(m)

    # Save and open the map
    file_path = "tsp_ortools_map.html"
    m.save(file_path)
    print("✅ Map saved to tsp_ortools_map.html")

    # Open in Google Chrome
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    abs_file_path = os.path.abspath(file_path)
    try:
        webbrowser.get(chrome_path).open(f"file://{abs_file_path}")
        print("🌐 Opening map in Chrome...")
    except webbrowser.Error as e:
        print(f"❌ Could not open Chrome: {e}")
