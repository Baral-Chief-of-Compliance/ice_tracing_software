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


def enter_path(path):
    for el in path:
        new_list = el.split("|")
        longitude = float(new_list[0])
        latitude = float(new_list[1])
        geo_json["features"][0]["geometry"]["coordinates"].append([longitude, latitude])

    with open("pathICE1.json", "w") as file:
        json.dump(geo_json, file)
