import streamlit as st


st.title("Clear Coating Solution Preparation")
st.divider()
with open("resources/clear_coating.md", "r") as f:
    st.markdown(f.read())

st.caption("© 2023 Sahil Pattni. All rights reserved.")
