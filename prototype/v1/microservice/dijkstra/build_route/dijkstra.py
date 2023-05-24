def dijkstra(graph, start, goal):
    shortest_distance = {} #records the cost to reach to that node. Going to be updated as we mode long the graph
    track_predecessor = {} #Keep check of the path that has led us to this node
    unseenNodes = graph #to iterate through the entire graph
    infinity = float('inf') #infinity can basicaly be considered a very large number
    track_path = [] #going to trace our journey back to the source node optimal route

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node

            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print("Path is not reachable")
            break

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity:
        return track_path