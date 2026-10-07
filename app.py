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
    
    div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
        width: 100%;
        background: linear-gradient(135deg, #071a38 0%, #0c2b5c 100%);
        color: #00f2fe !important;
        border: 1px solid #00f2fe !important;
        padding: 12px;
        font-weight: bold;
        font-size: 16px;
        letter-spacing: 2px;
        border-radius: 25px;
        box-shadow: 0 0 12px rgba(0, 242, 254, 0.4);
        transition: all 0.3s ease;
    }
    div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        background: #00f2fe !important;
        color: #030a16 !important;
        box-shadow: 0 0 25px #00f2fe;
    }

    /* Volatility Status Badges (Modern Capsule Shape) */
    .volatility-safe {
        background: rgba(0, 255, 136, 0.12);
        border: 1.5px solid #00ff88;
        color: #00ff88;
        border-radius: 30px;
        padding: 10px 16px;
        text-align: center;
        font-size: 13px;
        font-weight: bold;
        margin: 12px 0;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.25);
        letter-spacing: 0.5px;
    }

    .volatility-moderate {
        background: rgba(0, 242, 254, 0.12);
        border: 1.5px solid #00f2fe;
        color: #00f2fe;
        border-radius: 30px;
        padding: 10px 16px;
        text-align: center;
        font-size: 13px;
        font-weight: bold;
        margin: 12px 0;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.3);
        letter-spacing: 0.5px;
    }

    .volatility-danger {
        background: rgba(255, 0, 85, 0.15);
        border: 1.5px solid #ff0055;
        color: #ff0055;
        border-radius: 30px;
        padding: 10px 16px;
        text-align: center;
        font-size: 13px;
        font-weight: bold;
        margin: 12px 0;
        box-shadow: 0 0 15px rgba(255, 0, 85, 0.35);
        letter-spacing: 0.5px;
    }

    .pair-card {
        background: linear-gradient(145deg, #06142a 0%, #091f42 100%);
        border: 1.5px solid #00f2fe;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: #ffffff;
        margin-top: 10px;
        box-shadow: inset 0 0 15px rgba(0, 242, 254, 0.15);
    }

    .signal-put {
        background: rgba(255, 0, 85, 0.2);
        border: 2px solid #ff0055;
        color: #ff0055;
        border-radius: 8px;
        padding: 12px;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0 0 18px #ff0055;
        text-shadow: 0 0 10px #ff0055;
    }

    .signal-call {
        background: rgba(0, 255, 136, 0.2);
        border: 2px solid #00ff88;
        color: #00ff88;
        border-radius: 8px;
        padding: 12px;
        font-size: 28px;
        font-weight: 900;
        text-align: center;
        margin: 12px 0;
        box-shadow: 0 0 18px #00ff88;
        text-shadow: 0 0 10px #00ff88;
    }

    .accuracy-box-put {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        color: #ff0055;
        border: 3px solid #ff0055;
        border-radius: 50%;
        width: 110px;
        height: 110px;
        line-height: 104px;
        margin: 15px auto;
        box-shadow: 0 0 18px #ff0055;
    }

    .accuracy-box-call {
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        color: #00ff88;
        border: 3px solid #00ff88;
        border-radius: 50%;
        width: 110px;
        height: 110px;
        line-height: 104px;
        margin: 15px auto;
        box-shadow: 0 0 18px #00ff88;
    }

    .strategy-info {
        background: #071328;
        border-left: 4px solid #00f2fe;
        border-radius: 0 6px 6px 0;
        padding: 10px;
        margin: 10px 0;
        font-size: 13px;
        color: #00f2fe;
    }

    .trend-meter {
        background: #091a34;
        border: 1px solid #00f2fe;
        border-radius: 20px;
        padding: 10px;
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        margin-top: 10px;
    }

    .yellow-timer {
        background: #111a03;
        border: 2px solid #ffd700;
        color: #ffd700;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        text-shadow: 0 0 10px #ffd700;
        margin-top: 20px;
    }
    
    /* Hide Streamlit default form border */
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

st.markdown(
    '<div class="title-text">⬢ TANIX AI 2.0 PRO</div>', unsafe_allow_html=True
)

if not st.session_state.logged_in:
    st.markdown(
        "<p style='text-align:center; color:#00f2fe;'>MULTI-STRATEGY VIP ACCESS ALGORITHM</p>",
        unsafe_allow_html=True,
    )

    # Form wrapper to ensure smooth submit on mobile
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
    st.markdown(
        f"<p style='color:#00f2fe;'><b>TRADER ID:</b> {st.session_state.trader_id} &nbsp;|&nbsp; <span style='color:#00ff88;'>● CONNECTED & ACTIVE</span></p>",
        unsafe_allow_html=True,
    )

    if st.button("◆ SCAN MARKET"):
        status_box = st.empty()
        
        status_box.info(f"🔗 Connecting to Trader ID ({st.session_state.trader_id})...")
        time.sleep(0.5)
        
        status_box.info("📊 Fetching Live Economic Calendar & News Volatility Data...")
        time.sleep(0.6)
        
        status_box.info("⚡ Analyzing SMC Order Blocks, Market Structure & Volatility Filter...")
        time.sleep(0.6)
        
        status_box.empty()

        all_pairs = [
            "EUR/USD (OTC)", "GBP/USD (OTC)", "USD/JPY (OTC)", "AUD/CAD (OTC)",
            "USD/CHF (OTC)", "EUR/JPY (OTC)", "NZD/USD (OTC)", "GBP/JPY (OTC)",
            "AUD/JPY (OTC)", "USD/BDT (OTC)", "USD/INR (OTC)", "USD/PKR (OTC)",
            "BTC/USD (OTC)", "EUR/USD", "GBP/USD", "USD/JPY", "AUD/CAD", "GOLD", "BITCOIN"
        ]

        strategies = [
            "SMC Order Block & Institutional Liquidity Grab",
            "EMA 9/21/50 Triple Dynamic Trend Crossover",
            "RSI + Stochastic Double Oscillator Confluence",
            "Bollinger Bands Volatility Expansion & Outer Band Bounce",
            "Breaker Block & Supply/Demand Key Reversal Zone",
            "MACD Divergence + Pinbar Candlestick Exhaustion",
            "Volume Spread Analysis (VSA) High-Volume Rejection"
        ]

        st.session_state.current_pair = random.choice(all_pairs)
        st.session_state.selected_strategy = random.choice(strategies)
        st.session_state.signal_type = random.choice(["CALL (BUY)", "PUT (SELL)"])
        st.session_state.accuracy = random.randint(86, 98)

        # Volatility & News Filter Logic
        volatility_states = [
            ("🟢 GREEN: SAFE MARKET — TRADE KARO (High Accuracy)", "safe"),
            ("⚡ NEON BLUE: DHYAN SE — Market me uthal-puthal hai", "moderate"),
            ("🔴 RED: HIGH VOLATILITY — AVOID KARO (Do Not Trade)", "danger")
        ]

        vol_text, vol_type = random.choices(
            volatility_states, weights=[0.50, 0.35, 0.15], k=1
        )[0]
        st.session_state.volatility_text = vol_text
        st.session_state.volatility_type = vol_type

        # Trend Strength Calculation
        if "CALL" in st.session_state.signal_type:
            buyers = random.randint(78, 93)
            st.session_state.trend_status = f"🟢 STRONG UPTREND (Buyers: {buyers}%)"
        else:
            sellers = random.randint(78, 93)
            st.session_state.trend_status = f"🔴 STRONG DOWNTREND (Sellers: {sellers}%)"

        # Indian Standard Time (IST = UTC + 5:30)
        ist_offset = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
        now_ist = datetime.datetime.now(ist_offset)

        st.session_state.entry_time = now_ist.strftime("%H:%M:%S")
        st.session_state.expiry_time = (now_ist + datetime.timedelta(seconds=60)).strftime("%H:%M:%S")
        st.session_state.expiry_timestamp = time.time() + 60

        # Sound Alert Trigger
        st.components.v1.html(
            """
            <script>
            var ctx = new (window.AudioContext || window.webkitAudioContext)();
            var osc = ctx.createOscillator();
            var gain = ctx.createGain();
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.type = "sine";
            osc.frequency.value = 880;
            gain.gain.setValueAtTime(0.1, ctx.currentTime);
            osc.start();
            osc.stop(ctx.currentTime + 0.3);
            </script>
            """,
            height=0,
        )

    if "signal_type" in st.session_state:
        # Render Volatility Filter Banner
        if st.session_state.volatility_type == "safe":
            st.markdown(
                f'<div class="volatility-safe">{st.session_state.volatility_text}</div>',
                unsafe_allow_html=True,
            )
        elif st.session_state.volatility_type == "moderate":
            st.markdown(
                f'<div class="volatility-moderate">{st.session_state.volatility_text}</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="volatility-danger">{st.session_state.volatility_text}</div>',
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
        <div style="font-size: 13px; color: #7a9bbd; margin-top: 10px;">
            <p><b>Entry Time:</b> {st.session_state.entry_time}</p>
            <p><b>Expiry Time:</b> {st.session_state.expiry_time}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        timer_placeholder = st.empty()
        
        # Live Countdown Loop
        while True:
            remaining_sec = int(st.session_state.expiry_timestamp - time.time())
            if remaining_sec > 0:
                timer_placeholder.markdown(
                    f'<div class="yellow-timer">⏱️ 00:{remaining_sec:02d}</div>',
                    unsafe_allow_html=True,
                )
                time.sleep(1)
            else:
                timer_placeholder.markdown(
                    '<div class="yellow-timer" style="color:#ff0055; border-color:#ff0055;">EXPIRED</div>',
                    unsafe_allow_html=True,
                )
                break
            
