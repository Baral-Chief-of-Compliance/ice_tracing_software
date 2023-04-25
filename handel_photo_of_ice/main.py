from PIL import Image
import numpy as np
from math import sqrt
import create_geojson_from_photo
from create_parameters_for_dict import create_longitude
from map_object_border import clear
from create_polygon import clean_map
import json
import sys
import clean_line_lat_long


sys.setrecursionlimit(2000)

img = Image.open("./photos/test_3.jpg")

size = img.size

length = size[0]
width = size[1]
a = length // 2
b = width // 2

start_latitude = 55
end_latitude = 90
step_latitude = (90-55)/a
print(f"центр карты: ({a}, {b})\n"
      f"начальная широта: {end_latitude}\n"
      f"конечная широта: {start_latitude}\n"
      f"шаг широты на пиксель: {step_latitude}")

img_RGB = np.asarray(img.convert('RGB'))

map_ = [['.' for x in range(length)] for y in range(width)]

for y in range(width):
    for x in range(length):
        if ((img_RGB[y][x][0] >= 227 and img_RGB[y][x][0] <= 267) and
            (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 40) and
            (img_RGB[y][x][2] >= 229 and img_RGB[y][x][2] <= 269)
        ):

            map_[y][x] = {
                "type": "young",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])


        elif ((img_RGB[y][x][0] >= 124 and img_RGB[y][x][0] <= 164) and
            (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 40) and
            (img_RGB[y][x][2] >= 0 and img_RGB[y][x][2] <= 40)
        ):
            map_[y][x] = {
                "type": "old",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])


        elif ((img_RGB[y][x][0] >= 0 and img_RGB[y][x][0] <= 5) and
            (img_RGB[y][x][1] >= 195 and img_RGB[y][x][1] <= 205) and
            (img_RGB[y][x][2] >= 156 and img_RGB[y][x][2] <= 166)
        ):
            map_[y][x] = {
                "type": "first-year",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])


        elif ((img_RGB[y][x][0] >= 0 and img_RGB[y][x][0] <= 20) and
            (img_RGB[y][x][1] >= 95 and img_RGB[y][x][1] <= 125) and
            (img_RGB[y][x][2] >= 235 and img_RGB[y][x][2] <= 255)
        ):
            map_[y][x] = {
                "type": "nilas",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])


        elif ((img_RGB[y][x][0] >= 18 and img_RGB[y][x][0] <= 80) and
            (img_RGB[y][x][1] >= 163 and img_RGB[y][x][1] <= 187) and
            (img_RGB[y][x][2] >= 139 and img_RGB[y][x][2] <= 154)
        ):
            map_[y][x] = {
                "type": "line",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])

        # elif ((img_RGB[y][x][0] >= 0 and img_RGB[y][x][0] <= 20) and
        #
        #       (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 20) and
        #
        #       (img_RGB[y][x][2] >= 0 and img_RGB[y][x][2] <= 20)
        #
        # ):
        #     # map_[y][x]= '#'
        #     map_[y][x] = {
        #         "type": "nilas",
        #         "x": x-a,
        #         "y": b-y,
        #         "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
        #     }
        #
        #     map_[y][x] = create_longitude(map_[y][x])

# map_[b][a] = '.'


with open("map.txt", 'w') as file:
    for y in range(width):
        for x in range(length):
            file.write(str(map_[y][x]))
        file.write("\n")


# map_ = clear(map_, width, length, "first-year")
# create_geojson_from_photo.create_geojson(map_, width, length)
# geojson = clean_map(map_, length, width, "first-year")

geojson = clean_line_lat_long.clean_map(map_, length, width, "line")

with open("geo_json_map_line.json", "w") as file:
    json.dump(geojson, file)
