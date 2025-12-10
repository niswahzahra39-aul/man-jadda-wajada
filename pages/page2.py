import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt

st.title("Data Visualization")

df = pd.read_csv("data/DaftarSaham.csv")