import pandas

df = pandas.read_excel("project4/europe.xlsx")

df.to_json("project4/europe.json", orient='records')

df.to_csv('project4/europe.csv', index=False)

with open('project4/europe.csv') as file:
    print(next(file), end='')
    print(next(file))