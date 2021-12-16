import heapq

from typing import List

def read_input() -> List[List[str]]:
	with open('inputs/day15.txt') as f:
		lines = f.readlines()
	return [[int(x) for x in line.strip()] for line in lines]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dijkstra(grid: List[List[int]]) -> int:
	rows = len(grid)
	cols = len(grid[0])
	dist = [[2**32 for _ in line] for line in grid]

	dist[0][0] = 0
	queue = [(0, (0, 0))]
	while queue:
		top_dist, top = heapq.heappop(queue)
		if top_dist > dist[top[0]][top[1]]:
			# old item, disregard
			continue
		for direc in dirs:
			newrow = top[0] + direc[0]
			newcol = top[1] + direc[1]
			if newrow < 0 or newcol < 0 or newrow >= rows or newcol >= cols:
				continue
			alt = dist[top[0]][top[1]] + grid[newrow][newcol]
			if alt < dist[newrow][newcol]:
				dist[newrow][newcol] = alt
				heapq.heappush(queue, (alt, (newrow, newcol)))

	return dist[rows - 1][cols - 1]

def part_one(grid: List[List[int]]) -> int:
	return dijkstra(grid)

def enlarge_grid(grid: List[List[int]]) -> int:
	rows = len(grid)
	cols = len(grid[0])

	result = [[0 for _ in range(5 * cols)] for _ in range(5 * rows)]
	for a in range(rows):
		for b in range(cols):
			for c in range(5):
				for d in range(5):
					item = grid[a][b] + c + d
					if item >= 10:
						item -= 9
					result[a + c*rows][b + d*cols] = item
	return result 

def part_two(grid: List[List[int]]) -> int:
	grid = enlarge_grid(grid)
	return dijkstra(grid)

if __name__ == '__main__':
	grid = read_input()
	result_one = part_one(grid)
	print(result_one)
	result_two = part_two(grid)
	print(result_two)