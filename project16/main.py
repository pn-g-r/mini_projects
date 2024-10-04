import pandas

def convert_excel_to_json(excel_file):
    df = pandas.read_excel(excel_file)
    json_data = df.to_json(orient='records')
    return json_data