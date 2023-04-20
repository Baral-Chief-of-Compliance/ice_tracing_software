import folium
import json
import requests


ports_url = "http://127.0.0.1:5000/ports"

response = requests.get(ports_url)
ports = response.json()

coords_ports = {
    "type": "FeatureCollection",
    "features": []
}


for p in ports:
    inf = ports.get(p)
    coords_ports["features"].append({
        "type": "Feature",
        "properties": {},
        "geometry": {
            "coordinates": inf.get("coordinates"),
            "type": "Point"
        }
    })


json_ports = json.dumps(coords_ports)
print(json_ports)

map = folium.Map(location=[68.970663, 33.074918], zoom_start=5)

folium.GeoJson(json_ports, name="geojson").add_to(map)


map.save("./templates/index.html")
