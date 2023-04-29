from find_index import find_index


def find_min_elem(map_, width, length, longitude, latitude):
    if longitude >= 0 and latitude >= 0:
        for y in range(width):
            for x in range(length):
                if map_[y][x]["longitude"] >= 0 and map_[y][x]["latitude"] >= 0:
                    print(map_[y][x])
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
                    # print(map_[y][x]["longitude"], map_[y][x]["latitude"])
                    # with open("check_if.txt", "w") as file:
                    #     file.write(str(map_[y][x]))
                    #     file.write("\n")
                    if check_diff(map_[y][x], longitude, latitude, difference_long, difference_lat):
                        min_elem, difference_long, difference_lat = define_diff(map_[y][x], longitude, latitude)
                        print(min_elem, difference_long, difference_lat)

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


def build(map_, width, length, start_longitude, start_latitude, end_longitude, end_latitude):
    y_start, x_start = nearest(map_, width, length, start_longitude, start_latitude)
    y_end, x_end = nearest(map_, width, length, end_longitude, end_latitude)

    map_[y_start][x_start]["start"] = True
    map_[y_end][x_end]["end"] = True
