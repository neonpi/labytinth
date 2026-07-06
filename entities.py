from dataclasses import dataclass, field


@dataclass
class Node:
    """A node representing a walkable spot in the maze."""

    y: int
    x: int
    edges: list["Node"] = field(default_factory=list["Node"])

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return str(self.y) + "-" + str(self.x)


@dataclass
class Maze:
    """Maze represented as a graph with its recorded dimensions."""

    width: int
    height: int
    nodes: list[Node]

    def __init__(self, width: int, height: int, nodes: list[Node]):
        self.width = width
        self.height = height
        self.nodes = nodes

        by_coords = {(node.x, node.y): node for node in self.nodes}
        for node in self.nodes:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                neighbor = by_coords.get((node.x + dx, node.y + dy))
                if neighbor is not None:
                    node.edges.append(neighbor)

    def start(self) -> Node:
        return self.nodes[0]

    def exit(self) -> Node:
        return self.nodes[-1]


def is_start(maze: Maze, node: Node) -> bool:
    return node == maze.start()


def is_exit(maze: Maze, node: Node) -> bool:
    return node == maze.exit()
