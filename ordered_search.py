import heapq

from entities import Maze, Node, is_exit
from stats import SearchStats
from util import get_visited_dict, reconstruct_path


def ordered_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    visited = get_visited_dict(maze)
    counter = 0
    heap: list[tuple[int, int, Node]] = [(0, 0, maze.start())]
    parent: dict[Node, Node] = {}
    cost: dict[Node, int] = {maze.start(): 0}
    stats = SearchStats()

    while heap:
        _, _, node = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        stats.nodes_expanded += 1

        if is_exit(maze, node):
            break

        for neighbor in node.edges:
            stats.nodes_visited += 1
            new_cost = cost[node] + 1
            if not visited[neighbor] and (
                neighbor not in cost or new_cost < cost[neighbor]
            ):
                cost[neighbor] = new_cost
                parent[neighbor] = node
                counter += 1
                heapq.heappush(heap, (new_cost, counter, neighbor))

    return reconstruct_path(parent, maze.exit()), stats
