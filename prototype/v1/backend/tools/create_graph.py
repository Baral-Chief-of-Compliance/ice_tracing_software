from weight import get_weight


def create(area, iceclass):
    width = len(area)
    length = len(area[0])

    graph = {}

    for y in range(width):
        for x in range(length):
            if y == 0 and x == 0:
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y + 1][x + 1]['longitude']}|{area[y + 1][x + 1]['latitude']}": area[y + 1][x + 1]
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == 0 and x == length - 1:
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}":  area[y][x - 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y + 1][x - 1]['longitude']}|{area[y + 1][x - 1]['latitude']}": area[y + 1][x - 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == width - 1 and x == 0:
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y - 1][x + 1]['longitude']}|{area[y - 1][x + 1]['latitude']}": area[y - 1][x + 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == width - 1 and x == length - 1:
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}": area[y][x - 1]['weight'],
                    f"{area[y - 1][x - 1]['longitude']}|{area[y - 1][x - 1]['latitude']}": area[y - 1][x - 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == 0:
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 1.41
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}": area[y][x - 1]['weight'],
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y + 1][x - 1]['longitude']}|{area[y + 1][x - 1]['latitude']}": area[y + 1][x - 1]['weight'],
                    f"{area[y + 1][x + 1]['longitude']}|{area[y + 1][x + 1]['latitude']}": area[y + 1][x + 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == width - 1:
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 1.41
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}": area[y][x - 1]['weight'],
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y - 1][x - 1]['longitude']}|{area[y - 1][x - 1]['latitude']}": area[y - 1][x - 1]['weight'],
                    f"{area[y - 1][x + 1]['longitude']}|{area[y - 1][x + 1]['latitude']}": area[y - 1][x + 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif x == 0:
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 1.41
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y + 1][x + 1]['longitude']}|{area[y + 1][x + 1]['latitude']}": area[y + 1][x + 1]['weight'],
                    f"{area[y - 1][x + 1]['longitude']}|{area[y - 1][x + 1]['latitude']}": area[y - 1][x + 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif x == length - 1:
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 1.41
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}": area[y][x - 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y - 1][x - 1]['longitude']}|{area[y - 1][x - 1]['latitude']}": area[y - 1][x - 1]['weight'],
                    f"{area[y + 1][x - 1]['longitude']}|{area[y + 1][x - 1]['latitude']}": area[y + 1][x - 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            else:
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 1.41
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 1.41
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 1.41
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 1.41

                nodes = {
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}": area[y][x - 1]['weight'],
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y - 1][x - 1]['longitude']}|{area[y - 1][x - 1]['latitude']}": area[y - 1][x - 1]['weight'],
                    f"{area[y - 1][x + 1]['longitude']}|{area[y - 1][x + 1]['latitude']}": area[y - 1][x + 1]['weight'],
                    f"{area[y + 1][x + 1]['longitude']}|{area[y + 1][x + 1]['latitude']}": area[y + 1][x + 1]['weight'],
                    f"{area[y + 1][x - 1]['longitude']}|{area[y + 1][x - 1]['latitude']}": area[y + 1][x - 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

    return graph
