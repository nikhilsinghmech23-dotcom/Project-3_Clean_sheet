import pandas as pd
df=pd.read_csv("Details.csv")

df.isnull()
FilledDf=df.fillna("1525")
FilledDf.isnull().sum()
FilledDf.dropna()
analyzeDf=FilledDf.drop_duplicates()
print(analyzeDf.index)

FilledDf=pd.DataFrame(analyzeDf.dropna())
FilledDf.to_csv("Analyzed_Details.csv")