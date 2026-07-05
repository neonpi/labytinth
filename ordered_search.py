import heapq

from entities import Maze, Node, is_exit
from util import get_visited_dict, reconstruct_path


def ordered_search(maze: Maze) -> list[Node]:
    visited = get_visited_dict(maze)
    counter = 0
    heap: list[tuple[int, int, Node]] = [(0, 0, maze.start())]
    parent: dict[Node, Node] = {}
    cost: dict[Node, int] = {maze.start(): 0}

    while heap:
        _, _, node = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True

        if is_exit(maze, node):
            break

        for neighbor in node.edges:
            new_cost = cost[node] + 1
            if not visited[neighbor] and (
                neighbor not in cost or new_cost < cost[neighbor]
            ):
                cost[neighbor] = new_cost
                parent[neighbor] = node
                counter += 1
                heapq.heappush(heap, (new_cost, counter, neighbor))

    return reconstruct_path(parent, maze.exit())
