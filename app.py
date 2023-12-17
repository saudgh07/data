import streamlit as st
import pandas as pd

st.title("Excel Update App")
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # Add 'hour' column to dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()
st.header ("Existing File")
st.write(df)
st. sidebar.header ("Options")

options_form = st. sidebar. form("options_form")
user_name = options_form.text_input ("Name")
user_age = options_form. text_input ("Age")
add_data = options_form.form_submit_button()
if add_data:
  new_data = {"name": user_name,"age": int(user_age)}
  df = df.append(new_data, ignore_index=True)
  df.to_csv("data/names.csv", index-False)
