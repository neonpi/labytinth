import sys
import time

from a_star import a_star_search
from backtracking import backtracking_search
from bfs import breadth_first_search
from dfs import depth_limited_search
from greedy import greedy_search
from ida_star import ida_star_search
from maze_parser import read_maze
from ordered_search import ordered_search
from util import print_search_result

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


def run_search(name, search_fn):
    print(f"{name}:")
    start_time = time.perf_counter()
    path, stats = search_fn(maze)
    elapsed_time = time.perf_counter() - start_time
    print_search_result(path, stats, elapsed_time)
    print()


run_search("Backtracking", backtracking_search)
run_search("Busca em Largura", breadth_first_search)
run_search("Busca em Profundidade (Limitada)", depth_limited_search)
run_search("Busca Ordenada", ordered_search)
run_search("Busca Gulosa", greedy_search)
run_search("Busca A*", a_star_search)
run_search("Busca IDA*", ida_star_search)
