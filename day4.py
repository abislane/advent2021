from dataclasses import dataclass
from typing import List, Optional

class Board(object):
	def __init__(self, nums: List[List[int]]):
		self.nums = nums
		self.marked = [[False for _ in range(5)] for _ in range(5)]

	def mark(self, num: int):
		for row in range(5):
			for col in range(5):
				if self.nums[row][col] == num:
					self.marked[row][col] = True

	def is_complete(self) -> bool:
		"""Check if there is a bingo, and return the contents of the winning line"""
		# check rows
		for row in range(5):
			if all(self.marked[row]):
				return True

		# check cols
		for col in range(5):
			if all([self.marked[row][col] for row in range(5)]):
				return True

		return False

	def sum_unmarked(self) -> int:
		result = 0
		for row in range(5):
			for col in range(5):
				if not self.marked[row][col]:
					result += self.nums[row][col]
		return result

	def reset(self):
		self.marked = [[False for _ in range(5)] for _ in range(5)]

@dataclass
class BingoInput:
	sequence: List[int]
	boards: List[Board]

	def reset(self):
		for board in self.boards:
			board.reset()

def read_input() -> BingoInput:
	with open('inputs/day4.txt') as f:
		lines = f.readlines()
	sequence = [int(x) for x in lines[0].split(',')]

	boards = []
	line_index = 2
	while line_index < len(lines):
		nums = []
		for index in range(line_index, line_index + 5):
			nums.append([int(x) for x in lines[index].split()])
		boards.append(Board(nums))
		line_index += 6
	return BingoInput(sequence, boards)

def part_one(bingo: BingoInput) -> int:
	bingo.reset()
	for x in bingo.sequence:
		for board in bingo.boards:
			board.mark(x)
			if board.is_complete():
				return board.sum_unmarked() * x
	return -1

def part_two(bingo: BingoInput) -> int:
	bingo.reset()
	won = [False for _ in bingo.boards]
	remaining = len(bingo.boards)
	for x in bingo.sequence:
		for index in range(len(bingo.boards)):
			if won[index]:
				continue
			bingo.boards[index].mark(x)
			if bingo.boards[index].is_complete():
				won[index] = True
				remaining -= 1
				if remaining == 0:
					return bingo.boards[index].sum_unmarked() * x
	return -1


if __name__ == '__main__':
	bingo = read_input()
	result_one = part_one(bingo)
	print(result_one)
	result_two = part_two(bingo)
	print(result_two)