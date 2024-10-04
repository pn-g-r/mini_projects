import streamlit as st
import glob
 
data = {}
 
# Retrieve file paths from the 'files' directory
filepaths = sorted(glob.glob('project20/files/*.txt'))
 
# Process each file to extract letter and number
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    letter, number = content.split(":")
    data[letter] = float(number)
 
# Prepare data for the chart
chart_data = {
    'Letters': list(data.keys()),
    'Numbers': list(data.values())
}
 
# Streamlit app layout
st.title("Numbers from text files")
 
# Display the line chart
st.line_chart(chart_data, x='Letters')
 
# Display the list of letters and numbers
st.write('Letters and their corresponding numbers')
 
for letter, num in data.items():
    st.write(f'{letter}: {num}')