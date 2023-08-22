import streamlit as st


def header(name: str, desc: str = None):
    """
    Generates a header for the page.

    Args:
        name (str): The name of the page, used as a header.
        desc (str, optional): A description of the page.
    """
    st.title("GoldForge")
    st.header(name)
    if desc:
        st.markdown(desc)
    st.divider()
