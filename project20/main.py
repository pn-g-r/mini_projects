import streamlit as st
import glob


data = {}

filepaths = sorted(glob.glob("files/*.txt"))

for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    letter, number = content.split(":")
    data[letter] = float(number)

chart_data = {
    'Letters': list(data.keys()),
    'Numbers': list(data.values())
}
st.title("Numbers from text files")
st.line_chart(chart_data, x='Letters')