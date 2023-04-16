import numpy as np
import json


json_for_geo = {
    "type": "FeatureCollection",
    "features": []
}


def create_geo_json(width, height):

    a = width//2
    b = height//2
    map_ = [['.' for x in range(width)] for y in range(height)]
    EPSILON = 2.2
    latitude = 90.0
    for r in range(width//2):
        EPSILON = EPSILON + 0.1

        # draw the circle
        for y in range(height):
            for x in range(width):
                # see if we're close to (x-a)**2 + (y-b)**2 == r**2
                if abs((x-a)**2 + (y-b)**2 - r**2) < EPSILON**2:

                    # 1 квадрант
                    if (y < b) and (x > a):
                        x_c = x - a
                        y_c = b - y
                        f = 180 + np.degrees(np.arctan(y_c/x_c))

                    # 2 квадрант
                    elif (y < b) and (x < a):
                        x_c = x - a
                        y_c = b - y
                        f = np.degrees(np.arctan(y_c / x_c))

                    # 3 квадрант
                    elif (y > b) and (x < a):
                        x_c = x - a
                        y_c = b -y
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
                        f = 0

                    map_[y][x] = f'{f}'
                    json_for_geo["features"].append(
                        {
                            "type": "Feature",
                            "properties": {},
                            "geometry": {
                                "coordinates": [
                                f,
                                latitude
                                ],
                                "type": "Point"
                            }
                        }
                    )

        latitude = latitude - 0.54

    # print the map
    # for line in map_:
    #     print (' '.join(line))

    with open('data.json', 'w') as f:
        json.dump(json_for_geo, f)

    return map_
