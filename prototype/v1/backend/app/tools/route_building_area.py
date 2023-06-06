from app.tools.find_index import find_index
from global_land_mask import globe


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


def get_length_area_border(y_start, x_start, y_end, x_end):
    if y_start > y_end:
        area_width = y_start - y_end + 1
    elif y_start < y_end:
        area_width = y_end - y_start + 1

    if x_start > x_end:
        area_length = x_start - x_end + 1
    elif x_start < x_end:
        area_length = x_end - x_start + 1

    return area_width, area_length


def get_vertex_area_border(y_start, x_start, y_end, x_end):
    print(y_start, x_start, y_end, x_end)
    if y_start > y_end:
        y_vertex_top = y_end
        y_vertex_bottom = y_start

    elif y_start < y_end:
        y_vertex_top = y_start
        y_vertex_bottom = y_end

    if x_start > x_end:
        x_vertex_right = x_start
        x_vertex_left = x_end

    elif x_start < x_end:
        x_vertex_right = x_end
        x_vertex_left = x_start

    return y_vertex_top, y_vertex_bottom, x_vertex_right, x_vertex_left


def build(map_, width, length, start_longitude, start_latitude, end_longitude, end_latitude):
    y_start, x_start = nearest(map_, width, length, start_longitude, start_latitude)
    y_end, x_end = nearest(map_, width, length, end_longitude, end_latitude)

    print(f"старт {y_start}, {x_start}")
    print(f"финиш {y_end}, {x_end}")
    map_[y_start][x_start]["start"] = True
    map_[y_end][x_end]["end"] = True

    area_width, area_length = get_length_area_border(y_start, x_start, y_end, x_end)
    y_vertex_top, y_vertex_bottom, x_vertex_right, x_vertex_left \
        = get_vertex_area_border(y_start, x_start, y_end, x_end)

    area = [['.' for x in range(area_length)] for y in range(area_width)]

    print(f"y_vertex_top: {y_vertex_top}")
    print(f"y_vertex_bottom: {y_vertex_bottom}")
    print(f"x_vertex_right: {x_vertex_right}")
    print(f"x_vertex_left: {x_vertex_left}")

    for y in range(width):
        for x in range(length):
            if y_vertex_top <= y <= y_vertex_bottom:
                if x_vertex_left <= x <= x_vertex_right:
                    area[y - y_vertex_top][x - x_vertex_left] = map_[y][x]

    return area


def build_2(map_, width, length, start_longitude, start_latitude, end_longitude, end_latitude):
    y_start, x_start = nearest(map_, width, length, start_longitude, start_latitude)
    y_end, x_end = nearest(map_, width, length, end_longitude, end_latitude)

    print(f"старт {y_start}, {x_start}")
    print(f"финиш {y_end}, {x_end}")
    map_[y_start][x_start]["start"] = True
    map_[y_end][x_end]["end"] = True

    area_width, area_length = get_length_area_border(y_start, x_start, y_end, x_end)



    y_vertex_top, y_vertex_bottom, x_vertex_right, x_vertex_left \
        = get_vertex_area_border(y_start, x_start, y_end, x_end)

    y_vertex_top = 0
    area_width = 52

    area = [['.' for x in range(area_length)] for y in range(area_width)]

    for y in range(width):
        for x in range(length):
            if y_vertex_top <= y <= y_vertex_bottom:
                if x_vertex_left <= x <= x_vertex_right:
                    area[y - y_vertex_top][x - x_vertex_left] = map_[y][x]

    return area


def build_interval_route(map_, area_building_route):

    width = len(map_)
    length = len(map_[0])

    y_1, x_1 = nearest(map_, width, length, area_building_route[0][1], area_building_route[0][0])
    y_2, x_2 = nearest(map_, width, length, area_building_route[1][1], area_building_route[1][0])
    y_3, x_3 = nearest(map_, width, length, area_building_route[2][1], area_building_route[2][0])
    y_4, x_4 = nearest(map_, width, length, area_building_route[3][1], area_building_route[3][0])

    print(f"y_1 = {y_1}, x_1 = {x_1}")
    print(f"y_2 = {y_2}, x_2 = {x_2}")
    print(f"y_3 = {y_3}, x_3 = {x_3}")
    print(f"y_4 = {y_4}, x_4 = {x_4}")

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
