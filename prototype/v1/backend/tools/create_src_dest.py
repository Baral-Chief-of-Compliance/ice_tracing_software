def create_src_dest(area):
    width = len(area)
    length = len(area[0])

    src = ""
    dest = ""
    for y in range(width):
        for x in range(length):
            if area[y][x]["start"]:
                src = f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"
            if area[y][x]["end"]:
                dest = f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"

    return src, dest
