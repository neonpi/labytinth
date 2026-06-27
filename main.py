import sys

from parser import read_maze

input_file = ""

if len(sys.argv) == 1:
    input_file = "10x10-valid-input.txt"

graph = read_maze(input_file)
