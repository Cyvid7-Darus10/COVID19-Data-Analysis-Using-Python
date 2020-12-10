import pandas as pd 
import numpy as np  
import seaborn as sns
import matplotlib.pyplot as plt 
print('Modules are imported.')
corona_dataset_csv = pd.read_csv("./Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)
