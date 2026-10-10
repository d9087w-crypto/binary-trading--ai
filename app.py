import datetime
import random
import time
import streamlit as st

st.set_page_config(
    page_title="TANIX AI 2.0", page_icon="⚡", layout="centered"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #020712;
        color: #00f2fe;
        font-family: 'Space Mono', system-ui, -apple-system, sans-serif;
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

    /* Button active glow effect */
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

    .confidence-circle {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #00f2fe;
        border: 2.5px solid #00f2fe;
        border-radius: 50%;
        width: 105px;
        height: 105px;
        line-height: 100px;
        margin: 12px auto;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
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

    [data-testid="stForm"] {
        border: none !important;
        padding: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def generate_signal():
    all_pairs = ["GBP/AUD-OTC", "EUR/USD-OTC", "GBP/USD-OTC", "USD/JPY-OTC", "USD/INR-OTC", "GOLD", "BITCOIN-OTC"]
    st.session_state.current_pair = random.choice(all_pairs)
    st.session_state.signal_type = random.choice(["CALL (BUY)", "PUT (SELL)"])
    st.session_state.accuracy = random.randint(94, 98)

    ist_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    now_ist = datetime.datetime.now(ist_offset)
    st.session_state.entry_time = now_ist.strftime("%H:%M:%S")
    st.session_state.expiry_time = (now_ist + datetime.timedelta(seconds=60)).strftime("%H:%M:%S")
    st.session_state.expiry_timestamp = time.time() + 60

if "signal_type" not in st.session_state:
    generate_signal()

# Header matching reference
st.markdown('<div class="title-text">TANIX AI 2.0 PRO</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#00f2fe; font-size:11px;">SERVER TIME: {} | <span style="color:#00ff88;">● LIVE</span></p>'.format(datetime.datetime.now().strftime("%H:%M:%S")), unsafe_allow_html=True)

if not st.session_state.get("logged_in", False):
    with st.form("login_form"):
        trader_id_input = st.text_input("Trader ID", placeholder="Enter ID")
        vip_key_input = st.text_input("VIP Key", type="password", placeholder="Enter Password")
        if st.form_submit_button("ACCESS SYSTEM"):
            st.session_state.logged_in = True
            st.rerun()
else:
    st.markdown('<p style="text-align:center; color:#e000ff; font-size:11px;">ID: <b>{}</b></p>'.format(st.session_state.get("trader_id", "141413868")), unsafe_allow_html=True)

    if st.button("SCAN MARKET"):
        generate_signal()

    st.markdown('<div class="pair-card">{}</div>'.format(st.session_state.current_pair), unsafe_allow_html=True)

    if "PUT" in st.session_state.signal_type:
        st.markdown('<div class="signal-put">PUT (SELL)</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="signal-call">CALL (BUY)</div>', unsafe_allow_html=True)

    st.markdown('<div class="confidence-circle">{}%</div><p style="text-align:center; color:#00f2fe; font-size:10px;">CONFIDENCE</p>'.format(st.session_state.accuracy), unsafe_allow_html=True)

    st.markdown(
        """
        <div style="font-size: 11px; color: #7a9bbd; margin-top: 8px; text-align: center; border-top: 1px solid #00f2fe; padding-top: 8px;">
            <span><b>GENERATED:</b> {}</span><br>
            <span><b>ENTRY TIME:</b> {}</span><br>
            <span><b>EXPIRY TIME:</b> {}</span>
        </div>
        """.format(datetime.datetime.now().strftime("%H:%M:%S"), st.session_state.entry_time, st.session_state.expiry_time),
        unsafe_allow_html=True,
    )

    remaining_sec = int(st.session_state.expiry_timestamp - time.time())
    if remaining_sec > 0:
        st.markdown(f'<div class="yellow-timer">00:{remaining_sec:02d}</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="yellow-timer" style="color:#ff0055; border-color:#ff0055;">EXPIRED</div>', unsafe_allow_html=True)
        
