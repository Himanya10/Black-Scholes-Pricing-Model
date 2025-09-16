import streamlit as st
import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
import seaborn as sns
from numpy import log, sqrt, exp  

#######################
# Page configuration
st.set_page_config(
    page_title="Black-Scholes Option Pricing Model",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.metric-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 8px;
    width: auto;
    margin: 0 auto;
}
.metric-call {
    background-color: #90ee90;
    color: black;
    margin-right: 10px;
    border-radius: 10px;
}
.metric-put {
    background-color: #ffcccb;
    color: black;
    border-radius: 10px;
}
.metric-value {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0;
}
.metric-label {
    font-size: 1rem;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)

#######################
# Black-Scholes Class
class BlackScholes:
    def __init__(self, time_to_maturity, strike, current_price, volatility, interest_rate):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate

    def calculate_prices(self):
        d1 = (
            log(self.current_price / self.strike) +
            (self.interest_rate + 0.5 * self.volatility ** 2) * self.time_to_maturity
        ) / (self.volatility * sqrt(self.time_to_maturity))
        d2 = d1 - self.volatility * sqrt(self.time_to_maturity)

        call_price = self.current_price * norm.cdf(d1) - (
            self.strike * exp(-(self.interest_rate * self.time_to_maturity)) * norm.cdf(d2)
        )
        put_price = (
            self.strike * exp(-(self.interest_rate * self.time_to_maturity)) * norm.cdf(-d2)
        ) - self.current_price * norm.cdf(-d1)

        self.call_price = call_price
        self.put_price = put_price
        return call_price, put_price

#######################
# Sidebar Inputs
with st.sidebar:
    st.title("📊 Black-Scholes Model")
    st.write("`Created by:`")
    linkedin_url = "https://www.linkedin.com/in/Himanya-verma/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`Himanya Verma`</a>', unsafe_allow_html=True)

    current_price = st.number_input("Current Asset Price", value=100.0)
    strike = st.number_input("Strike Price", value=100.0)
    time_to_maturity = st.number_input("Time to Maturity (Years)", value=1.0)
    volatility = st.number_input("Volatility (σ)", value=0.2)
    interest_rate = st.number_input("Risk-Free Interest Rate", value=0.05)

    # ✅ Purchase price inputs
    purchase_call = st.number_input("Purchase Price of Call", value=5.0, step=0.5)
    purchase_put = st.number_input("Purchase Price of Put", value=5.0, step=0.5)

    st.markdown("---")
    spot_min = st.number_input('Min Spot Price', min_value=0.01, value=current_price*0.8, step=0.01)
    spot_max = st.number_input('Max Spot Price', min_value=0.01, value=current_price*1.2, step=0.01)
    vol_min = st.slider('Min Volatility for Heatmap', min_value=0.01, max_value=1.0, value=volatility*0.5, step=0.01)
    vol_max = st.slider('Max Volatility for Heatmap', min_value=0.01, max_value=1.0, value=volatility*1.5, step=0.01)

    spot_range = np.linspace(spot_min, spot_max, 10)
    vol_range = np.linspace(vol_min, vol_max, 10)

#######################
# Heatmap Function
def plot_heatmap(bs_model, spot_range, vol_range, strike, purchase_call, purchase_put):
    call_pnl = np.zeros((len(vol_range), len(spot_range)))
    put_pnl = np.zeros((len(vol_range), len(spot_range)))
    
    for i, vol in enumerate(vol_range):
        for j, spot in enumerate(spot_range):
            bs_temp = BlackScholes(bs_model.time_to_maturity, strike, spot, vol, bs_model.interest_rate)
            call_val, put_val = bs_temp.calculate_prices()
            call_pnl[i, j] = call_val - purchase_call
            put_pnl[i, j] = put_val - purchase_put
    
    fig_call, ax_call = plt.subplots(figsize=(10, 8))
    sns.heatmap(call_pnl, xticklabels=np.round(spot_range, 2), yticklabels=np.round(vol_range, 2),
                annot=True, fmt=".2f", cmap="RdYlGn", ax=ax_call, center=0, cbar_kws={'label': 'PNL'})
    ax_call.set_title('CALL PNL')
    ax_call.set_xlabel('Spot Price')
    ax_call.set_ylabel('Volatility')
    
    fig_put, ax_put = plt.subplots(figsize=(10, 8))
    sns.heatmap(put_pnl, xticklabels=np.round(spot_range, 2), yticklabels=np.round(vol_range, 2),
                annot=True, fmt=".2f", cmap="RdYlGn", ax=ax_put, center=0, cbar_kws={'label': 'PNL'})
    ax_put.set_title('PUT PNL')
    ax_put.set_xlabel('Spot Price')
    ax_put.set_ylabel('Volatility')
    
    return fig_call, fig_put

#######################
# Main Page
st.title("Black-Scholes Pricing Model with PNL")

# Show inputs table
input_df = pd.DataFrame({
    "Current Asset Price": [current_price],
    "Strike Price": [strike],
    "Time to Maturity (Years)": [time_to_maturity],
    "Volatility (σ)": [volatility],
    "Risk-Free Interest Rate": [interest_rate],
    "Call Purchase Price": [purchase_call],
    "Put Purchase Price": [purchase_put]
})
st.table(input_df)

# Calculate Call and Put
bs_model = BlackScholes(time_to_maturity, strike, current_price, volatility, interest_rate)
call_price, put_price = bs_model.calculate_prices()

# ✅ Compute PNL
call_pnl_val = call_price - purchase_call
put_pnl_val = put_price - purchase_put

# Display metrics
col1, col2 = st.columns([1,1], gap="small")
with col1:
    st.markdown(f"""
        <div class="metric-container metric-call">
            <div>
                <div class="metric-label">CALL PNL</div>
                <div class="metric-value">${call_pnl_val:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="metric-container metric-put">
            <div>
                <div class="metric-label">PUT PNL</div>
                <div class="metric-value">${put_pnl_val:.2f}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

#######################
# Heatmaps
st.markdown("")
st.title("Options PNL - Interactive Heatmap")
st.info("Explore how option PNL changes with varying 'Spot Prices' and 'Volatility' given your purchase price.")

col1, col2 = st.columns([1,1], gap="small")
with col1:
    st.subheader("Call PNL Heatmap")
    heatmap_fig_call, _ = plot_heatmap(bs_model, spot_range, vol_range, strike, purchase_call, purchase_put)
    st.pyplot(heatmap_fig_call)
with col2:
    st.subheader("Put PNL Heatmap")
    _, heatmap_fig_put = plot_heatmap(bs_model, spot_range, vol_range, strike, purchase_call, purchase_put)
    st.pyplot(heatmap_fig_put)
