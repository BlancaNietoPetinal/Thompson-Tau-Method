import numpy as np
import scipy.stats as ss


def maxim(data):
	m = 0
	ind = 0
	for i in range(len(data)):
		if not(np.isnan(data[i])) and data[i]>m:
			m = data[i]
			ind = i
	return m,ind

def thompson_tau(data,alpha = 0.05,threshold):
	# Information obtained from: https://www.statisticshowto.datasciencecentral.com/modified-thompson-tau-test/
	'''
	Implements the Thompson Tau method and returns a list with the outliers index.
	Inputs:
		- data: an array.
		- alpha: the significance level, default 0.05.
		- Threshold: the number of points tested.
	Outputs:
	 	- outliers: a list with the indices of the outliers.
	'''
	outliers = []
	n = len(data)
	mean = np.mean(data)
	delta = abs(data-mean)
	std = np.std(data)
	for i in range(threshold):
		d,ind = maxim(delta)
		reject = ss.t.ppf(alpha/2, n - 2)
		tau = (reject*(n - 1))/(np.sqrt(n)*np.sqrt(n - 2 + np.power(reject,2)))
		if d > tau*std:
			outliers += [ind]
		delta[ind] = None
	return outliers

# An example to test it
data = np.array([489, 490, 490, 491, 494, 499, 499, 500, 501, 505])
print(thompson_tau(data,0.05,10))
