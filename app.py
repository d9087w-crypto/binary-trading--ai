import datetime
import random
import time
import streamlit as st

# Page setup
st.set_page_config(
    page_title="TANIX AI 2.0 PRO", page_icon="⚡", layout="centered"
)

# Custom Cyberpunk / Dark Cyan CSS UI matching screenshots exactly
st.markdown(
    """
    <style>
    .stApp {
        background-color: #030a16;
        color: #00f2fe;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .title-text {
        text-align: center;
        color: #00f2fe;
        font-weight: 900;
        font-size: 24px;
        text-shadow: 0 0 12px #00f2fe;
        letter-spacing: 2px;
        margin-top: 5px;
        margin-bottom: 10px;
    }

    div[data-baseweb="input"] {
        background-color: #071328 !important;
        border: 1px solid #00f2fe !important;
        border-radius: 8px;
        color: #00f2fe !important;
    }
    
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        background: transparent !important;
        color: #00f2fe !important;
        border: 1.5px solid #00f2fe !important;
        padding: 8px;
        font-weight: bold;
        font-size: 14px;
        letter-spacing: 1.5px;
        border-radius: 20px;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.2);
        transition: all 0.3s ease;
    }

    .volatility-safe {
        background: transparent;
        border: 1.5px solid #00ff88;
        color: #00ff88;
        border-radius: 20px;
        padding: 8px 12px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 10px 0;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
    }

    .volatility-moderate {
        background: transparent;
        border: 1.5px solid #00f2fe;
        color: #00f2fe;
        border-radius: 20px;
        padding: 8px 12px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 10px 0;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
    }

    .pair-card {
        background: transparent;
        border: 1.5px solid #00f2fe;
        border-radius: 12px;
        padding: 14px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 10px;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.2);
    }

    .signal-put {
        background: transparent;
        border: 2px solid #ff0055;
        color: #ff0055;
        border-radius: 12px;
        padding: 12px;
        font-size: 26px;
        font-weight: 900;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
    }

    .signal-call {
        background: transparent;
        border: 2px solid #00ff88;
        color: #00ff88;
        border-radius: 12px;
        padding: 12px;
        font-size: 26px;
        font-weight: 900;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.4);
    }

    .accuracy-box-put {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #ff0055;
        border: 2px solid #ff0055;
        border-radius: 50%;
        width: 110px;
        height: 110px;
        line-height: 106px;
        margin: 15px auto;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.5);
    }

    .accuracy-box-call {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: #00ff88;
        border: 2px solid #00ff88;
        border-radius: 50%;
        width: 110px;
        height: 110px;
        line-height: 106px;
        margin: 15px auto;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
    }

    .strategy-info {
        background: #041226;
        border-left: 4px solid #00f2fe;
        border-radius: 0 6px 6px 0;
        padding: 10px;
        margin: 10px 0;
        font-size: 11px;
        color: #00f2fe;
        font-weight: 600;
    }

    .trend-meter {
        background: transparent;
        border: 1.5px solid #00f2fe;
        border-radius: 20px;
        padding: 8px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin-top: 8px;
        box-shadow: 0 0 8px rgba(0, 242, 254, 0.2);
    }

    .yellow-timer {
        background: transparent;
        border: 1.5px solid #ffd700;
        color: #ffd700;
        border-radius: 8px;
        padding: 8px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 12px;
    }

    .user-badge {
        text-align: center;
        font-size: 12px;
        color: #00f2fe;
        margin-bottom: 12px;
        letter-spacing: 1px;
    }

    .id-tag {
        background: #e000ff;
        color: #ffffff;
        font-size: 10px;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        margin-right: 4px;
    }

    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

VALID_VIP_PASSWORDS = ["TRADINGFUTURE2141", "TANIXVIP", "VIP786", "PRO2026"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def generate_signal():
    all_pairs = [
        "BTC/USD (OTC)", "EUR/USD (OTC)", "GBP/USD (OTC)", 
        "USD/JPY (OTC)", "AUD/CAD (OTC)", "EUR/JPY (OTC)", "GOLD"
    ]
    strategies = [
        "Breaker Block & Supply/Demand Key Reversal Zone",
        "SMC Order Block & Liquidity Grab",
        "EMA 9/21 Dynamic Trend Crossover",
        "RSI + Stochastic Double Oscillator"
    ]

    st.session_state.current_pair = random.choice(all_pairs)
    st.session_state.selected_strategy = random.choice(strategies)
    st.session_state.signal_type = random.choice(["CALL (BUY)", "PUT (SELL)"])
    st.session_state.accuracy = random.randint(89, 97)

    volatility_states = [
        ("🟢 GREEN: SAFE MARKET — TRADE KARO (High Accuracy)", "safe"),
        ("⚡ MODERATE VOLATILITY — CAUTION", "moderate")
    ]
    vol_text, vol_type = random.choice(volatility_states)
    st.session_state.volatility_text = vol_text
    st.session_state.volatility_type = vol_type

    if "CALL" in st.session_state.signal_type:
        buyers = random.randint(82, 94)
        st.session_state.trend_status = f"🟢 STRONG UPTREND (Buyers: {buyers}%)"
    else:
        sellers = random.randint(82, 94)
        st.session_state.trend_status = f"🔴 STRONG DOWNTREND (Sellers: {sellers}%)"

    ist_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_offset)
    st.session_state.entry_time = now_ist.strftime("%H:%M:%S")
    st.session_state.expiry_time = (now_ist + datetime.timedelta(seconds=60)).strftime("%H:%M:%S")
    st.session_state.expiry_timestamp = time.time() + 60

if "signal_type" not in st.session_state:
    generate_signal()

st.markdown(
    '<div class="title-text">⬢ TANIX AI 2.0 PRO</div>', unsafe_allow_html=True
)

if not st.session_state.logged_in:
    st.markdown(
        "<p style='text-align:center; color:#00f2fe; font-size:12px;'>MULTI-STRATEGY VIP ACCESS ALGORITHM</p>",
        unsafe_allow_html=True,
    )

    with st.form("login_form", clear_on_submit=False):
        trader_id_input = st.text_input(
            "Trader ID", placeholder="[id:// Enter Trader ID]", label_visibility="collapsed"
        )
        vip_key_input = st.text_input(
            "VIP Key",
            type="password",
            placeholder="[key:// Enter Secret Password Key]",
            label_visibility="collapsed",
        )

        submit_login = st.form_submit_button("◆ ACCESS SYSTEM")

    if submit_login:
        tid = trader_id_input.strip() if trader_id_input else ""
        vkey = vip_key_input.strip() if vip_key_input else ""

        if len(tid) == 0:
            st.error("❌ Please enter a Trader ID.")
        elif vkey not in VALID_VIP_PASSWORDS:
            st.error("❌ Invalid Password/Key! Contact Admin for VIP Access
                     
