import math


def shortest_path(M, start, goal):
    frontier_list, intersections_list, shortest_path_dict = [], [], {}
    f, g, h = {}, {}, {}

    frontier_list.append(start)

    g[start] = 0
    h[start] = get_distance(M.intersections[start], M.intersections[goal])
    f[start] = g[start] + h[start]

    while len(frontier_list) > 0:
        current_node = frontier_list[0]

        for node in frontier_list:
            if f[node] < f[current_node]:
                current_node = node

        if current_node == goal:
            path_list = []
            path_list.append(goal)
            next = goal

            while next != start:
                next = shortest_path_dict[next]
                path_list.append(next)

            path_list.reverse()

            return path_list

        intersections_list.append(current_node)
        frontier_list.remove(current_node)

        for node in M.roads[current_node]:
            if node in intersections_list:
                continue

            g_node = g[current_node] + get_distance(
                M.intersections[current_node], M.intersections[node]
            )

            if node not in frontier_list:
                frontier_list.append(node)

            elif g_node >= g[node]:
                continue

            g[node] = g_node
            h[node] = get_distance(M.intersections[node], M.intersections[goal])
            f[node] = g[node] + h[node]

            shortest_path_dict[node] = current_node

    return None


def get_distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
