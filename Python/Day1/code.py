# Code for the first day of Advent of code 2020

def part1():
	# Open data file
	f = open('data.txt')

	data = []

	# read in data and convert to int
	for line in f:
		data.append(int(line))

	# loop through the data - when looking dont need to look at tings we have already calculated
	for i, num1 in enumerate(data[:-1]):

		for j, num2 in enumerate(data[i+1:]):

			if (num1 + num2) == 2020:

				return num1 * num2

def part2():
	# Open data file
	f = open('data.txt')

	data = []

	# read in data and convert to int
	for line in f:
		data.append(int(line))

	# loop through the data - when looking dont need to look at tings we have already calculated
	for i, num1 in enumerate(data[:-2]):

		for j, num2 in enumerate(data[i+1:]):

			for k, num3 in enumerate(data[i+2:]):

				if (num1 + num2 + num3) == 2020:

					return num1 * num2 * num3

if __name__ == "__main__":
	result = part1()
	print(result)
	result = part2()
	print(result)