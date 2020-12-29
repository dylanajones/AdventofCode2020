

def readData():
	f = open('data.txt')

	data = []

	for line in f:
		data.append(int(line))

	return data

def testNum(num, pre):

	for i, num1 in enumerate(pre):
		for j, num2 in enumerate(pre):
			if i != j:
				if num1 + num2 == num:
					return True

	return False

def findFirst(data, preamble_length):

	for i in range(len(data)):
		if not testNum(data[i+preamble_length], data[i:i+preamble_length]):
			return data[i+preamble_length]

	return None

def findSumList(data, num):
	cur_sum = data[0] + data[1]
	front = 0
	back = 1

	while cur_sum != num:
		if cur_sum < num:
			back += 1
			cur_sum += data[back]

		if cur_sum > num:
			cur_sum -= data[front]
			front += 1

	return data[front:back+1]


def findMinMaxSum(data, num):

	sum_list = findSumList(data, num)
	return min(sum_list) + max(sum_list)

def main():
	data = readData()
	preamble_length = 25
	num = findFirst(data, preamble_length)
	print(num)
	num = findMinMaxSum(data, num)
	print(num)

if __name__ == '__main__':
	main()