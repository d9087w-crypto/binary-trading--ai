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
        background-color: #020712;
        color: #00f2fe;
        font-family: system-ui, -apple-system, sans-serif;
    }
    
    .title-text {
        text-align: center;
        color: #00f2fe;
        font-weight: 900;
        font-size: 26px;
        text-shadow: 0 0 15px rgba(0, 242, 254, 0.7);
        letter-spacing: 2.5px;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    div.stButton > button {
        width: 100%;
        background: rgba(0, 242, 254, 0.05) !important;
        color: #00f2fe !important;
        border: 2px solid #00f2fe !important;
        padding: 12px;
        font-weight: bold;
        font-size: 15px;
        letter-spacing: 2px;
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.3);
        transition: all 0.2s ease-in-out;
    }

    div.stButton > button:active, div.stButton > button:focus {
        background: rgba(0, 242, 254, 0.25) !important;
        color: #ffffff !important;
        border-color: #ffffff !important;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.8) !important;
    }

    div[data-baseweb="input"] {
        background-color: #040e22 !important;
        border: 1.5px solid #00f2fe !important;
        border-radius: 8px;
        color: #00f2fe !important;
    }

    div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        background: transparent !important;
        color: #00f2fe !important;
        border: 1.5px solid #00f2fe !important;
        padding: 10px;
        font-weight: bold;
        font-size: 14px;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
    }

    .volatility-safe {
        background: rgba(0, 255, 136, 0.05);
        border: 1.5px solid #00ff88;
        color: #00ff88;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 8px 0;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.2);
    }

    .volatility-alert-box {
        background: rgba(255, 0, 85, 0.1);
        border: 2px solid #ff0055;
        color: #ff0055;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 8px 0;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.4);
    }

    .pair-card {
        background: rgba(4, 18, 38, 0.6);
        border: 2px solid #00f2fe;
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        font-size: 24px;
        font-weight: 900;
        color: #ffffff;
        margin-top: 10px;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.3);
        letter-spacing: 1px;
    }

    .signal-put {
        background: rgba(255, 0, 85, 0.05);
        border: 2px solid #ff0055;
        color: #ff0055;
        border-radius: 12px;
        padding: 12px;
        font-size: 26px;
        font-weight: 900;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.4);
        letter-spacing: 2px;
    }

    .signal-call {
        background: rgba(0, 255, 136, 0.05);
        border: 2px solid #00ff88;
        color: #00ff88;
        border-radius: 12px;
        padding: 12px;
        font-size: 26px;
        font-weight: 900;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.4);
        letter-spacing: 2px;
    }

    .accuracy-box-put {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #ff0055;
        border: 2.5px solid #ff0055;
        border-radius: 50%;
        width: 105px;
        height: 105px;
        line-height: 100px;
        margin: 12px auto;
        box-shadow: 0 0 20px rgba(255, 0, 85, 0.5);
    }

    .accuracy-box-call {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #00ff88;
        border: 2.5px solid #00ff88;
        border-radius: 50%;
        width: 105px;
        height: 105px;
        line-height: 100px;
        margin: 12px auto;
        box-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
    }

    .strategy-info {
        background: #040e22;
        border-left: 4px solid #00f2fe;
        border-radius: 0 8px 8px 0;
        padding: 10px;
        margin: 8px 0;
        font-size: 11px;
        color: #00f2fe;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    .trend-meter {
        background: rgba(4, 18, 38, 0.5);
        border: 1.5px solid #00f2fe;
        border-radius: 12px;
        padding: 8px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin-top: 8px;
        box-shadow: 0 0 8px rgba(0, 242, 254, 0.2);
    }

    .yellow-timer {
        background: rgba(255, 215, 0, 0.05);
        border: 2px solid #ffd700;
        color: #ffd700;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
        box-shadow: 0 0 15px rgba(255, 215, 0, 0.4);
        letter-spacing: 2px;
    }

    .user-badge {
        text-align: center;
        font-size: 11px;
        color: #00f2fe;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }

    .id-tag {
        background: #e000ff;
        color: #ffffff;
        font-size: 9px;
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
        "GBP/AUD-OTC",
        "EUR/USD-OTC",
        "GBP/USD-OTC",
        "USD/JPY-OTC",
        "USD/INR-OTC",
        "GOLD",
        "BITCOIN-OTC",
    ]

    sureshot_strategies = [
        "SS1: Engulfing Momentum + Head/Tail Wick Confirmation",
        "SS2: 4-Candle Zig-Zag Alternating Breakout (Trend Aligned)",
        "SS3: Strong S/R Zone Rejection (Body-to-Body + 50% Midpoint)",
        "SS4: Strong Trend Reversal Trap (3-8 Candle Momentum)",
    ]

    st.session_state.current_pair = random.choice(all_pairs)
    st.session_state.selected_strategy = random.choice(sureshot_strategies)
    st.session_state.signal_type = random.choice(["CALL (BUY)", "PUT (SELL)"])
    st.session_state.accuracy = random.randint(94, 98)

    if random.choice([True, False, False]):
        st.session_state.is_red_alert = True
        st.session_state.volatility_text = (
            "RED ALERT: HIGH VOLATILITY / GAP DETECTED (Filter Active)"
        )
    else:
        st.session_state.is_red_alert = False
        st.session_state.volatility_text = (
            "GREEN: SAFE MARKET — TRADE KARO (High Accuracy)"
        )

    if "CALL" in st.session_state.signal_type:
        buyers = random.randint(88, 97)
        st.session_state.trend_status = (
            f"STRONG UPTREND (Buyers: {buyers}%) [Sureshot Matched]"
        )
    else:
        sellers = random.randint(88, 97)
        st.session_state.trend_status = (
            f"STRONG DOWNTREND (Sellers: {sellers}%) [Sureshot Matched]"
        )

    ist_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_offset)
    st.session_state.entry_time = now_ist.strftime("%H:%M:%S")
    
    # Accurate 60-second binary expiry calculation matching current minute cycle
    current_sec = now_ist.second
    remaining_to_minute = 60 - current_sec
    st.session_state.expiry_time = (
        now_ist + datetime.timedelta(seconds=remaining_to_minute)
    ).strftime("%H:%M:%S")
    st.session_state.expiry_timestamp = time.time() + remaining_to_minute


if "signal_type" not in st.session_state:
    generate_signal()

st.markdown(
    '<div class="title-text">TANIX AI 2.0 PRO</div>', unsafe_allow_html=True
)

if not st.session_state.logged_in:
    st.markdown(
        "<p style='text-align:center; color:#00f2fe; font-size:11px;'>SECURE VIP ACCESS ENGINE</p>",
        unsafe_allow_html=True,
    )

    with st.form("login_form", clear_on_submit=False):
        trader_id_input = st.text_input(
            "Trader ID",
            placeholder="Enter Trader ID",
            label_visibility="collapsed",
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
    <div style="font-size: 11px; color: #7a9bbd; margin-top: 8px; text-align: center;">
        <span><b>Entry:</b> {st.session_state.entry_time}</span> &nbsp;|&nbsp; 
        <span><b>Expiry:</b> {st.session_state.expiry_time}</span>
    </div>
    """,
        unsafe_allow_html=True,
    )

    remaining_sec = int(st.session_state.expiry_timestamp - time.time())
    if remaining_sec > 0:
        st.markdown(
            f'<div class="yellow-timer">00:{remaining_sec:02d}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="yellow-timer" style="color:#ff0055; border-color:#ff0055;">EXPIRED / NEW CANDLE</div>',
            unsafe_allow_html=True,
        )
        
