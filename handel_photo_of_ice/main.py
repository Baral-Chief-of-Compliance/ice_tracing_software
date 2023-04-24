from PIL import Image
import numpy as np
from math import sqrt
import create_geojson_from_photo
from create_parameters_for_dict import create_longitude


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

with open("test_map_.txt", "w") as file:
    for y in range(width):
        for x in range(length):
            file.write(str(map_[y][x]))
        file.write("\n")

file.close()


for y in range(width):
    for x in range(length):
        if ((img_RGB[y][x][0] >= 230 and img_RGB[y][x][0] <= 260) and
            (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 20) and
            (img_RGB[y][x][2] >= 230 and img_RGB[y][x][2] <= 250)
        ):

            map_[y][x] = {
                "type": "young",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])


        elif ((img_RGB[y][x][0] >= 120 and img_RGB[y][x][0] <= 150) and
            (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 20) and
            (img_RGB[y][x][2] >= 0 and img_RGB[y][x][2] <= 20)
        ):
            map_[y][x] = {
                "type": "old",
                "x": x-a,
                "y": b-y,
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            map_[y][x] = create_longitude(map_[y][x])


        elif ((img_RGB[y][x][0] >= 0 and img_RGB[y][x][0] <= 20) and
            (img_RGB[y][x][1] >= 185 and img_RGB[y][x][1] <= 215) and
            (img_RGB[y][x][2] >= 140 and img_RGB[y][x][2] <= 170)
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

map_[b][a] = '.'


with open("map.txt", 'w') as file:
    for y in range(width):
        for x in range(length):
            file.write(str(map_[y][x]))
        file.write("\n")

create_geojson_from_photo.create_geojson(map_, width, length)


