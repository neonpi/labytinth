import heapq
from itertools import count

from entities import Maze, Node, is_exit
from stats import SearchStats
from util import distance, reconstruct_path


def a_star_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    """Performs the A* search of start to exit of the given maze returning the path constructed
    during the process"""
    tie_breaker = count()  # avoids comparing Node objects on f-value ties in the heap
    open_heap: list[tuple[int, int, Node]] = []
    closed: set[Node] = set()
    parent: dict[Node, Node] = {}
    g_evaluation: dict[Node, int] = {}
    stats = SearchStats()

    g_evaluation[maze.start()] = 0
    heapq.heappush(open_heap, (distance(maze.start(), maze.exit()), next(tie_breaker), maze.start()))

    while open_heap:
        _, _, node = heapq.heappop(open_heap)

        if node in closed:
            continue  # stale entry left over from a worse path, already finalized

        stats.nodes_expanded += 1

        if is_exit(maze, node):
            break

        closed.add(node)

        for neighbor in node.edges:
            stats.nodes_visited += 1
            if neighbor in closed:
                continue

            temp_g = g_evaluation[node] + 1  # we're not using weighted edges

            if neighbor in g_evaluation and temp_g >= g_evaluation[neighbor]:
                continue  # worse path than the one to be explored later

            parent[neighbor] = node
            g_evaluation[neighbor] = temp_g
            f = temp_g + distance(neighbor, maze.exit())
            heapq.heappush(open_heap, (f, next(tie_breaker), neighbor))

    return reconstruct_path(parent, maze.exit()), stats
