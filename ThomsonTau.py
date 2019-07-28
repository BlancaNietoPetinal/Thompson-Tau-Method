import numpy as np
import scipy.stats as ss


def maxim(data):
	m = 0
	ind = 0
	for i in range(len(data)):
		if not(np.isnan(data[i])) and data[i]>m:
			m = data[i]
			ind = i
			print('new max in:',i,'which is:',m)
	return m,ind

def thompson_tau(data,alpha,threshold):
	# https://www.statisticshowto.datasciencecentral.com/modified-thompson-tau-test/
	# return a list with the outliers index
	outliers = []
	n = len(data)
	mean = np.mean(data)
	delta = abs(data-mean)
	std = np.std(data)
	for i in range(threshold):
		print(delta)
		d,ind = maxim(delta)
		print(d, ind)
		reject = ss.t.ppf(alpha/2, n - 2)
		tau = (reject*(n - 1))/(np.sqrt(n)*np.sqrt(n - 2 + np.power(reject,2)))
		if d > tau*std:
			outliers += [ind]
		delta[ind] = None
	return outliers

data = np.array([489, 490, 490, 491, 494, 499, 499, 500, 501, 505])
print(thompson_tau(data,0.05,10))