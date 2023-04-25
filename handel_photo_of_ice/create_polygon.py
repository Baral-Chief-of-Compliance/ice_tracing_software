def crete_list_coords(map_, y_start, x_start, list_coords, width, height):
    coords = [map_[y_start][x_start]["longitude"], map_[y_start][x_start]["latitude"]]
    list_coords.append(coords)

    if y_start == 0:
        if x_start == 0:
            if map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

        elif x_start == width - 1:
            if map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start-1] != '.' and map_[y_start + 1][x_start-1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        else:
            if map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start - 1] != '.' and map_[y_start + 1][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

    elif y_start == height - 1:

        if x_start == 0:
            if map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

        elif x_start == width - 1:

            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        else:

            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

    elif x_start == 0:
        if y_start == 0:
            if map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

        else:
            if map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

    elif x_start == width - 1:
        if y_start == 0:
            if map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start-1] != '.' and map_[y_start + 1][x_start-1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        else:
            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start - 1] != '.' and map_[y_start + 1][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

    else:
        if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

        elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

        elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

        elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

        elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

        elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

        elif map_[y_start + 1][x_start - 1] != '.' and map_[y_start + 1][x_start - 1]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

        elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == "young":
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)


def clean_map(map_, width, height):

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for y in range(height):
        for x in range(width):
            if map_[y][x] != '.':
                if map_[y][x]["type"] == "young":
                    list_cords = []
                    crete_list_coords(map_, y, x, list_cords, width, height)
                    list_cords.append(list_cords[0])
                    geojson["features"].append({
                        "type": "Feature",
                        "properties": {
                            "stroke": "#e50bde",
                            "stroke-width": 2,
                            "stroke-opacity": 1,
                            "fill": "#e60a8a",
                            "fill-opacity": 0.5
                        },
                        "geometry": {
                            "coordinates": [list_cords],
                            "type": "Polygon"
                        }
                    })

    # list_cords.append(list_cords[0])
    return geojson
