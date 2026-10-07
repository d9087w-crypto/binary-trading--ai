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
        font-size: 26px;
        text-shadow: 0 0 10px #00f2fe, 0 0 20px #00f2fe;
        letter-spacing: 2px;
        margin-bottom: 12px;
    }

    div[data-baseweb="input"] {
        background-color: #071328 !important;
        border: 1px solid #00f2fe !important;
        border-radius: 6px;
        color: #00f2fe !important;
    }
    
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        background: linear-gradient(135deg, #071a38 0%, #0c2b5c 100%);
        color: #00f2fe !important;
        border: 1px solid #00f2fe !important;
        padding: 10px;
        font-weight: bold;
        font-size: 15px;
        letter-spacing: 1.5px;
        border-radius: 20px;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.3);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        background: #00f2fe !important;
        color: #030a16 !important;
        box-shadow: 0 0 20px #00f2fe;
    }

    /* Volatility Status Badges */
    .volatility-safe {
        background: rgba(0, 255, 136, 0.1);
        border: 1px solid #00ff88;
        color: #00ff88;
        border-radius: 20px;
        padding: 6px 12px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 8px 0;
        box-shadow: 0 0 10px rgba(0, 255, 136, 0.2);
    }

    .volatility-moderate {
        background: rgba(0, 242, 254, 0.1);
        border: 1px solid #00f2fe;
        color: #00f2fe;
        border-radius: 20px;
        padding: 6px 12px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 8px 0;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.2);
    }

    .pair-card {
        background: linear-gradient(145deg, #06142a 0%, #091f42 100%);
        border: 1px solid #00f2fe;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 8px;
    }

    .signal-put {
        background: rgba(255, 0, 85, 0.15);
        border: 1.5px solid #ff0055;
        color: #ff0055;
        border-radius: 8px;
        padding: 8px;
        font-size: 24px;
        font-weight: 900;
        text-align: center;
        margin: 8px 0;
        box-shadow: 0 0 12px #ff0055;
    }

    .signal-call {
        background: rgba(0, 255, 136, 0.15);
        border: 1.5px solid #00ff88;
        color: #00ff88;
        border-radius: 8px;
        padding: 8px;
        font-size: 24px;
        font-weight: 900;
        text-align: center;
        margin: 8px 0;
        box-shadow: 0 0 12px #00ff88;
    }

    .accuracy-box-put {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #ff0055;
        border: 2px solid #ff0055;
        border-radius: 50%;
        width: 90px;
        height: 90px;
        line-height: 86px;
        margin: 10px auto;
        box-shadow: 0 0 12px #ff0055;
    }

    .accuracy-box-call {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #00ff88;
        border: 2px solid #00ff88;
        border-radius: 50%;
        width: 90px;
        height: 90px;
        line-height: 86px;
        margin: 10px auto;
        box-shadow: 0 0 12px #00ff88;
    }

    .strategy-info {
        background: #071328;
        border-left: 3px solid #00f2fe;
        border-radius: 0 4px 4px 0;
        padding: 8px;
        margin: 8px 0;
        font-size: 12px;
        color: #00f2fe;
    }

    .trend-meter {
        background: #091a34;
        border: 1px solid #00f2fe;
        border-radius: 15px;
        padding: 6px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin-top: 6px;
    }

    .yellow-timer {
        background: #111a03;
        border: 1.5px solid #ffd700;
        color: #ffd700;
        border-radius: 8px;
        padding: 8px;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        margin-top: 12px;
    }

    /* Session Tracker Capsule Header */
    .session-card {
        background: rgba(7, 19, 40, 0.8);
        border: 1px solid #00f2fe;
        border-radius: 12px;
        padding: 8px 10px;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 12px;
        font-size: 11px;
        flex-wrap: nowrap;
        white-space: nowrap;
    }

    .session-tag {
        background: #d946ef;
        color: #ffffff;
        font-weight: bold;
        padding: 2px 5px;
        border-radius: 4px;
        font-size: 10px;
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

if "session_wins" not in st.session_state:
    st.session_state.session_wins = 18
if "session_losses" not in st.session_state:
    st.session_state.session_losses = 3

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

# Page load hote hi default data ready rahega
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
            st.error("❌ Invalid Password/Key! Contact Admin for VIP Access.")
        else:
            st.session_state.logged_in = True
            st.session_state.trader_id = tid
            st.rerun()

else:
    total_trades = st.session_state.session_wins + st.session_state.session_losses
    win_rate = round((st.session_state.session_wins / total_trades) * 100, 1) if total_trades > 0 else 0

    st.markdown(
        f"""
        <div class="session-card">
            <div><span class="session-tag">ID</span> <b style="color:#00f2fe;">{st.session_state.trader_id}</b></div>
            <div>✅ <b>Wins:</b> <span style="color:#00ff88;">{st.session_state.session_wins}</span></div>
            <div>❌ <b>Loss:</b> <span style="color:#ff0055;">{st.session_state.session_losses}</span></div>
            <div>🎯 <b>WinRate:</b> <span style="color:#ffd700;">{win_rate}%</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("◆ SCAN MARKET"):
        status_box = st.empty()
        status_box.info(f"🔗 Scanning market for ID ({st.session_state.trader_id})...")
        time.sleep(0.3)
        status_box.empty()

        if random.random() > 0.15:
            st.session_state.session_wins += 1
        else:
            st.session_state.session_losses += 1

        generate_signal()

    if st.session_state.volatility_type == "safe":
        st.markdown(
            f'<div class="volatility-safe">{st.session_state.volatility_text}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="volatility-moderate">{st.session_state.volatility_text}</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<div class="pair-card">{st.session_state.current_pair}</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="strategy-info"><b>STRATEGY USED:</b> {st.session_state.selected_strategy}</div>',
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
            f'<div class="yellow-timer">⏱️ 00:{remaining_sec:02d}</div>',
            unsafe_allow_html=True,
        )
    else:
        timer_placeholder.markdown(
            '<div class="yellow-timer" style="color:#ff0055; border-color:#ff0055;">EXPIRED</div>',
            unsafe_allow_html=True,
    )
    
