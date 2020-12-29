
def readData():
	f = open('data.txt')

	data = []

	for line in f:
		line = line.strip('\n')

		s_line = line.split(' ')

		data.append(s_line)

	return data

def calcAcc(data):
	acc = 0
	index = 0
	visit = [False for x in range(len(data))]

	while (not all(visit)) and index != len(data):

		if not visit[index]:
			visit[index] = True

			if data[index][0] == 'nop':
				index += 1
			elif data[index][0] == 'acc':
				if data[index][1][0] == '+':
					acc += int(data[index][1][1:])
				elif data[index][1][0] == '-':
					acc -= int(data[index][1][1:])

				index += 1
			elif data[index][0] == 'jmp':
				if data[index][1][0] == '+':
					index += int(data[index][1][1:])
				elif data[index][1][0] == '-':
					index -= int(data[index][1][1:])
		else:
			return acc, index

	return acc, index

def calcAccCorrected(data):

	for i, instruction in enumerate(data):
		
		index = 0
		if instruction[0] == 'nop':
			data[i][0] = 'jmp'
			acc, index = calcAcc(data)
			data[i][0] = 'nop'

		elif instruction[0] == 'jmp':
			data[i][0] = 'nop'
			acc, index = calcAcc(data)
			data[i][0] = 'jmp'

		if index == len(data):
			return acc

def main():
	data = readData()
	acc, index = calcAcc(data)
	print(acc)
	acc = calcAccCorrected(data)
	print(acc)

if __name__ == '__main__':
	main()