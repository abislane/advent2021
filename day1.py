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

if __name__ == '__main__':
	depths = read_input()
	result_one = part_one(depths)
	print(result_one)