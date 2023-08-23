from typing import Tuple
import streamlit as st
import requests
import bs4


def london_fix() -> Tuple[float, float]:
    """
    Scrapes the London Fix price of gold.

    Returns:
        am_price (float): The AM price of gold.
        pm_price (float): The PM price of gold.
    """

    url = "https://www.kitco.com/gold.londonfix.html"
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    price_sheet = soup.find("tr", {"class": "even"})

    am_price = float(price_sheet.find("td", {"class": "am"}).text)
    pm_price = float(price_sheet.find("td", {"class": "pm"}).text)

    date = soup.find("td", {"class": "dates"}).text.upper()
    date = date.replace("QUOTES AS OF", "").strip().capitalize()

    return am_price, pm_price, date


st.title("GoldForge")
st.subheader(
    "Welcome to GoldForge, a web app that powers the precision jewelry manufacturing."
)

with st.sidebar:
    st.caption("© 2023 Sahil Pattni. All rights reserved.")
    st.caption(f"Streamlit version: {st.__version__}")
    with open("requirements.txt") as f:
        st.caption(f"Requirements: {f.read()}")

st.divider()


am_price, pm_price, date = london_fix()

st.header("London Fix")
st.caption(f"Last updated: {date}")
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Gold Price (AM)",
        f"${am_price:,.2f}",
    )
    st.metric(
        "Gold Price (AM)",
        f"{am_price * 3.67:,.2f} AED",
    )
with col2:
    st.metric(
        "Gold Price (PM)",
        f"${pm_price:,.2f}",
    )
    st.metric(
        "Gold Price (PM)",
        f"{pm_price * 3.67:,.2f} AED",
    )
