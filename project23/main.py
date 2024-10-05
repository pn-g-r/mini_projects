import pandas
import requests

def get_data(startdate, enddate):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        'format': 'geojson',
        'starttime': startdate,
        'endtime': enddate
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def extract_data(raw_data):
    clean_data = []
    features = raw_data['features']
    for feature in features:
        earthquake = {'Magnitude': feature['properties']['mag'],
                      'Location': feature['properties']['place'],
                      'Latitude': feature['geometry']['coordinates'][1],
                      'Longitude': feature['geometry']['coordinates'][0]}
        clean_data.append(earthquake)
    return clean_data
        
def save_to_excel(data, path):
    df = pandas.DataFrame(data)
    df.to_excel(path, index=False)


raw_data = get_data("2024-10-03", "2024-10-04")
clean_data = extract_data(raw_data)
save_to_excel(clean_data, 'project23/earthquakesoct.xlsx')