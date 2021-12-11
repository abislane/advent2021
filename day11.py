from copy import deepcopy
from queue import Queue
from typing import List, Tuple

def read_input() -> List[List[int]]:
	with open('inputs/day11.txt') as f:
		lines = f.readlines()
	return [[int(x) for x in line.strip()] for line in lines]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
def neighbors(pt: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
	result = []
	for direc in dirs:
		x = pt[0] + direc[0]
		y = pt[1] + direc[1]

		if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
			result.append((x, y))
	return result

def simulate_step(grid: List[List[int]]) -> int:
	flashes = set()
	to_flash = Queue()
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			grid[row][col] += 1
			if grid[row][col] > 9:
				flashes.add((row, col))
				to_flash.put((row, col))

	while not to_flash.empty():
		top = to_flash.get()
		for n in neighbors(top, grid):
			if n in flashes:
				continue
			grid[n[0]][n[1]] += 1
			if grid[n[0]][n[1]] > 9:
				flashes.add(n)
				to_flash.put(n)

	for flash in flashes:
		grid[flash[0]][flash[1]] = 0
	return len(flashes)

def part_one(grid: List[List[int]]) -> int:
	result = 0
	for _ in range(100):
		result += simulate_step(grid)
	return result

def part_two(grid: List[List[int]]) -> int:
	print_grid(grid)
	total = len(grid) * len(grid[0])
	index = 1
	while True:
		result = simulate_step(grid)
		if result == total:
			return index
		index += 1

if __name__ == '__main__':
	grid = read_input()
	result_one = part_one(deepcopy(grid))
	print(result_one)
	result_two = part_two(deepcopy(grid))
	print(result_two)