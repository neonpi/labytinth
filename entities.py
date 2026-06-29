from dataclasses import dataclass, field


@dataclass
class Node:
    """A node representing a walkable spot in the maze."""

    y: int
    x: int
    edges: list["Node"] = field(default_factory=list["Node"])

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return str(self.y) + "-" + str(self.x)


def are_neighbors(node: Node, other: Node) -> bool:
    return abs(node.y - other.y) + abs(node.x - other.x) == 1


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

        for i, node in enumerate(self.nodes):
            for other in self.nodes[i:]:
                if are_neighbors(node, other):
                    node.edges.append(other)
                    other.edges.append(node)

    def start(self) -> Node:
        return self.nodes[0]

    def exit(self) -> Node:
        return self.nodes[-1]


def is_start(maze: Maze, node: Node) -> bool:
    return node == maze.start()


def is_exit(maze: Maze, node: Node) -> bool:
    return node == maze.exit()
