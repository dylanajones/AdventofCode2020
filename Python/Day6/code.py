# Code for Advent of Code 2020 Day 6

def readData():
	f = open('data.txt')

	data = []
	s_data = []
	
	for line in f:
		if line != "\n":
			line = line.strip('\n')
			s_line = [char for char in line]

			s_data.append(set((s_line)))
		else:
			s_data = set.intersection(*s_data)
			data.append(s_data)
			s_data = []

	s_data = set.intersection(*s_data)
	data.append(s_data)

	return data

def countSum(data):

	count = 0

	for group in data:
		count += len(group)

	return count

def main():
	data = readData()
	sum_count = countSum(data)
	print(sum_count)
	return 0

if __name__ == '__main__':
	main()