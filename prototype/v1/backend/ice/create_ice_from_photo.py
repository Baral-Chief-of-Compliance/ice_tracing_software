from ice.test import Config


def create_ice_from_photo(photo, map_):

    width = len(photo)
    length = len(photo[0])

    for y in range(width):
        for x in range(length):
            if photo[y, x][0] == Config.old_ice[0] \
                    and photo[y, x][1] == Config.old_ice[1] \
                    and photo[y, x][2] == Config.old_ice[2]:
                map_[y][x]["type_of_ice"] = "old_ice"
                print("old_ice")

            elif photo[y, x][0] == Config.young_ice[0] \
                    and photo[y, x][1] == Config.young_ice[1] \
                    and photo[y, x][2] == Config.young_ice[2]:
                map_[y][x]["type_of_ice"] = "young_ice"
                print("young_ice")

            elif photo[y, x][0] == Config.first_year_ice[0] \
                    and photo[y, x][1] == Config.first_year_ice[1] \
                    and photo[y, x][2] == Config.first_year_ice[2]:
                map_[y][x]["type_of_ice"] = "first_year_ice"
                print("first_year_ice")

            elif photo[y, x][0] == Config.nilas_ice[0] \
                    and photo[y, x][1] == Config.nilas_ice[1] \
                    and photo[y, x][2] == Config.nilas_ice[2]:
                map_[y][x]["type_of_ice"] = "nilas_ice"
                print("nilas_ice")

            elif photo[y, x][0] == Config.fast_ice[0] \
                    and photo[y, x][1] == Config.fast_ice[1] \
                    and photo[y, x][2] == Config.fast_ice[2]:
                map_[y][x]["type_of_ice"] = "fast_ice"
                print("fast_ice")

            elif photo[y, x][0] == Config.ice_field[0] \
                    and photo[y, x][1] == Config.ice_field[1] \
                    and photo[y, x][2] == Config.ice_field[2]:
                map_[y][x]["type_of_ice"] = "ice_field"
                print("ice_field")

    return map_
