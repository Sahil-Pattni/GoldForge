import streamlit as st

from utils import header

# --- FUNCTIONS --- #


def calculate_alloy_weight(weights: list, purities: list, desired_purity: int) -> float:
    """
    Calculates the weight of the alloy needed to be added to the raw gold to achieve the desired purity.

    Args:
        weights (list): The weights of the alloys in grams.
        purities (list): The purities of the raw gold in perthousands.
        desired_purity (float): The desired purity of the alloy in perthousands.

    Returns:
        pure_gold (float): The amount of pure gold in the alloy.
        alloy_weight (float): The weight of the alloy needed to be added to the raw gold to achieve the desired purity.
        new_weight (float): The new weight of the gold after adding the alloy.
    """
    pure_gold = sum(
        [weight * (purity / 1000) for weight, purity in zip(weights, purities)]
    )
    purity = pure_gold / sum(weights)

    if purity < (desired_purity / 1000):
        raise ValueError(
            f"The desired purity {desired_purity/1000:,.3f} cannot be greater than the raw purity {purity:,.3f}"
        )

    new_weight = pure_gold / (desired_purity / 1000)
    alloy_weight = new_weight - sum(weights)

    return pure_gold, alloy_weight, new_weight


def gen_purity_input(key=1):
    return st.number_input(
        "Raw Purity [0 - 1000]",
        min_value=0,
        max_value=1000,
        value=995,
        step=1,
        key=key,
        help="The purity of the raw gold in perthousands. Defaults to 995",
    )


def gen_weight_input(key=1):
    return st.number_input(
        "Weight",
        min_value=0.0,
        value=0.0,
        key=key,
        help="The weight of the alloy in grams.",
    )


def generate_input_rows(n=4):
    global weights, purities
    for i in range(1, n * 2, 2):
        col1, col2 = st.columns(2)
        with col1:
            weights.append(gen_weight_input(i))
        with col2:
            purities.append(gen_purity_input(i + 1))


# ----------------- #
header(
    name="Alloys",
    desc="Welcome to the Alloys page. Here you can calculate the weight of the alloy needed to be added to the raw gold to achieve the desired purity.",
)
with st.sidebar:
    st.caption("© 2023 Sahil Pattni. All rights reserved.")

desired_purity: float = st.number_input(
    label="Desired Purity [0 - 1000]",
    min_value=0,
    max_value=1000,
    value=926,
    step=1,
    help="The purity of the alloy in perthousands.",
)

# Generate input rows
st.subheader("Input Gold")
weights = []
purities = []
generate_input_rows(n=3)


if desired_purity:
    try:
        raw_purity, alloy_weight, new_weight = calculate_alloy_weight(
            weights, purities, desired_purity
        )

        # st.subheader("Results")
        st.divider()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Raw Gold (Gross)", f"{sum(weights):.3f} g")
            st.metric("Pure Gold", f"{raw_purity:.3f} g")
        with col2:
            st.metric("Alloy to Add", f"{alloy_weight:.3f} g")
            st.metric("New Weight (Gross)", f"{new_weight:.3f} g")
        with col3:
            st.metric("Input Purity", f"{raw_purity / sum(weights):.3f}")

    except ZeroDivisionError:
        st.stop()
    except Exception as err:
        st.error(f"Error: {err}")
        st.stop()
