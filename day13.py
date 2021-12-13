from dataclasses import dataclass
from typing import List, Set, Tuple

@dataclass
class Input(object):
	points: Set[Tuple[int, int]]
	folds: List[Tuple[str, int]]

def read_input() -> Input:
	with open('inputs/day13.txt') as f:
		lines = f.readlines()
	
	points = set()
	index = 0
	while index < len(lines):
		line = lines[index].strip()
		index += 1
		if not line:
			break
		coords = line.split(',')
		points.add((int(coords[0]), int(coords[1])))

	folds = []
	while index < len(lines):
		line = lines[index].strip()
		index += 1
		fold = line.split('=')
		axis = fold[0][-1]
		loc = int(fold[1])
		folds.append((axis, loc))
	return Input(points, folds)

def do_fold(points: Set[Tuple[int, int]], fold: Tuple[str, int]) -> Set[Tuple[int, int]]:
	axis = fold[0]
	loc = fold[1]
	result = set()
	for point in points:
		if axis == 'x':
			if point[0] < loc:
				result.add(point)
			elif point[0] > loc:
				new_x = 2*loc - point[0]
				result.add((new_x, point[1]))
		if axis == 'y':
			if point[1] < loc:
				result.add(point)
			elif point[1] > loc:
				new_y = 2*loc - point[1]
				result.add((point[0], new_y))
	return result

def part_one(paper: Input) -> int:
	return len(do_fold(paper.points, paper.folds[0]))

def print_paper(points: Set[Tuple[int, int]]):
	min_y = min(p[1] for p in points)
	max_y = max(p[1] for p in points)
	min_x = min(p[0] for p in points)
	max_x = max(p[0] for p in points)

	for y in range(min_y, max_y + 1):
		line = ''
		for x in range(min_x, max_x + 1):
			if (x, y) in points:
				line += '#'
			else:
				line += ' '
		print(line) 

def part_two(paper: Input):
	points = paper.points
	for fold in paper.folds:
		points = do_fold(points, fold)
	print_paper(points)

if __name__ == '__main__':
	paper = read_input()
	result_one = part_one(paper)
	print(result_one)
	part_two(paper)
