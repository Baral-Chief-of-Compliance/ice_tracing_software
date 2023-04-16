import numpy as np


def create_test_data(width, height):
    a = width // 2
    b = height // 2
    map_ = [['.' for x in range(width)] for y in range(height)]
    EPSILON = 2.2
    latitude = 90.0
    for r in range(width // 2):
        EPSILON = EPSILON + 0.1

        # draw the circle
        for y in range(height):
            for x in range(width):
                # see if we're close to (x-a)**2 + (y-b)**2 == r**2
                if abs((x - a) ** 2 + (y - b) ** 2 - r ** 2) < EPSILON ** 2:
                    map_[y][x] = '#'

                    # 1 квадрант
                    # if (y < b) and (x > a):
                    #     x_c = x - a
                    #     y_c = b - y
                    #     f = 180 + np.degrees(np.arctan(y_c / x_c))
                    #
                    # # 2 квадрант
                    # elif (y < b) and (x < a):
                    #     x_c = x - a
                    #     y_c = b - y
                    #     f = np.degrees(np.arctan(y_c / x_c))
                    #
                    # # 3 квадрант
                    # elif (y > b) and (x < a):
                    #     x_c = x - a
                    #     y_c = b - y
                    #     f = np.degrees(np.arctan(y_c / x_c))
                    #
                    # # 4 квадрант
                    # elif (y > b) and (x > a):
                    #     x_c = x - a
                    #     y_c = b - y
                    #     f = 180 + (np.degrees(np.arctan(y_c / x_c)))
                    #
                    # elif (x == a) and (y > b):
                    #     x_c = 0
                    #     y_c = b - y
                    #     f = 90
                    #
                    # elif (x == a) and (y < b):
                    #     x_c = 0
                    #     y_c = b - y
                    #     f = 270
                    #
                    # elif (y == b) and (x > a):
                    #     x_c = x - a
                    #     y_c = 0
                    #     f = 180
                    #
                    # elif (y == b) and (x < a):
                    #     x_c = x - a
                    #     y_c = 0
                    #     f = 0
                    #
                    # map_[y][x] = f'{f}'

    return map_


def clear(map_, width, height):

    index_delete_point = []

    for y in range(height):
        for x in range(width):
            if map_[y][x] != '.':
                if y == 0:
                    if(
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y + 1][x] != '.'
                            and map_[y + 1][x - 1] != '.'
                            and map_[y + 1][x + 1] != '.'
                    ):
                        index_delete_point.append((y, x))
                    elif(
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y + 1][x] != '.'
                    ):
                        index_delete_point.append((y, x))

                elif y == height-1:
                    if(
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y - 1][x] != '.'
                            and map_[y - 1][x - 1] != '.'
                            and map_[y - 1][x + 1] != '.'
                    ):
                        index_delete_point.append((y, x))
                    elif(
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y - 1][x] != '.'
                    ):
                        index_delete_point.append((y, x))
                else:
                    if (
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y - 1][x] != '.'
                            and map_[y + 1][x] != '.'
                            and map_[y + 1][x + 1] != '.'
                            and map_[y + 1][x - 1] != '.'
                            and map_[y - 1][x - 1] != '.'
                            and map_[y - 1][x + 1] != '.'
                    ):
                        index_delete_point.append((y,x))

                    elif (
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y - 1][x] != '.'
                            and map_[y + 1][x] != '.'
                    ):
                        index_delete_point.append((y, x))

    for i in index_delete_point:
        map_[i[0]][i[1]] = '.'

    return map_


test_map = create_test_data(129,89)

for line in test_map:
    print (' '.join(line))

new_test = clear(test_map, 129, 89)

for line in new_test:
    print (' '.join(line))





