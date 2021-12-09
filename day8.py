from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Line(object):
	in_digits: List[str]
	out_digits: List[str]

def read_input() -> List[Line]:
	with open('inputs/day8.txt') as f:
		lines = f.readlines()
	digits = []
	for line in lines:
		in_out = line.strip().split(' | ')
		digits.append(Line(in_out[0].split(' '), in_out[1].split(' ')))
	return digits

def part_one(lines: List[Line]) -> int:
	result = 0
	for line in lines:
		for word in line.out_digits:
			size = len(word)
			if size == 2 or size == 3 or size == 4 or size == 7:
				result += 1
	return result

nums = {
	'abcefg': '0',
	'cf': '1',
	'acdeg': '2',
	'acdfg': '3',
	'bcdf': '4',
	'abdfg': '5',
	'abdefg': '6',
	'acf': '7',
	'abcdefg': '8',
	'abcdfg': '9',
}

def find_map(in_digits: List[str]) -> Dict[str, str]:
	result = {}
	found_set = set()
	digits_by_length = defaultdict(list)
	for digit in in_digits:
		digits_by_length[len(digit)].append(digit)
	one = set(digits_by_length[2][0])
	seven = set(digits_by_length[3][0])
	four = set(digits_by_length[4][0])
	eight = set(digits_by_length[7][0])

	top = (seven - one).pop()
	found_set.add(top)
	result[top] = 'a'

	intersect_five = set(digits_by_length[5][0])
	for five in digits_by_length[5]:
		intersect_five &= set(five)

	bottom = ((intersect_five - four) - found_set).pop()
	found_set.add(bottom)
	result[bottom] = 'g'

	middle = (intersect_five - found_set).pop()
	found_set.add(middle)
	result[middle] = 'd'

	top_left = ((four - one) - found_set).pop()
	found_set.add(top_left)
	result[top_left] = 'b'

	for five in digits_by_length[5]:
		remain = set(five) - found_set
		if len(remain) == 1:
			bottom_right = remain.pop()
			found_set.add(bottom_right)
			result[bottom_right] = 'f'
			break

	for three in digits_by_length[5]:
		remain = set(three) - found_set
		if len(remain) == 1:
			top_right = remain.pop()
			found_set.add(top_right)
			result[top_right] = 'c'
			break

	bottom_left = (eight - found_set).pop()
	found_set.add(bottom_left)
	result[bottom_left] = 'e'
	return result

def parse_result(out_digits: List[str], segement_map: Dict[str, str]) -> int:
	result = ''
	for digit in out_digits:
		new_segments = [segement_map[x] for x in digit]
		result += nums[''.join(sorted(new_segments))]
	return int(result)


def part_two(lines: List[Line]) -> int:
	result = 0
	for line in lines:
		segement_map = find_map(line.in_digits)
		result += parse_result(line.out_digits, segement_map)
	return result


if __name__ == '__main__':
	lines = read_input()
	result_one = part_one(lines)
	print(result_one)
	result_two = part_two(lines)
	print(result_two)