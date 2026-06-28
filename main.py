import sys

from maze_parser import read_maze

input_file = ""

if len(sys.argv) == 1:
    input_file = "10x10-valid-input.txt"
else:
    input_file = sys.argv[1]

try:
    maze = read_maze(input_file)
except FileNotFoundError:
    print(f"Error: file '{input_file}' not found")
