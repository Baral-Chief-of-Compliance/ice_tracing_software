def find_index(map_, width, length, elem):
    indexes = []
    for y in range(width):
        for x in range(length):
            if map_[y][x] == elem:
                indexes = [y, x]

    return indexes[0], indexes[1]
