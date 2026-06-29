from entities import Maze, Node, is_end
from util import euclidian_distance, get_visited_dict


def greedy_search(maze: Maze) -> list[Node]:
    """Performs a greedy search for the maze's exit using the euclidian distance of each
    candidate node to the exit as the heuristic."""

    visited = get_visited_dict(maze)
    path: list[Node] = []
    stack = [maze.start()]
    found = False

    while stack and not found:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        path.append(node)

        if is_end(maze, node):
            found = True
            continue

        unvisited_neighbors = sorted(
            [n for n in node.edges if not visited[n]],
            key=lambda n: euclidian_distance(n, maze.exit()),
            reverse=True
        )

        for neighbor in unvisited_neighbors:
            stack.append(neighbor)

    if found:
        return path
    return []
