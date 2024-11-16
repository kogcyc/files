import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data from your CSV file
data = pd.read_csv('chainTrain.csv', header=None, names=['x', 'y', 'z', 't'])

# Separate features and target
X = data[['x', 'y', 'z']]
y = data['t']

# Train the regression model
model = LinearRegression()
model.fit(X, y)
print("model trained successfully!")
print("here are the coefficients and the intercept")
print(model.coef_.tolist())
print(model.intercept_)