import streamlit as st
import requests

# API key and URL for exchange rates
api_key = "cf561c7c59b82bfb911bc763"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

# Function to convert between USD and EUR
def convert(currency_from, currency_to, currency_value):
    response = requests.get(url)
    data = response.json()

    if currency_from == "USD" and currency_to == "EUR":
        conversion_rate = data['conversion_rates']["EUR"]
    elif currency_from == "EUR" and currency_to == "USD":
        # Fetch conversion rate from EUR to USD by inverting USD to EUR rate
        conversion_rate = 1 / data['conversion_rates']["EUR"]
    
    result = currency_value * conversion_rate
    return result

# Streamlit app interface
st.title("Currency Converter: USD ⮀ EUR")

conversion = st.radio("Choose the conversion:", ("USD to EUR", "EUR to USD"))

input_value = st.number_input("Enter the amount:")

button = st.button("Convert")

# Conversion logic
if button:
    if conversion == "USD to EUR":
        euros = convert("USD", "EUR", input_value)
        st.success(f"{input_value} USD is {euros:.2f} EUR")
    elif conversion == "EUR to USD":
        dollars = convert("EUR", "USD", input_value)
        st.success(f"{input_value} EUR {dollars:.2f} USD")

