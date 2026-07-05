from entities import Maze, Node, is_exit
from util import get_visited_dict, reconstruct_path


def depth_first_search(maze: Maze) -> list[Node]:
    visited = get_visited_dict(maze)
    stack = [maze.start()]
    parent: dict[Node, Node] = {}

    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if is_exit(maze, node):
            break
        for neighbor in node.edges:
            if not visited[neighbor]:
                parent[neighbor] = node
                stack.append(neighbor)

    return reconstruct_path(parent, maze.exit())
