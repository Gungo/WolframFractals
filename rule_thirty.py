#!/usr/bin/env python3
import matplotlib as plt
import numpy as np
import random

# print array
def p(array):
	print(*array, sep="")

# print 2d
def p2d(array2d):
	str = "_"*len(array2d[0])
	print(str+"\n")
	for array in array2d:
		p(array)
	print(str+"\n\n")

def make_random_array(num):
	fin = []
	for i in range(num):
		curr = random.randint(0, 1)
		fin.append(curr)
	p(fin)
	return fin

# we know this array will be three long
def determine_case(a,b,c):
	if(b == 0):
		if(c==0):
			# x00
			return 1 if (a == 0) else 5
		else:
			# x01
			return 2 if (a == 0) else 6
	elif(c==0):
		# x10
		return 3 if (a == 0) else 7
	else:
		# x11
		return 4 if (a == 0) else 8
'''
	000: -> 1 (case1)
	001: -> 1 (case2)
	010: -> 1 (case3)
	011: -> 1 (case4)

	100: -> 0 (case5)
	101: -> 0 (case6)
	110: -> 0 (case7)
	111: -> 0 (case8)
'''
def transformation(case):
	if(case == 1 or (case <=8 and case >=6)):
		return 0
	return 1

def transform(original):
	fin = []
	size = len(original)
	for i in range(size):
		# fixes spacing and out of bounds
		a = original[i-1] if (i >= 1) else 0
		b = original[i]
		c = original[i+1] if (i < size-1) else 0

		case = determine_case(a, b, c)
		t = transformation(case)

		fin.append(t)

	return fin

def main():
	size = int(input("Enter size..."))
	original = [0]*size
	original[int(size/2)] = 1
	fin = []
	for i in range(size):
		fin.append(original)
		temp = transform(original)
		original = temp

	# p2d(fin)
	# matplotlib stuff
	N = size
	Z = np.array(fin)
	G = np.zeros((N,N,3))

	# Where we set the RGB for each pixel
	G[Z>0.5] = [1,1,1]
	G[Z<0.5] = [0,0,0]

	plt.imshow(G,interpolation='nearest')
	plt.show()

main()
