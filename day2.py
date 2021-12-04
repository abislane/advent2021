from dataclasses import dataclass 
from typing import List

@dataclass
class Step(object):
	direction: str
	magnitude: int

def read_input() -> List[Step]:
	with open('inputs/day2.txt') as f:
		lines = f.readlines()
	result = []
	for line in lines:
		parts = line.split()
		result.append(Step(parts[0], int(parts[1])))
	return result

def part_one(steps: List[Step]) -> int:
	horiz = 0
	depth = 0
	for step in steps:
		if step.direction == 'forward':
			horiz += step.magnitude
		elif step.direction == 'down':
			depth += step.magnitude
		elif step.direction == 'up':
			depth -= step.magnitude
	return horiz * depth

if __name__ == '__main__':
	steps = read_input()
	result_one = part_one(steps)
	print(result_one)
