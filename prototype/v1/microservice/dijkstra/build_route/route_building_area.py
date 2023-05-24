from global_land_mask import globe


def find_index(map_, width, length, elem):
    indexes = []
    for y in range(width):
        for x in range(length):
            if map_[y][x] == elem:
                indexes = [y, x]

    return indexes[0], indexes[1]


def find_min_elem(map_, width, length, longitude, latitude):
    if longitude >= 0 and latitude >= 0:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] >= 0 and map_[y][x]["latitude"] >= 0:
                    return map_[y][x]

    elif longitude < 0 and latitude < 0:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] < 0 and map_[y][x]["latitude"] < 0:
                    return map_[y][x]

    elif longitude >= 0 > latitude:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] >= 0 > map_[y][x]["latitude"]:
                    return map_[y][x]

    elif longitude < 0 <= latitude:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] < 0 <= map_[y][x]["latitude"]:
                    return map_[y][x]


def define_diff(elem, longitude, latitude):
    difference_long = abs(abs(elem["longitude"]) - abs(longitude))
    difference_lat = abs(abs(elem["latitude"]) - abs(latitude))
    return elem, difference_long, difference_lat


def check_diff(elem, longitude, latitude, difference_long, difference_lat):
    return difference_long > abs(abs(elem["longitude"]) - abs(longitude)) or difference_lat > abs(
        abs(elem["latitude"]) - abs(latitude))


def nearest(map_, width, length, longitude, latitude):
    min_elem = find_min_elem(map_, width, length, longitude, latitude)
    difference_long = abs(abs(min_elem["longitude"]) - abs(longitude))
    difference_lat = abs(abs(min_elem["latitude"]) - abs(latitude))

    if longitude >= 0 and latitude >= 0:
        for y in range(width):
            for x in range(length):

                if map_[y][x]["weight"] != 9999:

                    if map_[y][x]["longitude"] >= 0 and map_[y][x]["latitude"] >= 0:
                        if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                            min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    elif longitude < 0 and latitude < 0:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["weight"] != 9999:
                    if map_[y][x]["longitude"] < 0 and map_[y][x]["latitude"] < 0:
                        if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                            min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    elif longitude >= 0 > latitude:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["weight"] != 9999:
                    if map_[y][x]["longitude"] >= 0 > map_[y][x]["latitude"]:
                        if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                            min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    elif longitude < 0 <= latitude:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["weight"] != 9999:
                    if map_[y][x]["longitude"] < 0 <= map_[y][x]["latitude"]:
                        if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                            min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    y, x = find_index(map_, width, length, min_elem)

    return y, x


def build_interval_route(map_, area_building_route):

    width = len(map_)
    length = len(map_[0])

    y_1, x_1 = nearest(map_, width, length, area_building_route[0][1], area_building_route[0][0])
    y_2, x_2 = nearest(map_, width, length, area_building_route[1][1], area_building_route[1][0])
    y_3, x_3 = nearest(map_, width, length, area_building_route[2][1], area_building_route[2][0])
    y_4, x_4 = nearest(map_, width, length, area_building_route[3][1], area_building_route[3][0])

    area_width = y_4 - y_1 + 1
    area_length = x_2 - x_1 + 1

    area = [['.' for x in range(area_length)] for y in range(area_width)]

    for y in range(width):
        for x in range(length):
            if y_1 <= y <= y_4:
                if x_1 <= x <= x_2:
                    area[y - y_1][x - x_1] = map_[y][x]


    for y in range(len(area)):
        for x in range(len(area[0])):
            if globe.is_land(area[y][x]["latitude"], area[y][x]["longitude"]):
                area[y][x]["weight"] = 9999

    return area