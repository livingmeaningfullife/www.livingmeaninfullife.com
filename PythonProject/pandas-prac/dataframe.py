import pandas as pd

data = {
    'name': ['Chhotan P', 'Shivam P', 'Ankit p'],
    'quality': ['purity', 'simplicity', 'humility']
}

datafr = pd.DataFrame(data, index = ['devotee1', 'devotee2', 'devotee3'])
print(datafr)
print(datafr.loc[['devotee1', 'devotee2']])