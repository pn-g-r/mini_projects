import pandas as pd
import plotly.express as px

data = pd.read_csv('project25/houses.csv')

print(data)

fig = px.scatter(data, x='Size', y='Price', color='Location', title='House Price vs House size', hover_data={'Bedrooms': True, 'Bathrooms': True,'Age': True, 'Size': False, 'Price': False})

fig.show()