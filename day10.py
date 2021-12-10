from typing import List

def read_input() -> List[str]:
	with open('inputs/day10.txt') as f:
		lines = f.readlines()
	return [line.strip() for line in lines]

def process_line(line: str) -> (List[str], str):
	stack = []
	for x in line:
		if x == '{' or x == '[' or x == '<' or x == '(':
			stack.append(x)
			continue
		if not stack:
			return stack, x
		top = stack[-1]
		stack = stack[:-1]
		if (top == '{' and x != '}') or (top == '[' and x != ']') or (top == '<' and x != '>') or (top == '(' and x != ')'):
			return stack, x
	return stack, ''

def get_first_error(line: str) -> str:
	_, result = process_line(line)
	return result

p1_scores = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137,
} 
def part_one(lines: List[str]) -> int:
	result = 0
	for line in lines:
		first_error = get_first_error(line)
		if first_error:
			result += p1_scores[first_error]
	return result

def get_closure(line: str) -> str:
	stack, error = process_line(line)
	if error:
		return ''
	result = ''
	for x in reversed(stack):
		if x == '(':
			result += ')'
		elif x == '[':
			result += ']'
		elif x == '{':
			result += '}'
		elif x == '<':
			result += '>'
	return result

p2_scores = {
	')': 1,
	']': 2,
	'}': 3,
	'>': 4,
}
def get_p2_score(closure: str) -> int:
	result = 0
	for x in closure:
		result *= 5
		result += p2_scores[x]
	return result

def part_two(lines: List[str]) -> int:
	scores = []
	for line in lines:
		closure = get_closure(line)
		if closure:
			scores.append(get_p2_score(closure))
	scores.sort()
	return scores[len(scores)//2]

if __name__ == '__main__':
	lines = read_input()
	result_one = part_one(lines)
	print(result_one)
	result_two = part_two(lines)
	print(result_two)
