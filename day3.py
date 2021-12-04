from typing import List

def read_input() -> List[List[int]]:
	with open('inputs/day3.txt') as f:
		lines = f.readlines()
	result = []
	for line in lines:
		result.append([int(c) for c in line.strip()])
	return result

def count_bits(lines: List[List[int]], index: int) -> (int, int):
	ones = 0
	zeros = 0
	for row in lines:
		if row[index] == 1:
			ones += 1
		else:
			zeros += 1
	return (zeros, ones)

def bin_to_dec(bits: List[int]) -> int:
	result = 0
	for bit in bits:
		result *= 2
		result += bit
	return result

def part_one(lines: List[List[int]]) -> int:
	gamma = []
	epsilon = []
	for index in range(len(lines[0])):
		zeros, ones = count_bits(lines, index)
		if ones > zeros:
			gamma.append(1)
			epsilon.append(0)
		else:
			gamma.append(0)
			epsilon.append(1)
	gamma = bin_to_dec(gamma)
	epsilon = bin_to_dec(epsilon)
	return gamma * epsilon

def get_part_two_rating(lines: List[List[int]], high: bool) -> int:
	line_len = len(lines[0])
	for index in range(line_len):
		if len(lines) == 1:
			break
		zeros, ones = count_bits(lines, index)
		target = 1 if (high and ones >= zeros) or (not high and ones < zeros) else 0
		lines = list(filter(lambda line: line[index] == target, lines))
	return bin_to_dec(lines[0])

def part_two(lines: List[List[int]]) -> int:
	oxygen = get_part_two_rating(lines, True)
	co2 = get_part_two_rating(lines, False)
	return oxygen * co2

if __name__ == '__main__':
	lines = read_input()
	result_one = part_one(lines)
	print(result_one)
	result_two = part_two(lines)
	print(result_two)
