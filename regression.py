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
		return np.dot(x,self.theta)
		"""testing(cont.)
		importlib,reload(regression)
		model = regression.LinearRegression()
		model.fit(X,Y)
		model.predict(X)
		expect
		array([7.2,9.2,11.7,13.7])
		"""
	def score(self,x,y):
		
		pass
	