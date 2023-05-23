from app.tools.weight import get_weight


def create(area, iceclass):
    width = len(area)
    length = len(area[0])

    graph = {}

    for y in range(width):
        for x in range(length):
            if y == 0 and x == 0:
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 3

                nodes = {
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y + 1][x + 1]['longitude']}|{area[y + 1][x + 1]['latitude']}": area[y + 1][x + 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == 0 and x == length - 1:
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y + 1][x]['weight'] = get_weight(area[y][x], area[y + 1][x],  iceclass) + 1
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 3

                nodes = {
                    f"{area[y][x - 1]['longitude']}|{area[y][x - 1]['latitude']}":  area[y][x - 1]['weight'],
                    f"{area[y + 1][x]['longitude']}|{area[y + 1][x]['latitude']}": area[y + 1][x]['weight'],
                    f"{area[y + 1][x - 1]['longitude']}|{area[y + 1][x - 1]['latitude']}": area[y + 1][x - 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == width - 1 and x == 0:
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y][x + 1]['weight'] = get_weight(area[y][x], area[y][x + 1],  iceclass) + 1
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 3

                nodes = {
                    f"{area[y - 1][x]['longitude']}|{area[y - 1][x]['latitude']}": area[y - 1][x]['weight'],
                    f"{area[y][x + 1]['longitude']}|{area[y][x + 1]['latitude']}": area[y][x + 1]['weight'],
                    f"{area[y - 1][x + 1]['longitude']}|{area[y - 1][x + 1]['latitude']}": area[y - 1][x + 1]['weight']
                }

                graph[f"{area[y][x]['longitude']}|{area[y][x]['latitude']}"] = nodes

            elif y == width - 1 and x == length - 1:
                area[y - 1][x]['weight'] = get_weight(area[y][x], area[y - 1][x],  iceclass) + 1
                area[y][x - 1]['weight'] = get_weight(area[y][x], area[y][x - 1],  iceclass) + 1
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 3

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
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 3
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 3

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
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 3
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 3

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
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 3
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 3

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
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 3
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 3

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
                area[y - 1][x - 1]['weight'] = get_weight(area[y][x], area[y - 1][x - 1],  iceclass) + 3
                area[y - 1][x + 1]['weight'] = get_weight(area[y][x], area[y - 1][x + 1],  iceclass) + 3
                area[y + 1][x + 1]['weight'] = get_weight(area[y][x], area[y + 1][x + 1],  iceclass) + 3
                area[y + 1][x - 1]['weight'] = get_weight(area[y][x], area[y + 1][x - 1],  iceclass) + 3

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

    # counter = 0
    #
    # for k_el, v_el in list(graph.items()):
    #     counter = counter + 1
    #     for k, v in list(v_el.items()):
    #         counter = counter + 1
    #
    # print(counter)
    #
    # counter = 0
    # new_graph = {}
    # for k_el, v_el in list(graph.items()):
    #     new_graph[k_el] = {}
    #     for k, v in list(v_el.items()):
    #         if v == 10000:
    #             pass
    #         elif v == 10000.41:
    #             pass
    #         else:
    #             new_graph[k_el][k] = v
    #     # for k, value in list(graph[el].items()):
    #     #     if value == 10000:
    #     #         del graph[el][k]
    #     #     elif value == 10000.41:
    #     #         del graph[el][k]
    #
    # for k_el, v_el in list(new_graph.items()):
    #     counter = counter + 1
    #     for k, v in list(v_el.items()):
    #         counter = counter + 1
    #
    # print(counter)
    return graph
