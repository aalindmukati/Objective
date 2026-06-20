import seaborn as sns
import pandas as pd 
import numpy as np 

x = sns.get_dataset_names()

penguin = sns.load_dataset('penguins')
z = penguin['island'].value_counts()

print(z)