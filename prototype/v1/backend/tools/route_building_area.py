from find_index import find_index


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

                if map_[y][x]["longitude"] >= 0 and map_[y][x]["latitude"] >= 0:
                    if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                        min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    elif longitude < 0 and latitude < 0:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] < 0 and map_[y][x]["latitude"] < 0:
                    if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                        min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    elif longitude >= 0 > latitude:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] >= 0 > map_[y][x]["latitude"]:
                    if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                        min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)

    elif longitude < 0 <= latitude:
        for y in range(width):
            for x in range(length):
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
