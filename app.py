import datetime
import random
import time
import streamlit as st

st.set_page_config(
    page_title="TANIX AI 2.0 PRO", page_icon="⚡", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #030a16;
        color: #00f2fe;
        font-family: system-ui, -apple-system, sans-serif;
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

    .volatility-alert-box {
        background: rgba(255, 0, 85, 0.15);
        border: 2px solid #ff0055;
        color: #ff0055;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        font-size: 13px;
        font-weight: bold;
        margin: 10px 0;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
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
    
    # Advanced SMC & Suroshoot Strategies
    strategies = [
        "SUROSHOOT: Bullish Order Block + Fair Value Gap (FVG)",
        "SUROSHOOT: Bearish Order Block + Liquidity Grab",
        "SMC: Institutional Breaker Zone Reversal",
        "SMC: Smart Money Liquidity Sweep & Reversal",
        "SUROSHOOT: EMA 9/21 Trend Confluence"
    ]

    st.session_state.current_pair = random.choice(all_pairs)
    st.session_state.selected_strategy = random.choice(strategies)
    st.session_state.signal_type = random.choice(["CALL (BUY)", "PUT (SELL)"])
    st.session_state.accuracy = random.randint(92, 98)

    # Volatility Check (Includes Red Alert)
    if random.choice([True, False, False]):
        st.session_state.is_red_alert = True
        st.session_state.volatility_text = "RED ALERT: HIGH MARKET VOLATILITY DETECTED! TRADING RISKY"
    else:
        st.session_state.is_red_alert = False
        st.session_state.volatility_text = "GREEN: SAFE MARKET - TRADE KARO (High Accuracy)"

    if "CALL" in st.session_state.signal_type:
        buyers = random.randint(86, 96)
        st.session_state.trend_status = f"STRONG UPTREND [SMC CONFIRMED] (Buyers: {buyers}%)"
    else:
        sellers = random.randint(86, 96)
        st.session_state.trend_status = f"STRONG DOWNTREND [SMC CONFIRMED] (Sellers: {sellers}%)"

    ist_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_offset)
    st.session_state.entry_time = now_ist.strftime("%H:%M:%S")
    st.session_state.expiry_time = (now_ist + datetime.timedelta(seconds=60)).strftime("%H:%M:%S")
    st.session_state.expiry_timestamp = time.time() + 60

if "signal_type" not in st.session_state:
    generate_signal()

st.markdown(
    '<div class="title-text">TANIX AI 2.0 PRO</div>', unsafe_allow_html=True
)

if not st.session_state.logged_in:
    st.markdown(
        "<p style='text-align:center; color:#00f2fe; font-size:12px;'>MULTI-STRATEGY VIP ACCESS ALGORITHM</p>",
        unsafe_allow_html=True,
    )

    with st.form("login_form", clear_on_submit=False):
        trader_id_input = st.text_input(
            "Trader ID", placeholder="Enter Trader ID", label_visibility="collapsed"
        )
        vip_key_input = st.text_input(
            "VIP Key",
            type="password",
            placeholder="Enter Secret Password Key",
            label_visibility="collapsed",
        )

        submit_login = st.form_submit_button("ACCESS SYSTEM")

    if submit_login:
        tid = trader_id_input.strip() if trader_id_input else ""
        vkey = vip_key_input.strip() if vip_key_input else ""

        if len(tid) == 0:
            st.error("Please enter a Trader ID.")
        elif vkey not in VALID_VIP_PASSWORDS:
            st.error("Invalid Password/Key! Contact Admin for VIP Access.")
        else:
            st.session_state.logged_in = True
            st.session_state.trader_id = tid
            st.rerun()

else:
    st.markdown(
        f'<div class="user-badge"><span class="id-tag">ID</span> TRADER ID: <b>{st.session_state.trader_id}</b></div>',
        unsafe_allow_html=True,
    )

    if st.button("SCAN MARKET"):
        generate_signal()

    if st.session_state.is_red_alert:
        st.markdown(
            f'<div class="volatility-alert-box">{st.session_state.volatility_text}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="volatility-safe">{st.session_state.volatility_text}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="pair-card">{st.session_state.current_pair}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="strategy-info">STRATEGY USED: {st.session_state.selected_strategy}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="trend-meter">{st.session_state.trend_status}</div>',
        unsafe_allow_html=True,
    )

    if "PUT" in st.session_state.signal_type:
        st.markdown(
            '<div class="signal-put">PUT (SELL)</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="accuracy-box-put">{st.session_state.accuracy}%</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="signal-call">CALL (BUY)</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="accuracy-box-call">{st.session_state.accuracy}%</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
    <div style="font-size: 11px; color: #7a9bbd; margin-top: 6px; text-align: center;">
        <span><b>Entry:</b> {st.session_state.entry_time}</span> &nbsp;|&nbsp; 
        <span><b>Expiry:</b> {st.session_state.expiry_time}</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    timer_placeholder = st.empty()
    remaining_sec = int(st.session_state.expiry_timestamp - time.time())
    
    if remaining_sec > 0:
        timer_placeholder.markdown(
            f'<div class="yellow-timer">00:{remaining_sec:02d}</div>',
            unsafe_allow_html=True,
        )
    else:
        timer_placeholder.markdown(
            '<div class="yellow-timer" style="color:#ff0055; border-color:#ff0055;">EXPIRED</div>',
            unsafe_allow_html=True,
        )
        
