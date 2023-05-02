def choose_color(type_of_ice):
    if type_of_ice == "old_ice":
        return "#900001"

    elif type_of_ice == "young_ice":
        return "#f708f9"

    elif type_of_ice == "first_year_ice":
        return "#00c8a1"

    elif type_of_ice == "nilas_ice":
        return "#0968f5"

    elif type_of_ice == "fast_ice":
        return "#fffafa"

    elif type_of_ice == "ice_field":
        return "#b9b1b1"


def crete_list_coords(map_, y_start, x_start, list_coords, type_of_ice):
    height = len(map_)
    width = len(map_[0])

    coords = [map_[y_start][x_start]["longitude"], map_[y_start][x_start]["latitude"]]
    list_coords.append(coords)

    if y_start == 0:
        if x_start == 0:
            if map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

        elif x_start == width - 1:
            if map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

        else:
            if map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

    elif y_start == height - 1:

        if x_start == 0:
            if map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

        elif x_start == width - 1:

            if map_[y_start - 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

        else:

            if map_[y_start - 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

    elif x_start == 0:
        if y_start == 0:
            if map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

        else:
            if map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start + 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

    elif x_start == width - 1:
        if y_start == 0:
            if map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

        else:
            if map_[y_start - 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

            elif map_[y_start + 1][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, type_of_ice)

            elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
                map_[y_start][x_start]["type_of_ice"] = ''
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)

    else:
        if map_[y_start - 1][x_start - 1]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, type_of_ice)

        elif map_[y_start - 1][x_start]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start - 1, x_start, list_coords, type_of_ice)

        elif map_[y_start - 1][x_start + 1]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, type_of_ice)

        elif map_[y_start][x_start + 1]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start, x_start + 1, list_coords, type_of_ice)

        elif map_[y_start + 1][x_start + 1]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, type_of_ice)

        elif map_[y_start + 1][x_start]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start + 1, x_start, list_coords, type_of_ice)

        elif map_[y_start + 1][x_start - 1]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, type_of_ice)

        elif map_[y_start][x_start - 1]["type_of_ice"] == type_of_ice:
            map_[y_start][x_start]["type_of_ice"] = ''
            return crete_list_coords(map_, y_start, x_start - 1, list_coords, type_of_ice)


def clean_map(map_, type_of_ice):

    height = len(map_)
    width = len(map_[0])

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for y in range(height):
        for x in range(width):
            if map_[y][x]["type_of_ice"] == type_of_ice:
                list_cords = []
                crete_list_coords(map_, y, x, list_cords, type_of_ice)
                list_cords.append(list_cords[0])
                geojson["features"].append({
                    "type": "Feature",
                    "properties": {
                        "stroke": choose_color(type_of_ice),
                        "stroke-width": 2,
                        "stroke-opacity": 1,
                        "fill": choose_color(type_of_ice),
                        "fill-opacity": 0.5
                    },
                    "geometry": {
                        "coordinates": [list_cords],
                        "type": "Polygon"
                    }
                })

    # list_cords.append(list_cords[0])
    return geojson
