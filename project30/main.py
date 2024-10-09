import streamlit as st
import pandas as pd


st.title("Mars Atmospheric Conditions Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    column = st.selectbox("select a column to visualize", df.columns[1:])
    minval = df[column].min()
    maxval = df[column].max()
    min, max = st.slider("Select range to filter", minval, maxval, (minval, maxval))

    df_filtered = df[df[column].between(min, max)]

    st.line_chart(df_filtered.set_index("Date")[column])