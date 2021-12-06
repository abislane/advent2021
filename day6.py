from typing import List

def read_input() -> List[int]:
	with open('inputs/day6.txt') as f:
		line = f.readline()
	return [int(x) for x in line.split(',')]

def simulate(fish: List[int], days: int) -> int:
	# on day n, create next_add which is day n + 1s number
	per_day = [0,0,0,0,0,0,0,0,0]
	for x in fish:
		per_day[x] += 1

	for day in range(days):
		zero = per_day[0]
		per_day = per_day[1:]
		per_day[6] += zero
		per_day.append(zero)
	return sum(per_day)

def part_one(fish: List[int]) -> int:
	return simulate(fish, 80)

def part_two(fish: List[int]) -> int:
	return simulate(fish, 256)


if __name__ == '__main__':
	fish = read_input()
	result_one = part_one(fish)
	print(result_one)
	result_two = part_two(fish)
	print(result_two)