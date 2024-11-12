import streamlit as st
import plotly.express as px
import pandas


df = pandas.read_csv("exer_day_38/storage.txt")
figure = px.line(x = df["date"], y=df["temperature"],
				 labels={"x": "date", "y": "temperature (C)"})

st.plotly_chart(figure)

st.line_chart(data = df)

