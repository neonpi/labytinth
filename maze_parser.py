from entities import Maze, Node


def read_maze(file_path: str) -> Maze:
    """Reads from input file and creates the equivalent graph.

    Arguments:
    file_path -- the absolute or relative file path of the file defining the desired maze
    """
    nodes: list[Node] = []
    width: int
    height: int

    with open(file=file_path, mode="r", encoding="utf_8") as file:
        dimensions_line = file.readline()
        dimensions = [int(number) for number in dimensions_line.strip().split(" ")]
        width = dimensions[0]
        height = dimensions[1]
        validate_maze_dimensions(width, height)

        lines = [line.replace("\n", "").replace("\r", "") for line in file.readlines()]
        check_line_amount_against_height(len(lines), height)
        entry_count = 0
        exit_count = 0

        for i, line in enumerate(lines):
            check_line_against_set_width(i, line, width)

            for j, char in enumerate(line):
                if char not in ["A", "B", " ", "#"]:
                    raise ValueError(
                        "Only allowed characters in maze definition are: '#', 'A', 'B' and ' ' (blank space)"
                    )

                if char == "A":
                    entry_count += 1
                if char == "B":
                    exit_count += 1
                if char == " ":
                    node = Node(x=j, y=i)
                    nodes.append(node)

    if entry_count != 1:
        raise ValueError("There should be exactly one entry.")
    if exit_count != 1:
        raise ValueError("There should be exactly one exit.")

    maze = Maze(height=height, width=width, nodes=nodes)

    return maze


def check_line_amount_against_height(line_amount: int, height: int):
    if line_amount != height:
        raise ValueError(
            "Expected and actual (line amount) heights for the maze are different. Expected: {}, got: {}".format(
                height, line_amount
            )
        )


def check_line_against_set_width(position: int, line: str, width: int):
    if len(line) != width:
        raise ValueError(
            "There are more columns in line {}:'{}' than the set width for the maze. Expected: {}, got: {}".format(
                position, line, width, len(line)
            )
        )


def validate_maze_dimensions(width: int, height: int):
    if width < 1 or height < 1:
        raise ValueError(
            "Dimensions must be positive. W = {0}, H = {1} isn't allowed.".format(
                width, height
            )
        )
    if width == 1 and height == 1:
        raise ValueError(
            "Maze area must be larger than 1 square unit. W = 1, H = 1 aren't allowed"
        )
