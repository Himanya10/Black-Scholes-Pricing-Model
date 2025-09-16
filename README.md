# 📊 Black-Scholes Option Pricing & PNL Heatmaps

https://black-scholes-pricing-model-ggowf4pffudqv5ykqqvzqm.streamlit.app/#call-pnl-heatmap 

An interactive **Streamlit web app** to visualize Black–Scholes option pricing and profit & loss (PNL) for call and put options.  
The app generates **4 heatmaps** based on user inputs:  

1. Call Option Value  
2. Put Option Value  
3. Call Option PNL (with purchase price)  
4. Put Option PNL (with purchase price)  

Green represents **positive values (profit)** and red represents **negative values (loss)**.

---

## 🚀 Features
- Input parameters:
  - Stock price (S₀)  
  - Strike price (K)  
  - Time to maturity (T)  
  - Risk-free rate (r)  
  - Volatility (σ)  
  - Purchase price (for both Call and Put)  
- Dynamic Black–Scholes pricing calculation  
- Heatmaps for option values and PNL  
- Customizable stock price and volatility ranges  

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/black-scholes-heatmaps.git
   cd black-scholes-heatmaps
2. Create and activate a virtual environment (optional but recommended):
     ```bash
    git clone python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
3. Install dependencies:
   ```bash
    pip install -r requirements.txt
## ▶️ Usage
Run the app locally:
streamlit run streamlit_app.py
Then open the link provided in your terminal (usually http://localhost:8501).
## 📦 Requirements
See requirements.txt:
1. streamlit
2. pandas
3. numpy
4. scipy
5. plotly
6. matplotlib
7. seaborn
## 📊 Example Dashboard
Once launched, you’ll see a dashboard with four heatmaps:
  🔹 Option Values 
  Call Value Heatmap
  Put Value Heatmap
  🔹 Option PNL
  Call PNL Heatmap
  Put PNL Heatmap
## 📖 Background
This project implements the Black–Scholes Model, a fundamental financial model for pricing European call and put options.
PNL is calculated as:
PNL = Option Value – Purchase Price
## 📝 License
This project is licensed under the MIT License.
