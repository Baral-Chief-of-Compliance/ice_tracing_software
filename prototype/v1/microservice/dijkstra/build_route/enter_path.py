import json

geo_json = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [],
        "type": "LineString"
      }
    }
  ]
}

polyline_for_ymap = []


def enter_path(path):
    for el in path:
        new_list = el.split("|")
        longitude = float(new_list[0])
        latitude = float(new_list[1])
        polyline_for_ymap.append([latitude, longitude])
        geo_json["features"][0]["geometry"]["coordinates"].append([longitude, latitude])

    with open("data/pathArc7.json", "w") as file:
        json.dump(polyline_for_ymap, file)

    with open("data/pathArc7_map_box.json", "w") as file:
        json.dump(geo_json, file)
