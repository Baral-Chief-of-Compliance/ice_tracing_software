import numpy as np


def create_longitude(dict):
    # 1 квадрант
    if dict["x"] > 0 and dict["y"] > 0:
        dict["longitude"] = 180 + np.degrees(np.arctan(dict["y"] / dict["x"]))

    # 2 квадрант
    elif dict["x"] < 0 and dict["y"] > 0:
        dict["longitude"] = np.degrees(np.arctan(dict["y"] / dict["x"]))

    # 3 квадрант
    elif dict["x"] < 0 and dict["y"] < 0:
        dict["longitude"] = np.degrees(np.arctan(dict["y"] / dict["x"]))
    # 4 квадрант
    elif dict["x"] > 0 and dict["y"] < 0:
        dict["longitude"] = 180 + np.degrees(np.arctan(dict["y"] / dict["x"]))

    elif dict["x"] > 0 and dict["y"] == 0:
        dict["longitude"] = 180.074126828645745

    elif dict["x"] < 0 and dict["y"] == 0:
        dict["longitude"] = 1.074126828645745

    elif dict["x"] == 0 and dict["y"] > 0:
        dict["longitude"] = 269.074126828645745

    elif dict["x"] == 0 and dict["y"] < 0:
        dict["longitude"] = 90.074126828645745

    return dict
