import requests
import streamlit as st
 
def get_historical_events(month, day):
    url = f"http://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    events = data['data']['Events']
    return events
 
st.title('Historical Events Viewer')
st.write('Enter a date to retrieve historical events.')
 
# Input fields for month and day
month = st.number_input('Enter the month (e.g., 7 for July):', min_value=1, max_value=12, step=1)
day = st.number_input('Enter the day (e.g., 1 for 1st):', min_value=1, max_value=31, step=1)
 
# Button to trigger event retrieval
if st.button('Show Events'):
    events = get_historical_events(month, day)
    if events:
        st.subheader(f"Historical Events on {month}/{day}:")
        for event in events:
            st.write(f"Year: {event['year']}")
            st.write(f"Description: {event['text']}")
            if event['links']:
                st.write(f"Link: {event['links'][0]['link']}")
            st.divider()