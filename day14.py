from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class Input(object):
	sequence: str
	transforms: Dict[str, str]

def read_input() -> Input:
	with open('inputs/day14.txt') as f:
		lines = f.readlines()
	sequence = lines[0].strip()

	transforms = {}
	for index in range(2, len(lines)):
		parts = lines[index].strip().split(' -> ')
		transforms[parts[0]] = parts[1]
	return Input(sequence, transforms)

# Add dict2 into dict1 (note: assumes defaultdicts)
def add_dicts(dict1: Dict[str, int], dict2: Dict[str, int]):
	for key in dict2:
		if key not in dict1:
			dict1[key] = 0
		dict1[key] += dict2[key]

# memoizes find_freqs
cache: Dict[Tuple[str, str, int], Dict[str, int]] = {}
# given two characters, finds the frequency of characters between them if transformed are performed a number of times
def find_freqs_rec(start: str, end: str, transforms: Dict[str, str], times: int) -> Dict[str, int]:
	if times == 0:
		return {}
	if (start, end, times) in cache:
		return cache[(start, end, times)]

	middle = transforms[start + end]
	result = {middle: 1}
	dict1 = find_freqs_rec(start, middle, transforms, times - 1)
	add_dicts(result, dict1)
	dict2 = find_freqs_rec(middle, end, transforms, times - 1)
	add_dicts(result, dict2)
	cache[(start, end, times)] = result
	return result

def find_freqs(sequence: str, transforms: Dict[str, str], times: int) -> Dict[str, int]:
	result = {}
	for index in range(len(sequence) - 1):
		new_dict = find_freqs_rec(sequence[index], sequence[index + 1], transforms, times)
		add_dicts(result, new_dict)
	
	for x in sequence:
		if x not in result:
			result[x] = 0
		result[x] += 1
	return result 


def part_one(parsed_input: Input) -> int:
	freqs = find_freqs(parsed_input.sequence, parsed_input.transforms, 10)
	return max(freqs.values()) - min(freqs.values())

def part_two(parsed_input: Input) -> int:
	freqs = find_freqs(parsed_input.sequence, parsed_input.transforms, 40)
	return max(freqs.values()) - min(freqs.values())

if __name__ == '__main__':
	parsed_input = read_input()
	result_one = part_one(parsed_input)
	print(result_one)
	result_two = part_two(parsed_input)
	print(result_two)
