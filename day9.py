from math import prod
from queue import Queue
from typing import List, Tuple

class Grid(object):
	def __init__(self, nums: List[List[int]]):
		self.nums = nums
		self.rows = len(nums)
		self.cols = len(nums[0])
		self.marked = [[False for _ in range(self.cols)] for _ in range(self.rows)]

def read_input() -> Grid:
	with open('inputs/day9.txt') as f:
		lines = f.readlines()
	return Grid([[int(x) for x in line.strip()] for line in lines])

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def get_neighbors(grid: Grid, row: int, col: int) -> List[Tuple[int, int]]:
	neighbors = []
	for direc in dirs:
		x = row + direc[0]
		y = col + direc[1]
		if x >= 0 and x < grid.rows and y >= 0 and y < grid.cols:
			neighbors.append((x, y))
	return neighbors

def is_low_point(grid: Grid, row: int, col: int) -> bool:
	neighbors = get_neighbors(grid, row, col)
	heights = [grid.nums[n[0]][n[1]] for n in neighbors]
	return grid.nums[row][col] < min(heights)

def part_one(grid: Grid) -> int:
	result = 0
	for row in range(grid.rows):
		for col in range(grid.cols):
			if is_low_point(grid, row, col):
				result += grid.nums[row][col] + 1
	return result

def bfs(grid: Grid, start: Tuple[int, int]) -> int:
	queue = Queue()
	queue.put(start)
	size = 0
	while not queue.empty():
		top = queue.get()
		if grid.marked[top[0]][top[1]]:
			continue
		if grid.nums[top[0]][top[1]] == 9:
			continue

		grid.marked[top[0]][top[1]] = True
		size += 1
		for n in get_neighbors(grid, top[0], top[1]):
			queue.put(n)
	return size


def part_two(grid: Grid) -> int:
	basin_sizes = []
	for row in range(grid.rows):
		for col in range(grid.cols):
			if grid.marked[row][col] or grid.nums[row][col] == 9:
				continue
			basin_size = bfs(grid, (row, col))
			basin_sizes.append(basin_size)
	return prod(sorted(basin_sizes, reverse=True)[:3])

if __name__ == '__main__':
	grid = read_input()
	result_one = part_one(grid)
	print(result_one)
	result_two = part_two(grid)
	print(result_two)
