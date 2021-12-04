from typing import List

def read_input() -> List[int]:
	with open('inputs/day1.txt') as f:
		lines = f.readlines()
	return [int(line) for line in lines]

def part_one(depths: List[int]) -> int:
	result = 0
	for i in range(1, len(depths)):
		if depths[i] > depths[i-1]:
			result += 1
	return result

def part_two(depths: List[int]) -> int:
	if len(depths) <= 3:
		return 0
	result = 0

	prev_depth = depths[0] + depths[1] + depths[2]
	for i in range(3, len(depths)):
		new_depth = prev_depth - depths[i - 3] + depths[i]
		if new_depth > prev_depth:
			result += 1
		prev_depth = new_depth

	return result

if __name__ == '__main__':
	depths = read_input()
	result_one = part_one(depths)
	print(result_one)
	result_two = part_two(depths)
	print(result_two)