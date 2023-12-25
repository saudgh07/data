import streamlit as st
import pandas as pd

st.title("Excel Update App")
save_data = st.button("Save File")
df = pd.read_csv("names.csv")
st.header("Random Data")
st.write(df)

st.sidebar.header("Options")
options_form = st.sidebar.form("options_form")
user_name = options_form.text_input("Name")
user_age = options_form.text_input("Age")
add_data = options_form.form_submit_button()
if add_data:
    new_data = {"name": user_name, "age": int(user_age)}
    new_row = pd.DataFrame([new_data])
    df = df.append(new_row, ignore_index=True)
    df.to_csv("names.csv", index=False)
