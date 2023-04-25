def crete_list_coords(map_, y_start, x_start, list_coords, width, height, type_of_ice):
    coords = [map_[y_start][x_start]["longitude"], map_[y_start][x_start]["latitude"]]
    list_coords.append(coords)

    if y_start == 0:
        if x_start == 0:
            if map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

        elif x_start == width - 1:
            if map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start-1] != '.' and map_[y_start + 1][x_start-1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

        else:
            if map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start - 1] != '.' and map_[y_start + 1][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

    elif y_start == height - 1:

        if x_start == 0:
            if map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

        elif x_start == width - 1:

            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

        else:

            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

    elif x_start == 0:
        if y_start == 0:
            if map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

        else:
            if map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

    elif x_start == width - 1:
        if y_start == 0:
            if map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start-1] != '.' and map_[y_start + 1][x_start-1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

        else:
            if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

            elif map_[y_start + 1][x_start - 1] != '.' and map_[y_start + 1][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height, type_of_ice)

            elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)

    else:
        if map_[y_start - 1][x_start - 1] != '.' and map_[y_start - 1][x_start - 1]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height, type_of_ice)

        elif map_[y_start - 1][x_start] != '.' and map_[y_start - 1][x_start]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height, type_of_ice)

        elif map_[y_start - 1][x_start + 1] != '.' and map_[y_start - 1][x_start + 1]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height, type_of_ice)

        elif map_[y_start][x_start + 1] != '.' and map_[y_start][x_start + 1]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height, type_of_ice)

        elif map_[y_start + 1][x_start + 1] != '.' and map_[y_start + 1][x_start + 1]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height, type_of_ice)

        elif map_[y_start + 1][x_start] != '.' and map_[y_start + 1][x_start]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height, type_of_ice)

        elif map_[y_start + 1][x_start - 1] != '.' and map_[y_start + 1][x_start - 1]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height, type_of_ice)

        elif map_[y_start][x_start - 1] != '.' and map_[y_start][x_start - 1]["type"] == type_of_ice:
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height, type_of_ice)


def clean_map(map_, width, height, type_of_ice):

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for y in range(height):
        for x in range(width):
            if map_[y][x] != '.':
                if map_[y][x]["type"] == type_of_ice:
                    list_cords = []
                    crete_list_coords(map_, y, x, list_cords, width, height, type_of_ice)
                    list_cords.append(list_cords[0])
                    geojson["features"].append({
                        "type": "Feature",
                        "properties": {
                            "stroke": "#00C8A1",
                            "stroke-width": 2,
                            "stroke-opacity": 1,
                            "fill": "#00C8A1",
                            "fill-opacity": 0.5
                        },
                        "geometry": {
                            "coordinates": [list_cords],
                            "type": "Polygon"
                        }
                    })

    # list_cords.append(list_cords[0])
    return geojson
