# Code for day 2 of Advent of code 2020

# Reads in the data a returns a list of tuples where tuple is
# ([low, high], letter, password)
def readData():
	data = []

	f = open('data.txt')

	for line in f:
		line = line.strip('\n')
		s_line = line.split(' ')
		bounds = s_line[0].split('-')
		p_data = ([int(bounds[0]), int(bounds[1])], s_line[1][0], s_line[2])
		data.append(p_data)

	return data

def countGood(data):
	good = 0
	for d in data:
		count = 0
		
		for c in d[2]:
			
			if c == d[1]:
				count += 1

		if d[0][0] <= count <= d[0][1]:
			good += 1

	return good

def countGood2(data):
	good = 0

	for d in data:
		if (d[2][d[0][0]-1] == d[1] and d[2][d[0][1]-1] != d[1]) or (d[2][d[0][0]-1] != d[1] and d[2][d[0][1]-1] == d[1]):
			good += 1

	return good

def main():
	data = readData()
	num_good = countGood(data)
	print(num_good)
	num_good = countGood2(data)
	print(num_good)

if __name__ == "__main__":
	main()
