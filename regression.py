import numpy as np
class LinearRegression:
	x = None
	theta = None
	y = None
	
	def fit(self,x,y):
		temp = np.linalg.inv(np.dot(x.T,x))
		self.theta = np. dot(np.dot(temp,x.T),y)
		"""testing(cont.)
		import importlib
		importlib,reload(regression)
		model = regression.LinearRegression()
		model.fit(X,Y)
		model.theta
		expect
		array([5.30412371,0.49484536])
		"""
	def predict(self,x):
		pass
	def score(self,x,y):
		pass
	