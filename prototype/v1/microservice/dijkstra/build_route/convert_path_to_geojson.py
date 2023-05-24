def convert(path):
    polyline_for_ymap = []

    for el in path:
        new_list = el.split("|")
        longitude = float(new_list[0])
        latitude = float(new_list[1])
        polyline_for_ymap.append([latitude, longitude])

    return polyline_for_ymap
