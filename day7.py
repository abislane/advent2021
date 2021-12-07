from typing import List

def read_input() -> List[int]:
	with open('inputs/day7.txt') as f:
		line = f.readline()
	return [int(x) for x in line.split(',')]

def part_one(crabs: List[int]) -> int:
	min_move = None
	min_pos = min(crabs)
	max_pos = max(crabs)
	for x in range(min_pos, max_pos + 1):
		move = 0
		for y in crabs:
			move += abs(x - y)
		if not min_move:
			min_move = move
		else:
			min_move = min(move, min_move)
	return min_move

def part_two(crabs: List[int]) -> int:
	min_move = None
	min_pos = min(crabs)
	max_pos = max(crabs)
	for x in range(min_pos, max_pos + 1):
		move = 0
		for y in crabs:
			n = abs(x - y)
			move += n * (n + 1) // 2
		if not min_move:
			min_move = move
		else:
			min_move = min(move, min_move)
	return min_move

if __name__ == '__main__':
	crabs = read_input()
	result_one = part_one(crabs)
	print(result_one)
	result_two = part_two(crabs)
	print(result_two)
