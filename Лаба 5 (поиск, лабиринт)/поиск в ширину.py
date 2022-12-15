import timeit

graph = {1: set([2, 3, 4]),
         2: set([5, 6]),
         3: set([]),
         4: set([7, 8]),
         5: set([9, 10]),
         6: set([]),
         7: set([11, 12]),
         8: set([]),
         9: set([]),
         10: set([]),
         11: set([]),
         12: set([]),
         }


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


start_time = timeit.default_timer()
print('Кратчайший путь', shortest_path(graph, int(input('Введите начало:')), int(input('Введите конец:'))))
end_time = timeit.default_timer() - start_time

print('Время выполнения поиска кратчайшего пути (BFS)', end_time)
