def clear(map_, width, length, type_of_ice):

    index_delete_point = []

    for y in range(width):
        for x in range(length):
            if map_[y][x] != '.':
                if map_[y][x]["type"] == type_of_ice:
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

                    elif y == width-1:
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

                    elif x == length-1:
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