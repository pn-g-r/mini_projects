import pandas

df = pandas.read_excel("project4/europe.xlsx")

print(df)

df.to_json("project4/europe.json", orient='records')