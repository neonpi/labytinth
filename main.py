import sys

from parser import read_maze

input_file = ""

if len(sys.argv) == 1:
    input_file = "10x10-valid-input.txt"
else:
    input_file = sys.argv[1]

maze = read_maze(input_file)
