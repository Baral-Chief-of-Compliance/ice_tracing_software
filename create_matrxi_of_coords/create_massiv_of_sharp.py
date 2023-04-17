def create_massiv(width, height):
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

    return map_