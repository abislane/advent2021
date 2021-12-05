from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Tuple

@dataclass
class Line:
	start: (int, int)
	end: (int, int)

def read_input() -> List[Line]:
	with open('inputs/day5.txt') as f:
		lines = f.readlines()
	result = []
	for line in lines:
		points = line.split(' -> ')
		start = points[0].split(',')
		start = (int(start[0]), int(start[1]))
		end = points[1].split(',')
		end = (int(end[0]), int(end[1]))
		result.append(Line(start, end))
	return result

def sign(x: int) -> int:
	if x < 0:
		return -1
	elif x == 0:
		return 0
	else:
		return 1

def add_line(line: Line, point_map: Dict[Tuple[int, int], int]) -> Dict[Tuple[int, int], int]:
	x_sign = sign(line.end[0] - line.start[0])
	y_sign = sign(line.end[1] - line.start[1])

	x = line.start[0]
	y = line.start[1]
	while x != line.end[0] + x_sign or y != line.end[1] + y_sign:
		point_map[(x, y)] += 1
		x += x_sign
		y += y_sign
	return point_map

def count_overlaps(point_map: Dict[Tuple[int, int], int]) -> int:
	return sum(1 for point in point_map if point_map[point] > 1)

def part_one(lines: List[Line]) -> int:
	point_map = defaultdict(int)
	for line in lines:
		if line.start[0] == line.end[0] or line.start[1] == line.end[1]:
			point_map = add_line(line, point_map)

	return count_overlaps(point_map)

def part_two(lines: List[Line]) -> int:
	point_map = defaultdict(int)
	for line in lines:
		point_map = add_line(line, point_map)

	return count_overlaps(point_map)

if __name__ == '__main__':
	lines = read_input()
	result_one = part_one(lines)
	print(result_one)
	result_two = part_two(lines)
	print(result_two)