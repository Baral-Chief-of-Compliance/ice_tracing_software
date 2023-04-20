
def crete_list_coords(map_, y_start, x_start, list_coords, width, height):
    list_coords.append(map_[y_start][x_start])

    if y_start == 0:
        if x_start == 0:
            if map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

        elif x_start == width - 1:
            if map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start-1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        else:
            if map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

    elif y_start == height - 1:

        if x_start == 0:
            if map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

        elif x_start == width - 1:

            if map_[y_start - 1][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        else:

            if map_[y_start - 1][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

    elif x_start == 0:
        if y_start == 0:
            if map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

        else:
            if map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start - 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start + 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

    elif x_start == width - 1:
        if y_start == 0:
            if map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start-1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        elif y_start == height - 1:
            if map_[y_start - 1][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

        else:
            if map_[y_start - 1][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

            elif map_[y_start - 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

            elif map_[y_start + 1][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

            elif map_[y_start][x_start - 1] != '.':
                map_[y_start][x_start] = '.'
                return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)

    else:
        if map_[y_start - 1][x_start - 1] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords, width, height)

        elif map_[y_start - 1][x_start] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start, list_coords, width, height)

        elif map_[y_start - 1][x_start + 1] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords, width, height)

        elif map_[y_start][x_start + 1] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start, x_start + 1, list_coords, width, height)

        elif map_[y_start + 1][x_start + 1] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords, width, height)

        elif map_[y_start + 1][x_start] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start, list_coords, width, height)

        elif map_[y_start + 1][x_start - 1] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords, width, height)

        elif map_[y_start][x_start - 1] != '.':
            map_[y_start][x_start] = '.'
            return crete_list_coords(map_, y_start, x_start - 1, list_coords, width, height)





    # try:
    #     map_[y_start - 1][x_start - 1]
    # except IndexError:
    #     pass
    #
    # else:
    #     print(f'\nсработал 1 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start - 1][x_start - 1] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start - 1, x_start - 1, list_coords)
    #
    # try:
    #     map_[y_start - 1][x_start]
    #
    # except IndexError:
    #     pass
    #
    # else:
    #     print(f'\nсработал 2 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start - 1][x_start] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start - 1, x_start, list_coords)
    #
    # try:
    #     map_[y_start - 1][x_start + 1]
    #
    # except IndexError:
    #     pass
    # else:
    #     print(f'\nсработал 3 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start - 1][x_start + 1] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start - 1, x_start + 1, list_coords)
    #
    # try:
    #     map_[y_start][x_start + 1]
    # except IndexError:
    #     pass
    # else:
    #     print(f'\nсработал 4 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start][x_start + 1] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start, x_start + 1, list_coords)
    #
    # try:
    #     map_[y_start + 1][x_start + 1]
    # except IndexError:
    #     pass
    #
    # else:
    #     print(f'\nсработал 5 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start + 1][x_start + 1] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start + 1, x_start + 1, list_coords)
    #
    # try:
    #     map_[y_start + 1][x_start]
    # except IndexError:
    #     pass
    #
    # else:
    #     print(f'\nсработал 6 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start + 1][x_start] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start + 1, x_start, list_coords)
    #
    # try:
    #     map_[y_start + 1][x_start - 1]
    # except IndexError:
    #     pass
    # else:
    #     print(f'\nсработал 7 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start + 1][x_start - 1] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start + 1, x_start - 1, list_coords)
    #
    # try:
    #     map_[y_start][x_start - 1]
    # except IndexError:
    #     pass
    #
    # else:
    #     print(f'\nсработал 8 else для {map_[y_start][x_start]} c y: {y_start} x: {x_start}')
    #     if map_[y_start][x_start - 1] != '.':
    #         map_[y_start][x_start] = '.'
    #         return crete_list_coords(map_, y_start, x_start - 1, list_coords)

def clean_map(map_, width, height):
    list_cords = []
    for y in range(height):
        for x in range(width):
            if map_[y][x] != '.':
                print("\n\n")
                print(map_[y][x])
                crete_list_coords(map_, y, x, list_cords, width, height)

    # list_cords.append(list_cords[0])
    return list_cords
