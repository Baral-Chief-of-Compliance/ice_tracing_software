def format_polygons(polygons):
    coords = []
    for polygon in polygons["features"]:
        polygon_coords = []

        for el in polygon["geometry"]["coordinates"][0]:
            long, lat = el[0], el[1]
            polygon_coords.append([lat, long])
        coords.append(polygon_coords)

    return coords
