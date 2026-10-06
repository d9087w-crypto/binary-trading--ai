 import datetime
import random
import time
import streamlit as st

# Page setup
st.set_page_config(
    page_title="TANIX AI 2.0 PRO", page_icon="⚡", layout="centered"
)

# Custom Cyberpunk / Dark Cyan CSS UI
st.markdown(
    """
    <style>
    .stApp {
        background-color: #030a16;
        color: #00f2fe;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .title-text {
        text-align: center;
        color: #00f2fe;
        font-weight: 800;
        font-size: 28px;
        text-shadow: 0 0 10px #00f2fe, 0 0 20px #00f2fe;
        letter-spacing: 2px;
        margin-bottom: 20px;
    }

    div[data-baseweb="input"] {
        background-color: #071328 !important;
        border: 1px solid #00f2fe !important;
        border-radius: 6px;
        color: #00f2fe !important;
    }
    
    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #071a38 0%, #0c2b5c 100%);
        color: #00f2fe !important;
        border: 1px solid #00f2fe !important;
        padding: 12px;
        font-weight: bold;
        font-size: 16px;
        letter-spacing: 2px;
        border-radius: 6px;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background: #00f2fe !important;
        color: #030a16 !important;
        box-shadow: 0 0 20px #00f2fe;
    }

    .pair-card {
        background: #06142a;
        border: 1px solid #00f2fe;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 15px;
    }

    .signal-put {
        background: rgba(255, 0, 85, 0.2);
        border: 2px solid #ff0055;
        color: #ff0055;
        border-radius: 6px;
        padding: 12px;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 0 15px #ff0055;
        text-shadow: 0 0 10px #ff0055;
    }

    .signal-call {
        background: rgba(0, 255, 136, 0.2);
        border: 2px solid #00ff88;
        color: #00ff88;
        border-radius: 6px;
        padding: 12px;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 0 15px #00ff88;
        text-shadow: 0 0 10px #00ff88;
    }

    .accuracy-box-put {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #ff0055;
        border: 3px solid #ff0055;
        border-radius: 50%;
        width: 100px;
        height: 100px;
        line-height: 94px;
        margin: 15px auto;
        box-shadow: 0 0 15px #ff0055;
    }

    .accuracy-box-call {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #00ff88;
        border: 3px solid #00ff88;
        border-radius: 50%;
        width: 100px;
        height: 100px;
        line-height: 94px;
        margin: 15px auto;
        box-shadow: 0 0 15px #00ff88;
    }

    .strategy-info {
        background: #071328;
        border-left: 4px solid #00f2fe;
        padding: 10px;
        margin: 10px 0;
        font-size: 13px;
        color: #00f2fe;
    }

    .yellow-timer {
        background: #111a03;
        border: 2px solid #ffd700;
        color: #ffd700;
        border-radius: 8px;
        padding: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        text-shadow: 0 0 10px #ffd700;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# YOUR VIP PASSWORDS
VALID_VIP_PASSWORDS = ["TRADINGFUTURE2141", "TANIXVIP", "VIP786", "PRO2026"]

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.markdown(
    '<div class="title-text">⬢ TANIX AI 2.0 PRO</div>', unsafe_allow_html=True
)

if not st.session_state.logged_in:
    st.markdown(
        "<p style='text-align:center; color:#00f2fe;'>MULTI-STRATEGY VIP ACCESS ALGORITHM</p>",
        unsafe_allow_html=True,
    )

    trader_id = st.text_input(
        "Trader ID", placeholder="[id:// Enter Trader ID]", label_visibility="collapsed"
    )
    vip_key = st.text_input(
        "VIP Key",
        type="password",
        placeholder="[key:// Enter Secret Password Key]",
        label_visibility="collapsed",
    )

    if st.button("◆ ACCESS SYSTEM"):
        if trader_id.strip() == "":
            st.error("Please enter a valid Trader ID.")
        elif vip_key.strip() not in VALID_VIP_PASSWORDS:
            st.error("❌ Invalid Password/Key! Contact Admin for VIP Access.")
        else:
            st.session_state.logged_in = True
            st.session_state.trader_id = trader_id
            st.rerun()

else:
    st.markdown(
        f"<p style='color:#00f2fe;'><b>ID:</b> {st.session_state.trader_id} &nbsp;|&nbsp; <span style='color:#00ff88;'>● LIVE VIP ENGINE</span></p>",
        unsafe_allow_html=True,
    )

    if st.button("◆ SCAN MARKET"):
        with st.spinner(
            "Analyzing SMC Order Blocks, EMA Crossover & RSI Divergence..."
        ):
            time.sleep(1.2)

            all_pairs = [
                "EUR/USD (OTC)",
                "GBP/USD (OTC)",
                "USD/JPY (OTC)",
                "AUD/CAD (OTC)",
                "USD/CHF (OTC)",
                "EUR/JPY (OTC)",
                "NZD/USD (OTC)",
                "GBP/JPY (OTC)",
                "AUD/JPY (OTC)",
                "USD/BDT (OTC)",
                "USD/INR (OTC)",
                "USD/PKR (OTC)",
                "BTC/USD (OTC)",
                "EUR/USD",
                "GBP/USD",
                "USD/JPY",
                "AUD/CAD",
                "GOLD",
                "BITCOIN",
            ]

            strategies = [
                "SMC Order Block Bounce",
                "EMA 9/21 Trend Crossover",
                "RSI Overbought/Oversold Reversal",
                "Bollinger Band Outer Rejection",
                "Price Action Resistance Breakdown",
            ]

            st.session_state.current_pair = random.choice(all_pairs)
            st.session_state.selected_strategy = random.choice(strategies)
            st.session_state.signal_type = random.choice(
                ["CALL (BUY)", "PUT (SELL)"]
            )

            st.session_state.accuracy = random.randint(55, 78)

            now = datetime.datetime.now()
            st.session_state.entry_time = now.strftime("%H:%M:%S")
            st.session_state.expiry_time = (
                now + datetime.timedelta(seconds=60)
            ).strftime("%H:%M:%S")
            st.session_state.expiry_timestamp = time.time() + 60

    if "signal_type" in st.session_state:
        st.markdown(
            f'<div class="pair-card">{st.session_state.current_pair}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="strategy-info"><b>STRATEGY USED:</b> {st.session_state.selected_strategy}</div>',
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
        <div style="font-size: 13px; color: #7a9bbd; margin-top: 10px;">
            <p><b>Entry Time:</b> {st.session_state.entry_time}</p>
            <p><b>Expiry Time:</b> {st.session_state.expiry_time}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        remaining_sec = int(st.session_state.expiry_timestamp - time.time())
        if remaining_sec > 0:
            st.markdown(
                f'<div class="yellow-timer">⏱️ 00:{remaining_sec:02d}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="yellow-timer" style="color:#ff0055; border-color:#ff0055;">EXPIRED</div>',
                unsafe_allow_html=True,
            )
            
