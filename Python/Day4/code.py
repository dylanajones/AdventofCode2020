# Code for Day 4 of Advent of Code 2020

class Passport:
	def __init__(self, data):
		
		self.byr = None
		self.iyr = None
		self.eyr = None
		self.hgt = None
		self.hcl = None
		self.ecl = None
		self.pid = None
		self.cid = None

		self.valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

		for item in data:
			d = item.split(':')

			if d[0] == 'byr':
				self.byr = d[1]
			elif d[0] == 'iyr':
				self.iyr = d[1]
			elif d[0] == 'eyr':
				self.eyr = d[1]
			elif d[0] == 'hgt':
				self.hgt = d[1]
			elif d[0] == 'hcl':
				self.hcl = d[1]
			elif d[0] == 'ecl':
				self.ecl = d[1]
			elif d[0] == 'pid':
				self.pid = d[1]
			elif d[0] == 'cid':
				self.cid = d[1]

	def isValid(self):
		if self.validBYR() and self.validIYR() and self.validEYR() and self.validHGT() and self.validHCL()  and self.validECL() and self.validPID():
			return True
		else:
			return False

	def validBYR(self):
		if self.byr is None:
			return False

		if len(self.byr) != 4:
			return False

		if 1920 <= int(self.byr) <= 2002:
			return True

		return False

	def validIYR(self):
		if self.iyr is None:
			return False

		if len(self.iyr) != 4:
			return False

		if 2010 <= int(self.iyr) <= 2020:
			return True

		return False

	def validEYR(self):
		if self.eyr is None:
			return False

		if len(self.eyr) != 4:
			return False

		if 2020 <= int(self.eyr) <= 2030:
			return True

		return False

	def validHGT(self):
		if self.hgt is None:
			return False

		num = int(self.hgt[:-2])
		unit = self.hgt[-2:]

		if unit == 'cm':
			if 150 <= num <= 193:
				return True

		if unit == 'in':
			if 59 <= num <= 76:
				return True

		return False

	def invalidChar(self, char):
		if ('a' <= char <= 'f') or ('0' <= char <= '9'):
			return False
		else:
			return True

	def validHCL(self):
		if self.hcl is None:
			return False

		if len(self.hcl) != 7 or self.hcl[0] != '#':
			return False

		for char in self.hcl[1:]:
			if self.invalidChar(char):
				return False

		return True

	def validECL(self):
		if self.ecl is None:
			return False

		if self.ecl in self.valid_eye_color:
			return True
		else:
			return False

	def validPID(self):
		if self.pid is None:
			return False

		if len(self.pid) == 9:
			for char in self.pid:
				if not ('0' <= char <= '9'):
					return False
			return True
		else:
			return False

def readData():
	f = open('data.txt')

	data = []
	s_data = []
	for line in f:
		if line != "\n":
			line = line.strip('\n')
			s_line = line.split()

			s_data = s_data + s_line
		else:
			data.append(Passport(s_data))
			s_data = []

	data.append(Passport(s_data))

	return data

def countValidPassports(data):

	count = 0

	for passport in data:
		if passport.isValid():
			count += 1

	return count

def main():
	data = readData()
	valid_passports = countValidPassports(data)
	print(valid_passports)

if __name__ == "__main__":
	main()