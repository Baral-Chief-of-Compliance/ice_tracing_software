from global_land_mask import globe
import numpy as np


def get_weight_based_ice_class(elem, iceclass):
    if iceclass == "Arc9":
        if elem["type_of_ice"] == "old_ice":
            return 60
        elif elem["type_of_ice"] == "first_year_ice":
            return 50
        elif elem["type_of_ice"] == "young_ice":
            return 40
        elif elem["type_of_ice"] == "nilas_ice":
            return 30
        elif elem["type_of_ice"] == "fast_ice":
            return 20
        elif elem["type_of_ice"] == "fast_ice":
            return 10
        else:
            return 0

    elif iceclass == "Arc8":
        if elem["type_of_ice"] == "old_ice":
            return 99
        elif elem["type_of_ice"] == "first_year_ice":
            return 60
        elif elem["type_of_ice"] == "young_ice":
            return 45
        elif elem["type_of_ice"] == "nilas_ice":
            return 35
        elif elem["type_of_ice"] == "fast_ice":
            return 25
        elif elem["type_of_ice"] == "fast_ice":
            return 15
        else:
            return 0

    elif iceclass == "Arc7":
        if elem["type_of_ice"] == "old_ice":
            return 30
        elif elem["type_of_ice"] == "first_year_ice":
            return 20
        elif elem["type_of_ice"] == "young_ice":
            return 10
        elif elem["type_of_ice"] == "nilas_ice":
            return 5
        elif elem["type_of_ice"] == "fast_ice":
            return 13
        elif elem["type_of_ice"] == "ice_field":
            return 8
        else:
            return 2

    elif iceclass == "Arc6":
        if elem["type_of_ice"] == "old_ice":
            return 99
        elif elem["type_of_ice"] == "first_year_ice":
            return 99
        elif elem["type_of_ice"] == "young_ice":
            return 55
        elif elem["type_of_ice"] == "nilas_ice":
            return 45
        elif elem["type_of_ice"] == "fast_ice":
            return 35
        elif elem["type_of_ice"] == "fast_ice":
            return 25
        else:
            return 0

    elif iceclass == "Arc5":
        if elem["type_of_ice"] == "old_ice":
            return 9999
        elif elem["type_of_ice"] == "first_year_ice":
            return 9999
        elif elem["type_of_ice"] == "young_ice":
            return 15
        elif elem["type_of_ice"] == "nilas_ice":
            return 5
        elif elem["type_of_ice"] == "fast_ice":
            return 25
        elif elem["type_of_ice"] == "ice_field":
            return 10
        else:
            return 1

    elif iceclass == "Arc4":
        if elem["type_of_ice"] == "old_ice":
            return 99
        elif elem["type_of_ice"] == "first_year_ice":
            return 99
        elif elem["type_of_ice"] == "young_ice":
            return 65
        elif elem["type_of_ice"] == "nilas_ice":
            return 55
        elif elem["type_of_ice"] == "fast_ice":
            return 45
        elif elem["type_of_ice"] == "fast_ice":
            return 35
        else:
            return 0

    elif iceclass == "Ice3":
        if elem["type_of_ice"] == "old_ice":
            return 99
        elif elem["type_of_ice"] == "first_year_ice":
            return 99
        elif elem["type_of_ice"] == "young_ice":
            return 99
        elif elem["type_of_ice"] == "nilas_ice":
            return 60
        elif elem["type_of_ice"] == "fast_ice":
            return 50
        elif elem["type_of_ice"] == "fast_ice":
            return 40
        else:
            return 0

    elif iceclass == "Ice2":
        if elem["type_of_ice"] == "old_ice":
            return 99
        elif elem["type_of_ice"] == "first_year_ice":
            return 99
        elif elem["type_of_ice"] == "young_ice":
            return 99
        elif elem["type_of_ice"] == "nilas_ice":
            return 65
        elif elem["type_of_ice"] == "fast_ice":
            return 55
        elif elem["type_of_ice"] == "fast_ice":
            return 45
        else:
            return 0

    elif iceclass == "Ice1":
        if elem["type_of_ice"] == "old_ice":
            return 99
        elif elem["type_of_ice"] == "first_year_ice":
            return 99
        elif elem["type_of_ice"] == "young_ice":
            return 99
        elif elem["type_of_ice"] == "nilas_ice":
            return 70
        elif elem["type_of_ice"] == "fast_ice":
            return 60
        elif elem["type_of_ice"] == "fast_ice":
            return 50
        else:
            return 0


def get_weight(previous_elem, elem, iceclass):
    lat = np.linspace(
        previous_elem["latitude"],
        elem["latitude"],
        100
        )

    lon = np.linspace(
        previous_elem["longitude"],
        elem["longitude"],
        100
    )

    is_in_land = globe.is_land(lat, lon)
    count_land = np.count_nonzero(is_in_land == True)

    if count_land > 0:
        return 9999

    else:
        result = get_weight_based_ice_class(elem, iceclass)
        return result
