# 📊 Black-Scholes Option Pricing & PNL Heatmaps

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
Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies:
pip install -r requirements.txt
▶️ Usage
Run the app locally:
streamlit run streamlit_app.py
Then open the link provided in your terminal (usually http://localhost:8501).
📦 Requirements
See requirements.txt:
streamlit
numpy
pandas
matplotlib
scipy
📊 Example
Once launched, you’ll see a dashboard with four heatmaps:
Top Left: Call Option Value
Top Right: Put Option Value
Bottom Left: Call Option PNL
Bottom Right: Put Option PNL
📖 Background
This project implements the Black–Scholes Model, a fundamental financial model for pricing European call and put options.
PNL is calculated as:
PNL = Option Value – Purchase Price
📝 License
This project is licensed under the MIT License.

---

Do you want me to also make the README **include example screenshots of the heatmaps** (placeholders now, so you can replace with real ones after running the app)?
You said:
sure 
ChatGPT said:
Perfect 👍 Here’s an updated README.md with placeholders for screenshots of your app’s 4 heatmaps.
# 📊 Black-Scholes Option Pricing & PNL Heatmaps

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
Create and activate a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies:
pip install -r requirements.txt
▶️ Usage
Run the app locally:
streamlit run streamlit_app.py
Then open the link provided in your terminal (usually http://localhost:8501).
📦 Requirements
See requirements.txt:
streamlit
numpy
pandas
matplotlib
scipy
📊 Example Dashboard
Once launched, you’ll see a dashboard with four heatmaps:
🔹 Option Values
Call Value Heatmap
Put Value Heatmap
🔹 Option PNL
Call PNL Heatmap
Put PNL Heatmap
Replace the screenshots/*.png files with your actual heatmap images after running the app.
📖 Background
This project implements the Black–Scholes Model, a fundamental financial model for pricing European call and put options.
PNL is calculated as:
PNL = Option Value – Purchase Price
📝 License
This project is licensed under the MIT License.
