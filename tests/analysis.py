# add basic preprocessing code for data stored in directory data
# add basic code for data analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('data/data.csv')

# Check for missing values
data.isnull().sum()

# Check for duplicates
data.duplicated().sum()

# Check for data types
data.dtypes

# Check for unique values
data.nunique()

# Check for outliers
data.describe()
