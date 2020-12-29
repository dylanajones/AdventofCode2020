
def readData():
	data = dict()

	f = open('data.txt')

	for line in f:
		line = line.strip('\n')
		line = line.split('bags contain')

		bag = line[0].strip(' ')
		holds = [x.strip(' .') for x in line[1].split(',')]

		for i, item in enumerate(holds):
			if item == 'no other bags':
				holds = None
			else:
				s = item.split(' ')
				holds[i] = ''
				for part in s[1:-1]:
					holds[i] = holds[i] + part + ' '

				holds[i] = (holds[i].rstrip(' '), int(s[0]))

		data[bag] = holds

	return data

def countHoldGold(data):
	count = 0

	for key in data:
		
		if key != 'shiny gold':
			count += checkHoldGold((key, 1), data)

	return count

def checkHoldGold(bag, data):

	open_list = [bag]

	while len(open_list) != 0:

		item = open_list.pop(0)[0]

		if item == 'shiny gold':
			return 1

		if data[item] is not None:
			open_list += data[item]

	return 0

def goldHoldCount(data):

	return numBagsHeld('shiny gold', data)

def numBagsHeld(bag, data):

	if data[bag] is None:
		return 0
	else:
		count = 0
		for bag_data in data[bag]:
			count += bag_data[1] + bag_data[1] * numBagsHeld(bag_data[0], data)
		return count

def main():
	data = readData()
	count = countHoldGold(data)
	print(count)
	count = goldHoldCount(data)
	print(count)

if __name__ == '__main__':
	main()