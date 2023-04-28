from create_node import create


step = 0.33333

start_latitude = 90.0
end_latitude = -90.0

latitude_list = []
width = int((180 // step) + 1)
for i in range(width):
    if i == 0:
        latitude_list.append(start_latitude)

    elif i == width - 1:
        latitude_list.append(end_latitude)

    else:
        latitude_list.append(start_latitude - i * step)


start_longitude = -180
end_longitude = 180
longitude_list = []
length = int((360 // step) + 1)

for i in range(length):
    if i == 0:
        longitude_list.append(start_longitude)

    elif i == length - 1:
        longitude_list.append(end_longitude)

    else:
        longitude_list.append(start_longitude + i * step)


map_ = [['.' for x in range(length)] for y in range(width)]

for y in range(width):
    for x in range(length):

        if y == 0 and x == 0:
            map_[y][x] = create(-180.0, 90.0, False, False, "")

        elif y == 0 and x == length - 1:
            map_[y][x] = create(180.0, 90.0, False, False, "")

        elif y == width - 1 and x == 0:
            map_[y][x] = create(-180.0, -90.0, False, False, "")

        elif y == width - 1 and x == length - 1:
            map_[y][x] = create(180.0, -90.0, False, False, "")

        elif y == 0:
            map_[y][x] = create(start_longitude + x * step, 90.0, False, False, "")

        elif y == width - 1:
            map_[y][x] = create(start_longitude + x * step, -90.0, False, False, "")

        elif x == 0:
            map_[y][x] = create(-180, start_latitude - y * step, False, False, "")

        elif x == length - 1:
            map_[y][x] = create(180, start_latitude - y * step, False, False, "")

        else:
            map_[y][x] = create(start_longitude + x * step, start_latitude - y * step, False, False, "")

with open("map.txt", "w") as file:
    for line in map_:
        file.write(str(line))
        file.write("\n")
