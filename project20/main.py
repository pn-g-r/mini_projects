import polars as pl

df = pl.read_csv(r'project20\cars.csv')

cly_4_df = df.filter(pl.col('cylinders')==4)
print(cly_4_df)

mean_horsepower = df.group_by('cylinders').agg(pl.col('horsepower').mean())
print(mean_horsepower)