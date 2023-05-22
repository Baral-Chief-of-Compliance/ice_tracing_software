from build_route.enter_path import enter_path
import sys


def dijkstra(graph, src, dest, visited=[], distances={}, predecessors={}):
    print(f"пункт назначение (dest): {dest}")
    print(f"источник (src): {src}")
    print(predecessors)
    sys.setrecursionlimit(10000)
    if src not in graph:
        raise TypeError("The root of the shortest path tree cannot be found")
    if dest not in graph:
        raise TypeError("The root of the shortest path tree cannot be found")
    if src == dest:
        path = []
        pred = dest
        while pred != None:
            path.append(pred)
            pred = predecessors.get(pred, None)
            readable = path[0]

        for index in range(1, len(path)): readable = path[index]+'--->'+readable
        print('shortest path - array: '+str(path))
        print("path: "+readable+", cost="+str(distances[dest]))
        enter_path(path)

    else:
        if not visited:
            distances[src] = 0

        for neighbor in graph[src]:
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src

        visited.append(src)
        unvisited = {}

        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k, float('inf'))

        x = min(unvisited, key=unvisited.get)
        dijkstra(graph, x, dest, visited, distances, predecessors)
