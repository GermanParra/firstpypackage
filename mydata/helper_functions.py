import pandas as pd
import numpy as np

#df = pd.DataFrame({'a':[1,2,np.nan,8,np.nan,5],'b':[4,np.nan,6,np.nan,6,5]})

def count_nulls(df):
    'return total count of null values in a data frame'
    total = df.isnull().sum().sum()
    return total

def tt_split(df,frac):
    '''split data into train and test
       it takes a df and the test set size'''
    if type(df) == pd.core.frame.DataFrame: 
      if (frac < 1) & (frac != 0):
        test = df[:(round(len(df)*frac))]
        train = df[(round(len(df)*frac)):]
        return (pd.DataFrame(train), pd.DataFrame(test))
      else:
        raise NameError('Second Argument needs a value > 0 and < 1')
    else:
      raise NameError('First Argument is not a DataFrame Type')

#print(count_nulls(df))



