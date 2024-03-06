import pandas as pd

# replace below path wit your file path
path = r"D:\Projects\Files\clientemaillist.csv"

def readCsv(_path):
    df = pd.read_csv(_path,delimiter=",")
    return df
    
df = readCsv(path)

## Read top 5 rows | .head()
print("####### .head() #########")
print(df.head())

## read last 5 rows | .tail()
print("####### .tail() #########")
print(df.tail())

## list all columns | .columns
print(df.columns)

## get summary of dataframe | .info()
print("####### .info() #########")
print(df.info())

## Get descriptive stats, summary | .describe()
print("####### describe()###########")
print(df.describe())

## export to a csv file
print("####### .to_csv()#########")
df.to_csv('df-to-csv.csv')

print("####### .to_csv() tab delimitted #########")
df.to_csv('df-to-tab-csv.csv', sep="\t")


print("####### .to_csv() tab delimitted, index #########")
df.to_csv('df-to-tab-index-csv.csv', sep="\t", index=False)

print("####### .to_csv() tab delimitted, without header #########")
df.to_csv('df-to-tab-nohead-csv.csv', sep="\t", header=False)



