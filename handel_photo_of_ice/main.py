from PIL import Image
import numpy as np
from math import sqrt
import create_geojson_from_photo


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
        if ((img_RGB[y][x][0] >= 230 and img_RGB[y][x][0] <= 260) and
            (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 20) and
            (img_RGB[y][x][2] >= 230 and img_RGB[y][x][2] <= 250)
        ):
            map_[y][x] = {
                "type": "young",
                "x": x-a,
                "y": b-y,
                "longitude": np.degrees(np.arctan(b-y / x-a)),
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            if map_[y][x]["x"] > 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -180 + map_[y][x]["longitude"]

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] > 0:
                pass

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] < 0:
                pass

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = 90 + (-1 * map_[y][x]["longitude"])

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = -180

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = 0

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -90

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = -270

        elif ((img_RGB[y][x][0] >= 120 and img_RGB[y][x][0] <= 150) and
            (img_RGB[y][x][1] >= 0 and img_RGB[y][x][1] <= 20) and
            (img_RGB[y][x][2] >= 0 and img_RGB[y][x][2] <= 20)
        ):
            map_[y][x] = {
                "type": "old",
                "x": x-a,
                "y": b-y,
                "longitude": np.degrees(np.arctan(b-y / x-a)),
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            if map_[y][x]["x"] > 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -180 + map_[y][x]["longitude"]

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] > 0:
                pass

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] < 0:
                pass

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = 90 + (-1 * map_[y][x]["longitude"])

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = -180

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = 0

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -90

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = -270

        elif ((img_RGB[y][x][0] >= 0 and img_RGB[y][x][0] <= 20) and
            (img_RGB[y][x][1] >= 185 and img_RGB[y][x][1] <= 215) and
            (img_RGB[y][x][2] >= 140 and img_RGB[y][x][2] <= 170)
        ):
            map_[y][x] = {
                "type": "first-year",
                "x": x-a,
                "y": b-y,
                "longitude": np.degrees(np.arctan(b-y / x-a)),
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            if map_[y][x]["x"] > 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -180 + map_[y][x]["longitude"]

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] > 0:
                pass

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] < 0:
                pass

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = 90 + (-1 * map_[y][x]["longitude"])

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = -180

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = 0

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -90

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = -270

        elif ((img_RGB[y][x][0] >= 0 and img_RGB[y][x][0] <= 20) and
            (img_RGB[y][x][1] >= 95 and img_RGB[y][x][1] <= 125) and
            (img_RGB[y][x][2] >= 235 and img_RGB[y][x][2] <= 255)
        ):
            map_[y][x] = {
                "type": "nilas",
                "x": x-a,
                "y": b-y,
                "longitude": np.degrees(np.arctan(b-y / x-a)),
                "latitude": 90 - sqrt(((x-a)**2 + (y-b)**2))*step_latitude
            }

            if map_[y][x]["x"] > 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -180 + map_[y][x]["longitude"]

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] > 0:
                pass

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] < 0:
                pass

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = 90 + (-1 * map_[y][x]["longitude"])

            elif map_[y][x]["x"] > 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = -180

            elif map_[y][x]["x"] < 0 and map_[y][x]["y"] == 0:
                map_[y][x]["longitude"] = 0

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] > 0:
                map_[y][x]["longitude"] = -90

            elif map_[y][x]["x"] == 0 and map_[y][x]["y"] < 0:
                map_[y][x]["longitude"] = -270


with open("map.txt", 'w') as file:
    for line in map_:
        file.write(str(line))
        file.write("\n")


create_geojson_from_photo.create_geojson(map_, width, length)


