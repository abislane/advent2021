from collections import defaultdict
from copy import copy
from queue import Queue
from typing import Dict, List

def read_input() -> Dict[str, str]:
	with open('inputs/day12.txt') as f:
		lines = f.readlines()
	result = defaultdict(list)
	for line in lines:
		nodes = line.strip().split('-')
		result[nodes[0]].append(nodes[1])
		result[nodes[1]].append(nodes[0])
	return result

def part_one(adj_map: Dict[str, str]) -> int:
	result = 0
	queue = Queue()
	queue.put(['start'])
	while not queue.empty():
		top = queue.get()
		cur_node = top[-1]
		for n in adj_map[cur_node]:
			if n == 'end':
				result += 1
				continue
			if n in top and n.islower():
				continue
			new_path = copy(top)
			new_path.append(n)
			queue.put(new_path)
	return result

def part_two(adj_map: Dict[str, str]) -> int:
	result = 0
	queue = Queue()
	queue.put((['start'], True))
	while not queue.empty():
		top, can_revisit = queue.get()
		cur_node = top[-1]
		for n in adj_map[cur_node]:
			path_can_revisit = can_revisit
			if n == 'end':
				result += 1
				continue
			if n == 'start':
				continue
			new_path = copy(top)
			new_path.append(n)
			if n.isupper():
				add_path = True
			else:
				if can_revisit:
					add_path = True					
					path_can_revisit = n not in top
				else:
					if n in top:
						add_path = False
					else:
						add_path = True

			if add_path:
				queue.put((new_path, path_can_revisit))
	return result 

if __name__ == '__main__':
	adj_map = read_input()
	result_one = part_one(adj_map)
	print(result_one)
	result_two = part_two(adj_map)
	print(result_two)
