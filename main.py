import sys

from a_star import a_star_search
from backtracking import backtracking_search
from bfs import breadth_first_search
from dfs import depth_limited_search
from greedy import greedy_search
from ida_star import ida_star_search
from maze_parser import read_maze
from ordered_search import ordered_search
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

print("Backtracking:")
print_constructed_path(backtracking_search(maze))
print("Busca em Largura:")
print_constructed_path(breadth_first_search(maze))
print("Busca em Profundidade (Limitada):")
print_constructed_path(depth_limited_search(maze))
print("Busca Ordenada:")
print_constructed_path(ordered_search(maze))
print("Busca Gulosa:")
print_constructed_path(greedy_search(maze))
print("Busca A*:")
print_constructed_path(a_star_search(maze))
print("Busca IDA*:")
print_constructed_path(ida_star_search(maze))
