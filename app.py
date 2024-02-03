import streamlit as st
import pandas as pd
import time

# Create an empty dataframe to store call notes
call_notes_df = pd.DataFrame(columns=["Caller Name", "Phone Number", "Note"])

# Streamlit app header
st.title("Phone Call Summary and Reminder")

# Input form for adding call notes
caller_name = st.text_input("Caller Name:")
phone_number = st.text_input("Phone Number:")
note = st.text_area("Call Note:")

# Button to add the note to the dataframe
if st.button("Add Call Note"):
    call_notes_df = call_notes_df.append({"Caller Name": caller_name, "Phone Number": phone_number, "Note": note},
                                         ignore_index=True)
    st.success("Call note added successfully!")

# Display the list of call notes
st.header("List of Call Notes")
st.table(call_notes_df)

# Simulate a reminder when a call comes in
incoming_call_number = st.text_input("Enter Incoming Call Number:")

if st.button("Check Call"):
    if incoming_call_number in call_notes_df["Phone Number"].values:
        matching_note = call_notes_df.loc[call_notes_df["Phone Number"] == incoming_call_number, "Note"].values[0]
        st.warning(f"Reminder: Call from {incoming_call_number}. Note: {matching_note}")
    else:
        st.info("No matching call note found for this number.")

# This part of the code simulates a call event and should be triggered externally based on your phone system.
# For a real-world implementation, you'd need integration with your phone system.

# To run this Streamlit app, use: streamlit run your_app_file.py
