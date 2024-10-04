import pandas

df = pandas.read_excel("project4/europe.xlsx")

df.to_json("project4/europe.json", orient='records')