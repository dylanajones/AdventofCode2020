# Code for day 5 of Advent of Code 2020

import math

def loadData():
	f = open('data.txt')

	data = []

	for line in f:
		line = line.strip('\n')
		data.append(line)

	return data

def calSeats(data):
	seats = []

	for loc in data:
		front = 0
		back = 127

		for char in loc[:6]:
			if char == 'F':
				back -= math.ceil((back - front) / 2)
			elif char == 'B':
				front += math.ceil((back - front) / 2)

		if loc[6] == 'F':
			row = front
		elif loc[6] == 'B':
			row = back

		front = 0
		back = 7

		for char in loc[-3:-1]:
			if char == 'L':
				back -= math.ceil((back - front) / 2)
			elif char == 'R':
				front += math.ceil((back - front) / 2)

		if loc[-1] == 'R':
			col = back
		elif loc[-1] == 'L':
			col = front

		seats.append((row, col, row * 8 + col))

	return seats

def findMySeat(seats):

	seat_ids = [x[2] for x in seats]

	for seat_id in range(min(seat_ids), max(seat_ids)):

		if seat_id not in seat_ids:
			if seat_id - 1 in seat_ids and seat_id + 1 in seat_ids:
				return seat_id

def main():
	data = loadData()
	seats = calSeats(data)
	seats.sort(key=lambda s: s[2])
	my_seat = findMySeat(seats)
	print(my_seat)

if __name__ == '__main__':
	main()