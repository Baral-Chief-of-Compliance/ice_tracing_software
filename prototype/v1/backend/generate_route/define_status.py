def check(area, end_longitude, end_latitude):

    area_width = len(area)
    area_length = len(area[0])

    for y in range(area_width):
        for x in range(area_length):
            if area[y][x]["longitude"] == end_longitude and area[y][x]["latitude"] == end_latitude:
                return "завершение"

    return "в процессе"
