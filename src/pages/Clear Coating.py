import streamlit as st
from utils import header

header(
    name="Clear Coating Solution Preparation",
)
with st.sidebar:
    st.caption("© 2023 Sahil Pattni. All rights reserved.")

with open("resources/clear_coating.md", "r") as f:
    st.markdown(f.read())

st.caption("© 2023 Sahil Pattni. All rights reserved.")
