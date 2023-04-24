import json


geojson = {
  "type": "FeatureCollection",
  "features": []
}


def create_geojson(map_, width, length):
    for y in range(width):
        for x in range(length):
            if map_[y][x] != '.':
                if map_[y][x]["type"] == "young":
                    geojson["features"].append(
                        {
                            "type": "Feature",
                            "properties": {
                                "marker-color": "#e212ab",
                                "marker-size": "small"
                            },
                            "geometry": {
                                "coordinates": [
                                    map_[y][x]["longitude"],
                                    map_[y][x]["latitude"]
                                ],
                                "type": "Point"
                            }
                        }
                    )

    with open("geo_json_young_ice.json", "w") as file:
        json.dump(geojson, file)

