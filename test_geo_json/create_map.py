import folium


url = ("http://127.0.0.1:5000")

m = folium.Map(location=[45.5236, -122.6750], zoom_start=9)

folium.GeoJson(url, name="geojson").add_to(m)

m.save("map.html")