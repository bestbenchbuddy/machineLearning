#http://iamtrask.github.io/2015/07/12/basic-python-network/
import numpy as np
 

# sigmoid function

def nonlin(x,deriv=False):
	if(deriv==True):
		return x*(1-x)
	return 1/(1+np.exp(-x))
 
# input dataset
X = np.array([ [6,9,7] ])
 
# output dataset           
y = np.array([[24]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
#np.random.seed(1)
 
# initialize weights 
weights = [3.2,4.5,5.1]

#syn0 = 10 * np.random.random_sample((1,4)) - 10

#syn0 = 2 * np.random.random((3,2)) -1 #mean of 0 

 
	for iter in xrange(10000):
 
	# forward propagation
	l0 = X
	l1 = nonlin(np.dot(l0,weights))
	 
	# how much did we miss?
	l1_error = y - l1
	 
	# multiply how much we missed by the
	# slope of the sigmoid at the values in l1
	l1_delta = l1_error * nonlin(l1,True)


	# update weights
	weights += np.dot(l0.T,l1_delta)
 
print "Output After Training:"
print l1
print "Output Weights After Training:"
print weights

# printing weights to see end result