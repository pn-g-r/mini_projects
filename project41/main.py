import requests

url = 'https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/'

def construct_filepath(year):
    filepath = f"{year}.csv.gz"
    return filepath

def construct_url(url, filepath):
    file_url = f"{url}{filepath}"
    return file_url

def download_file(fileurl, filepath, dir='project41/'):
    response = requests.get(fileurl)
    with open(dir + filepath, 'wb') as file:
        file.write(response.content)





for year in range(1800, 1805):
    filepath = construct_filepath(year)
    fileurl = construct_url(url, filepath)
    download_file(fileurl, filepath)