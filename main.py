import datasets
# X,Y = datasets.load_linear_example1()

X,Y = datasets.load_nonlinear_example1()

# ex_X = datasets.polynomial2_features(X)
ex_X = datasets.polynomial3_features(X)

print(ex_X)
print(Y)

import regression
# model = regression.LinearRegression()
# print(model.x)

import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
# print(model.theta)
# print(model.predict(X))
# print(model.score(X,Y))
