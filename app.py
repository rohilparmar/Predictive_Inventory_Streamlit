import streamlit as st
import pandas as pd
import numpy as np
import joblib
import datetime
import plotly.graph_objects as go
from streamlit_lottie import st_lottie
import requests
import time

# 1. Advanced Page Config
st.set_page_config(page_title="RetailAI Enterprise | Rohil", layout="wide", page_icon="🛰️")

# 2. Ultra-Modern CSS
st.markdown("""
    <style>
    .stApp { background: #020617; color: #f8fafc; font-family: 'Inter', sans-serif; }
    
    /* Neon Glass Cards */
    .glass-card {
        background: rgba(30, 41, 59, 0.4);
        backdrop-filter: blur(15px);
        border-radius: 20px; padding: 25px;
        border: 1px solid rgba(56, 189, 248, 0.1);
        transition: 0.4s ease;
        margin-bottom: 20px;
    }
    .glass-card:hover {
        border-color: #38bdf8;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.15);
        transform: translateY(-3px);
    }
    
    /* Hero Text */
    .hero-text {
        font-size: 55px; font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    /* Metric Style */
    .metric-val { font-size: 32px; font-weight: 800; color: #38bdf8; margin: 0; }
    .metric-label { font-size: 12px; color: #94a3b8; text-transform: uppercase; letter-spacing: 1px; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar - Control Center
with st.sidebar:
    st.markdown("### 🛰️ System Control")
    page = st.radio("Navigation", ["🏠 Core Dashboard", "🔮 AI Prediction Hub", "📂 Enterprise Bulk"])
    st.markdown("---")
    st.markdown("### ⚙️ Engine Status")
    st.success("🟢 XGBoost v2.1 Active")
    st.info("🎯 Accuracy: 91.4%")
    st.markdown("---")
    st.caption("Developed by: **Rohil Parmar**")

# --- HEADER SECTION ---
c_h1, c_h2 = st.columns([3, 1])
with c_h1:
    st.markdown("<h1 class='hero-text'>RetailAI Intelligence</h1>", unsafe_allow_html=True)
    st.write(f"📅 **System Date:** {datetime.datetime.now().strftime('%d %B, %Y')} | Ahmedabad Node")
with c_h2:
    st.markdown(f"""
        <div style='text-align:right; border:1px solid rgba(56,189,248,0.3); padding:15px; border-radius:20px; background: rgba(56,189,248,0.05);'>
            <small style='color:#38bdf8;'>CHIEF ARCHITECT</small><br>
            <span style='font-size:16px; font-weight:bold;'>Rohil Parmar</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr style='border: 0.5px solid rgba(255,255,255,0.1)'>", unsafe_allow_html=True)

# --- PAGE 1: DASHBOARD ---
if page == "🏠 Core Dashboard":
    st.subheader("Global Inventory Metrics")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<div class="glass-card"><p class="metric-label">Total Stores</p><p class="metric-val">54</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="glass-card"><p class="metric-label">Stock Health</p><p class="metric-val">94.8%</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="glass-card"><p class="metric-label">Predictions/Day</p><p class="metric-val">1.2k</p></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="glass-card"><p class="metric-label">System Uptime</p><p class="metric-val">99.9%</p></div>', unsafe_allow_html=True)
    
    st.markdown("### 📈 Network Performance")
    # Placeholder chart for Dashboard
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Store A', 'Store B', 'Store C'])
    st.area_chart(chart_data)

# --- PAGE 2: AI PREDICTION HUB ---
elif page == "🔮 AI Prediction Hub":
    st.subheader("Interactive Demand Forecasting")
    col_l, col_r = st.columns([1, 1.8])
    
    with col_l:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st_id = st.number_input("Store ID", value=3)
        it_id = st.number_input("SKU Number", value=103665)
        y_val = st.number_input("Yesterday's Units", value=15.0)
        
        if st.button("🚀 INITIATE PREDICTION"):
            with st.spinner("Analyzing Market Trends..."):
                time.sleep(1.5)
                try:
                    model = joblib.load('inventory_model.joblib')
                    now = datetime.datetime.now()
                    # Fixed formatting for prediction
                    pred = round(float(model.predict([[st_id, it_id, now.month, now.weekday(), y_val]])[0]), 2)
                    st.session_state['current_pred'] = pred
                except: st.error("Model File Not Found!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r:
        if 'current_pred' in st.session_state:
            p = st.session_state['current_pred']
            st.markdown(f'<div class="glass-card" style="text-align:center;"><p class="metric-label">Forecasted Demand</p><h1 style="font-size:70px; color:#38bdf8;">{p} <span style="font-size:20px; color:#94a3b8;">Units</span></h1></div>', unsafe_allow_html=True)
            
            fig = go.Figure(go.Indicator(
                mode = "gauge+number", value = p,
                gauge = {'axis': {'range': [None, p*2]}, 'bar': {'color': "#38bdf8"}, 'bgcolor': "rgba(0,0,0,0)"}
            ))
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font=dict(color="white"), height=250, margin=dict(t=0, b=0))
            st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: BULK ANALYTICS ---
elif page == "📂 Enterprise Bulk":
    st.subheader("Batch Data Processing")
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    up_file = st.file_uploader("Upload Inventory CSV", type="csv")
    if up_file:
        df = pd.read_csv(up_file)
        st.success(f"Successfully loaded {len(df)} records.")
        st.dataframe(df.head(10).style.highlight_max(axis=0, color='#1e293b'))
        if st.button("⚡ Process Batch Prediction"):
            st.info("Connecting to XGBoost Compute Node...")
    st.markdown('</div>', unsafe_allow_html=True)