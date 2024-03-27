import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r'''a+ar^1+ar^2+ar^3''')

st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pic your gender', ['Male, Female'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellect'])
st.slider('Pick a number', 0, 50)