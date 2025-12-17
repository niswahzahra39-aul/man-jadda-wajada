import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("Data Visualization")


df = pd.read_csv("data/DaftarSaham.csv")  

st.write(df.head())
st.write(df.tail())

st.plotly_chart( grafik )