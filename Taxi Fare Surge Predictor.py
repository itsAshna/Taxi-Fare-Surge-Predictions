# ##Imports
# %matplotlib inline
# %load_ext autoreload
# %autoreload 2
# %config InlineBackend.figure_format = 'retina'

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

data_path = '/Users/ashnaarora/Downloads/final.csv'
rides= pd.read_csv(data_path)
rides.head()
rides
##Make Dataset
len(rides)
rides.shape
# rides.drop(['XYZ','X1','X2','X3','X4'])

X = rides.values[:, 0:3]
X = X.astype(np.int64)
X
Y = rides.values[:,3]
Y = Y.astype(np.int64)
Y
##Model

#%%
from sklearn.tree import DecisionTreeRegressor  
  
# create a regressor object 
regressor = DecisionTreeRegressor(random_state = 0)  


#%%
  
# fit the regressor with X and Y data 
regressor.fit(X, Y) 
k = np.array([[0,0,0]]).astype(int)
y_pred = regressor.predict(k) 
  
# print the predicted price 
print("Predicted price: % d\n"% y_pred)  
regressor.score(X,Y)

#%%

output = []

f = open( '/Users/ashnaarora/Downloads/final.csv', 'r' ) #open the file in read universal mode
for line in f:
    cells = line.split( "," )
    if (cells[2]=='0\n'):
      cells[2] = '0'
    elif (cells[2]=='1\n'):
      cells[2] = '1'
    elif (cells[2]=='2\n'):
      cells[2]= '2'
    elif (cells[2]=='3\n'):
      cells[2] = '3'
    elif (cells[2]=='4\n'):
      cells[2]= '4'
    elif (cells[2]=='5\n'):
      cells[2] = '5'
  
    output.append( ( cells[ 0 ], cells[ 1], cells[2])) #since we want the first, second and third column
    
#%%

f.close()

output
# output.remove(('from_month','from_day','from_time\n'))

      
      