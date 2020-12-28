# Code for day 3 of Advent of Code 2020

def readMap():
	tree_map = []

	f = open('data.txt')

	for line in f:
		line = line.strip('\n')
		tree_map.append(line)

	return tree_map 

def calCollisions(tree_map, move):
	x_pos = 0
	y_pos = 0
	width = len(tree_map[0])
	height = len(tree_map)
	collisions = 0

	while(y_pos + move[1] < height):
		x_pos = (x_pos + move[0]) % width
		y_pos = y_pos + move[1]

		if tree_map[y_pos][x_pos] == '#':
			collisions += 1

	return collisions

def main():
	moves = [(1,1),(3,1),(5,1),(7,1),(1,2)]
	tree_map = readMap()
	collisions_mult = 1
	for move in moves:
		collisions = calCollisions(tree_map, move)
		collisions_mult = collisions_mult * collisions

	print(collisions_mult)

if __name__ == '__main__':
	main()