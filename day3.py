from typing import List

def read_input() -> List[List[int]]:
	with open('inputs/day3.txt') as f:
		lines = f.readlines()
	result = []
	for line in lines:
		result.append([int(c) for c in line.strip()])
	return result

def part_one(lines: List[List[int]]) -> int:
	gamma = 0
	epsilon = 0
	for index in range(len(lines[0])):
		ones = 0
		zeros = 0
		for row in lines:
			if row[index] == 1:
				ones += 1
			else:
				zeros += 1
		gamma *= 2
		epsilon *= 2
		if ones > zeros:
			gamma += 1
		else:
			epsilon += 1
	return gamma * epsilon

if __name__ == '__main__':
	lines = read_input()
	result_one = part_one(lines)
	print(result_one)
