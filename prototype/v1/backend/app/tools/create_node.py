def create(longitude, latitude, start, end, type_of_ice):
    return {
        "longitude": longitude,
        "latitude": latitude,
        "start": start,
        "end": end,
        "type_of_ice": type_of_ice,
        "weight": 0
    }
