from random import choice 
from numpy import array, dot, random 
import numpy as np
import time
# from pylab import plot, ylim

def nonlin(x,deriv = False):
		if (deriv==True):
			return x*(1-x)
		return 1/(1+np.exp(-x))

unit_step = lambda x: 0 if x < 0 else 1

training_data = [ 
	(array([5,6,9]), 24), 
] 

w = [random.uniform(0, 5), random.uniform(0, 5), random.uniform(0, 5)]
# print w

errors = [] 
eta = 0.2 
n = 10
x, expected = choice(training_data) 

for i in xrange(n): 
	#print x, expected
	#time.sleep(1)
	result = dot(w, x)
	error = (expected - unit_step(result))
	print unit_step(result)
	errors.append(error)
	w += eta * error * x
	w = w2-wT
	w2 = w
	print w
# print x

for x, _ in training_data: 
	# print '%s\n\n' % w
	result = dot(x, w) 
	print("{}, {} -> {}".format(x[:3], result, w))

# Target = 24
# input -> x
# error function -> E = 1/2(T-O)^2
# 