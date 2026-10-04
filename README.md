import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Binary Trading AI Signal Assistant", 
    page_icon="📈", 
    layout="centered"
)

st.title("📈 Binary Trading Signal & Risk Assistant")
st.write("1-minute aur 5-minute chart screenshots analyze karein aur risk limits check karein.")

st.markdown("---")

# Chart Upload
st.subheader("1. Chart Screenshot Upload Karein")
uploaded_file = st.file_uploader("TradingView / Broker Chart Screenshot Upload Karein", type=["png", "jpg", "jpeg"])

# Risk Inputs
st.subheader("2. Session & Capital Status")
col1, col2 = st.columns(2)
with col1:
    account_drawdown = st.number_input("Aaj Ka Drawdown (%)", min_value=0.0, max_value=100.0, value=0.0, step=0.5)
with col2:
    consecutive_losses = st.number_input("Consecutive Loss Trades", min_value=0, max_value=10, value=0, step=1)

st.markdown("---")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Chart Screenshot", use_column_width=True)
    
    if st.button("🔍 Run Confluence & Risk Analysis", type="primary"):
        st.subheader("📊 Analysis Results")
        
        # Risk Evaluation First
        if account_drawdown >= 3.0 or consecutive_losses >= 3:
            st.error("🚨 **STAND DOWN / NO TRADE**")
            st.warning("""
            **Risk Limit Alert:**
            - Total Daily Loss >= 3% ya Consecutive Losses >= 3 reach ho gaya hai.
            - Rules ke mutabiq aaj trading immediately STOP karein.
            """)
        else:
            st.success("✅ **RISK CHECK PASSED** (Capital limits inside safe zone)")
            
            st.markdown("""
            ### 🎯 Mandatory Technical Confluence Checklist (3/3 Required)
            Trade lene se pehle chart par in teeno cheezon ko confirm karein:
            
            1. **Trend Check (200 EMA):**
               - Above 200 EMA = *CALL Setups Only*
               - Below 200 EMA = *PUT Setups Only*
            2. **HTF Level Check:** Price Support Zone (CALL) ya Resistance Zone (PUT) par hona chahiye.
            3. **Indicator Confluence (3/3):**
               - **RSI (14):** Oversold < 30 (CALL) / Overbought > 70 (PUT)
               - **Bollinger Bands (20,2):** Lower Band Touch (CALL) / Upper Band Touch (PUT)
               - **MACD (12,26,9):** Bullish Crossover (CALL) / Bearish Crossover (PUT)
            
            > ⚠️ **Note:** Agar 3/3 confluence nahi mil raha hai, toh trade **SKIP** karein!
            """)
            
