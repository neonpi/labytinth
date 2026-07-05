import sys

from a_star import a_star_search
from greedy import greedy_search
from ida_star import ida_star_search
from maze_parser import read_maze
from util import print_constructed_path

input_file = ""

if len(sys.argv) == 1:
    input_file = "8x8-valid-input.txt"
else:
    input_file = sys.argv[1]

try:
    maze = read_maze(input_file)
except FileNotFoundError:
    print(f"Error: file '{input_file}' not found")
    sys.exit(1)

print("Greedy:")
print_constructed_path(greedy_search(maze))
print("A*:")
print_constructed_path(a_star_search(maze))
print("IDA*:")
print_constructed_path(ida_star_search(maze))
