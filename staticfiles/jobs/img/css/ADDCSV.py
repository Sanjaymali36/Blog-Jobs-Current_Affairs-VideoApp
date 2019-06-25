import pandas as pd
import glob

path =r'C:/Users/dell/Downloads/Basic Science & Engineering Drawing (CSV)/Basic Science & Engineering Drawing (CSV)/enviroment study'
allFiles = glob.glob(path + "/*.csv")

list_ = []

for file in allFiles:
    df = pd.read_csv(file,index_col=None, header=0)
    list_.append(df)

frame = pd.concat(list_, axis = 0, sort=False,ignore_index = True)
print(frame)
csv =frame.to_csv(r'C:/Users/dell/Downloads/files/combination3.csv')