from random import choice 
from numpy import array, dot, random 
import time
# from pylab import plot, ylim

unit_step = lambda x: 0 if x < 0 else 1 

training_data = [ 
	(array([0,0,1]), 1), 
	(array([0,1,1]), 0), 
	(array([1,0,1]), 0), 
	(array([1,1,1]), 0), 
] 

random.uniform(1.5, 1.9)
w = random.rand(3) 

errors = [] 
eta = 0.2 
n = 4

for i in xrange(n): 
	x, expected = choice(training_data) 
	#print x, expected
	time.sleep(1)
	result = dot(w, x) 
	error = expected - unit_step(result) 
	errors.append(error) 
	w += eta * error * x 

print x

for x, _ in training_data: 
	#print '%s\n\n' % w
	result = dot(x, w) 
	print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

# ylim([-1,1]) 
# plot(errors)