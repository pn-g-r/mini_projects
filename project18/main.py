import streamlit as st
from faker import Faker

fake = Faker()

def generate_name(number_of_names):
    names = [fake.name() for _ in range(number_of_names)]
    return names


st.title("Random name generator")
num_names = st.number_input("Enter the number of names to generate:", 
                            min_value=1, max_value=1000, value=5, step=1)


button = st.button("Generate Names")

if button:
    names = generate_name(num_names)
    st.subheader("Generated names")
    for name in names:
        st.write(name)
