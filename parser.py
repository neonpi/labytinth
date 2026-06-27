def read_maze(file_path: str) -> list[list[int]]:
    """
    Parse input files to an in-memory graph representation
    """
    graph = [[1]]  # TODO remove placeholder
    with open(file=file_path, encoding="utf_8") as file:
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
            for char in line:
                if char == "S":
                    exit_count += 1
                if char == "E":
                    entry_count += 1

        if entry_count != 1:
            raise ValueError("There should be exactly one entry.")
        if exit_count != 1:
            raise ValueError("There should be exactly one exit.")

    return graph


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
    """
    Checks if the dimensions set in the first line of the file passed as argument are valid
    """
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
