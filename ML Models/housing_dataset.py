from sklearn.datasets import fetch_california_housing

# Load the California housing dataset
housing = fetch_california_housing()

# Print the description of the dataset
print(housing.DESCR)

# Access the data and target (features and target variable)
X = housing.data
y = housing.target

# Convert to pandas DataFrame (optional)
import pandas as pd
df = pd.DataFrame(data=X, columns=housing.feature_names)
df['MedHouseVal'] = y  # Add the target variable to the DataFrame

# Display the first few rows of the DataFrame
print(df.head())

# Plot histograms of the features (optional)
import matplotlib.pyplot as plt
df.hist(bins=50, figsize=(20,15))
plt.show()
