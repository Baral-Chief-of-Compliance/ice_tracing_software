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


def clear(map_, width, height):

    index_delete_point = []

    for y in range(height):
        for x in range(width):
            if map_[y][x] != '.':
                if map_[y][x]["type"] == "young":
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


# test_map = create_test_data(11,11)
#
# for line in test_map:
#     print (line)
#
#
#
# print("\n\n")
#
#
# new_test = clear(test_map, 11, 11)
#
#
# for line in new_test:
#     print (line)
#
# list_cords = clean_map(new_test, 11, 11)
#
# print("\n\n")
# sharp_massiv = create_massiv(11,11)
# for line in sharp_massiv:
#     print (' '.join(line))
#
#
# print("\n\n")
#
# print(list_cords)
#
# polygon = sg.MultiPoint(list_cords).convex_hull
# json_for_geo["features"][0]["geometry"] = sg.mapping(polygon)
#
# with open('coords_of_polygon.json', 'w') as f:
#     json.dump(json_for_geo, f)

