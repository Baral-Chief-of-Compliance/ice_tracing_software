def clear(map_, type_of_ice):

    width = len(map_)
    length = len(map_[0])

    index_delete_point = []

    for y in range(width):
        for x in range(length):
            if map_[y][x]["type_of_ice"] == type_of_ice:
                if y == 0:
                    # if(
                    #         map_[y][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y][x + 1]["type_of_ice"] != type_of_ice
                    #         and map_[y + 1][x]["type_of_ice"] != type_of_ice
                    #         and map_[y + 1][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y + 1][x + 1]["type_of_ice"] != type_of_ice
                    # ):
                    #     index_delete_point.append((y, x))
                    # elif(
                    #         map_[y][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y][x + 1]["type_of_ice"] != type_of_ice
                    #         and map_[y + 1][x]["type_of_ice"] != type_of_ice
                    # ):
                    #     index_delete_point.append((y, x))

                    pass

                elif y == width - 1:
                #     if(
                #             map_[y][x - 1]["type_of_ice"] != type_of_ice
                #             and map_[y][x + 1]["type_of_ice"] != type_of_ice
                #             and map_[y - 1][x]["type_of_ice"] != type_of_ice
                #             and map_[y - 1][x - 1]["type_of_ice"] != type_of_ice
                #             and map_[y - 1][x + 1]["type_of_ice"] != type_of_ice
                #     ):
                #         index_delete_point.append((y, x))
                #     elif(
                #             map_[y][x - 1]["type_of_ice"] != type_of_ice
                #             and map_[y][x + 1]["type_of_ice"] != type_of_ice
                #             and map_[y - 1][x]["type_of_ice"] != type_of_ice
                #     ):
                #         index_delete_point.append((y, x))
                #
                # elif x == 0:
                #     if (
                #             map_[y + 1][x + 1]["type_of_ice"] != type_of_ice
                #             and map_[y][x + 1]["type_of_ice"] != type_of_ice
                #             and map_[y + 1][x]["type_of_ice"] != type_of_ice
                #     ):
                #         index_delete_point.append((y, x))
                #     elif (
                #             map_[y - 1][x + 1]["type_of_ice"] != type_of_ice
                #             and map_[y][x + 1]["type_of_ice"] != type_of_ice
                #             and map_[y - 1][x]["type_of_ice"] != type_of_ice
                #     ):
                #         index_delete_point.append((y, x))
                    pass

                elif x == length - 1:
                    # if (
                    #         map_[y + 1][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y + 1][x]["type_of_ice"] != type_of_ice
                    # ):
                    #     index_delete_point.append((y, x))
                    # elif (
                    #         map_[y - 1][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y][x - 1]["type_of_ice"] != type_of_ice
                    #         and map_[y - 1][x]["type_of_ice"] != type_of_ice
                    # ):
                    #     index_delete_point.append((y, x))
                    pass

                else:
                    if (
                            map_[y][x - 1]["type_of_ice"] == type_of_ice
                            and map_[y][x + 1]["type_of_ice"] == type_of_ice
                            and map_[y - 1][x]["type_of_ice"] == type_of_ice
                            and map_[y + 1][x]["type_of_ice"] == type_of_ice
                            and map_[y + 1][x + 1]["type_of_ice"] == type_of_ice
                            and map_[y + 1][x - 1]["type_of_ice"] == type_of_ice
                            and map_[y - 1][x - 1]["type_of_ice"] == type_of_ice
                            and map_[y - 1][x + 1]["type_of_ice"] == type_of_ice
                    ):
                        index_delete_point.append([y, x])

                    elif (
                            map_[y][x - 1]["type_of_ice"] == type_of_ice
                            and map_[y][x + 1]["type_of_ice"] == type_of_ice
                            and map_[y - 1][x]["type_of_ice"] == type_of_ice
                            and map_[y + 1][x]["type_of_ice"] == type_of_ice
                    ):
                        index_delete_point.append([y, x])

    for i in index_delete_point:
        map_[i[0]][i[1]]["type_of_ice"] = ''

    return map_
