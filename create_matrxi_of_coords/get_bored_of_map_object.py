import numpy as np
from create_polygon import clean_map
import json
from create_massiv_of_sharp import create_massiv
import shapely.geometry as sg


json_for_geo = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": []
    }
  ]
}


def create_test_data(width, height):
    a = width // 2
    b = height // 2
    map_ = [['.' for x in range(width)] for y in range(height)]
    EPSILON = 2.2
    latitude = 90.0
    for r in range(width // 2):
        EPSILON = EPSILON + 0.2

        # draw the circle
        for y in range(height):
            for x in range(width):
                # see if we're close to (x-a)**2 + (y-b)**2 == r**2
                if abs((x - a) ** 2 + (y - b) ** 2 - r ** 2) < EPSILON ** 2:
                    map_[y][x] = '#'

                    #1 квадрант
                    if (y < b) and (x > a):
                        x_c = x - a
                        y_c = b - y
                        f = 180 + np.degrees(np.arctan(y_c / x_c))

                    # 2 квадрант
                    elif (y < b) and (x < a):
                        x_c = x - a
                        y_c = b - y
                        f = 360 + np.degrees(np.arctan(y_c / x_c))

                    # 3 квадрант
                    elif (y > b) and (x < a):
                        x_c = x - a
                        y_c = b - y
                        f = np.degrees(np.arctan(y_c / x_c))

                    # 4 квадрант
                    elif (y > b) and (x > a):
                        x_c = x - a
                        y_c = b - y
                        f = 180 + (np.degrees(np.arctan(y_c / x_c)))

                    elif (x == a) and (y > b):
                        x_c = 0
                        y_c = b - y
                        f = 90

                    elif (x == a) and (y < b):
                        x_c = 0
                        y_c = b - y
                        f = 270

                    elif (y == b) and (x > a):
                        x_c = x - a
                        y_c = 0
                        f = 180

                    elif (y == b) and (x < a):
                        x_c = x - a
                        y_c = 0
                        f = 360

                    map_[y][x] = [f, 75.18776700960646]

    return map_


def clear(map_, width, height):

    index_delete_point = []

    for y in range(height):
        for x in range(width):
            if map_[y][x] != '.':
                if y == 0:
                    # if(
                    #         map_[y][x - 1] != '.'
                    #         and map_[y][x + 1] != '.'
                    #         and map_[y + 1][x] != '.'
                    #         and map_[y + 1][x - 1] != '.'
                    #         and map_[y + 1][x + 1] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    # elif(
                    #         map_[y][x - 1] != '.'
                    #         and map_[y][x + 1] != '.'
                    #         and map_[y + 1][x] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    pass

                elif y == height-1:
                    # if(
                    #         map_[y][x - 1] != '.'
                    #         and map_[y][x + 1] != '.'
                    #         and map_[y - 1][x] != '.'
                    #         and map_[y - 1][x - 1] != '.'
                    #         and map_[y - 1][x + 1] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    # elif(
                    #         map_[y][x - 1] != '.'
                    #         and map_[y][x + 1] != '.'
                    #         and map_[y - 1][x] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    pass

                elif x == 0:
                    # if (
                    #         map_[y + 1][x + 1] != '.'
                    #         and map_[y][x + 1] != '.'
                    #         and map_[y + 1][x] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    # elif (
                    #         map_[y - 1][x + 1] != '.'
                    #         and map_[y][x + 1] != '.'
                    #         and map_[y - 1][x] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    pass

                elif x == width-1:
                    # if (
                    #         map_[y + 1][x - 1] != '.'
                    #         and map_[y][x - 1] != '.'
                    #         and map_[y + 1][x] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    # elif (
                    #         map_[y - 1][x - 1] != '.'
                    #         and map_[y][x - 1] != '.'
                    #         and map_[y - 1][x] != '.'
                    # ):
                    #     index_delete_point.append((y, x))
                    pass

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
                        index_delete_point.append([y, x])

                    elif (
                            map_[y][x - 1] != '.'
                            and map_[y][x + 1] != '.'
                            and map_[y - 1][x] != '.'
                            and map_[y + 1][x] != '.'
                    ):
                        index_delete_point.append([y, x])

    for i in index_delete_point:
        map_[i[0]][i[1]] = '.'

    return map_


test_map = create_test_data(11,11)

for line in test_map:
    print (line)



print("\n\n")


new_test = clear(test_map, 11, 11)


for line in new_test:
    print (line)

list_cords = clean_map(new_test, 11, 11)

print("\n\n")
sharp_massiv = create_massiv(11,11)
for line in sharp_massiv:
    print (' '.join(line))


print("\n\n")

print(list_cords)

polygon = sg.MultiPoint(list_cords).convex_hull
json_for_geo["features"][0]["geometry"] = sg.mapping(polygon)

with open('coords_of_polygon.json', 'w') as f:
    json.dump(json_for_geo, f)

