import streamlit as st

# ---------- Sidebar CSS ----------
st.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-right: 2px solid #ccc;
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        color: #203a43;
    }
    .tip-box {
        background: #f8f9fa;
        padding: 12px;
        border-radius: 10px;
        font-size: 16px;
        color: #222;
        margin-bottom: 12px;
        border-left: 5px solid #2c5364;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar Content ----------

st.sidebar.markdown("### 📌 Quick Tips to Stay Safe")

tips = [
    "🔹 **Never click unknown links** in messages.",
    "🔹 **Avoid sharing OTP or passwords** with anyone.",
    "🔹 Check **email sender address** carefully.",
    "🔹 **Be cautious of 'too good to be true' offers.**",
    "🔹 Use **strong and unique passwords.**"
]

for tip in tips:
    st.sidebar.markdown(f"<div class='tip-box'>{tip}</div>", unsafe_allow_html=True)

st.sidebar.write("---")

st.sidebar.caption("💡 Stay alert. Stay safe. Spam Shield has your back! 🔐")


st.set_page_config(page_title="Spam Shield", page_icon="🛡️", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    /* Add Background Image with Transparency */
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                    url("https://media.istockphoto.com/id/1094130172/vector/isometric-digital-padlock-abstract-technology-background-vector-illustration.jpg?s=612x612&w=0&k=20&c=DOWwK6yDOh35hV25CZt0lr44pxQ8ng9sntB-NTM7JEY=") no-repeat center center fixed;
        background-size: cover;
    }

    .center-heading {
        text-align: center;
        font-size: 55px;
        font-weight: bold;
        color: black; /* Black heading */
        margin-bottom: 10px;
    }
    .subheading {
        text-align: center;
        font-size: 20px;
        color: black; /* Black text */
        margin-bottom: 40px;
    }
    .feature-box {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        color: black; /* Black text */
    }
    .feature-title {
        font-size: 20px;
        font-weight: bold;
        margin-top: 10px;
        color: black; /* Black title */
    }

        /* 🔵 Navy Bluish Gradient Button */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 12px 28px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(0, 255, 255, 0.4); /* Slight cyan glow */
    }

    </style>
""", unsafe_allow_html=True)

# ---------- Centered Heading ----------
st.markdown("<h1 class='center-heading'>🛡️ Spam Shield</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheading'>Your friendly spam detector app!</p>", unsafe_allow_html=True)

# ---------- Hero Section ----------
col1, col2 = st.columns([1.5, 1])

# ✅ Left Content
with col1:
    st.markdown(
        """
        <div style="text-align:center;">
            <h4 style="font-size:26px; font-weight:bold; color:black;">👋 Welcome to Spam Shield!</h4>
            <p style="font-size:20px; color:black; line-height:1.8; margin-top:10px;">
            🚀 Say goodbye to unwanted spam, scams, and phishing messages.<br>
            🛡️ Our smart AI instantly checks your messages and tells you if they are <b>safe or spam</b>.<br>
            🔒 No sign-up, no data storage – just a simple, secure, and fun way to protect your inbox.<br>
            🎉 <b>Start detecting spam now and keep your messages safe!</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ✅ Right Content (Image + Button Below It)
with col2:
    st.image("https://www.galaxkey.com/wp-content/uploads/2018/06/spam-scaled-1.jpg", width=320)
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)

    # Centered Button
    b1, b2, b3 = st.columns([0.5, 4, 0.5])
    with b2:
        if st.button("🚀 Start Detecting Spam", key="start"):
            st.switch_page("pages/1_Spam_Detector.py")

st.write("---")

# ---------- Features Section ----------
st.subheader("✨ Why Use Spam Shield?")
col3, col4, col5 = st.columns(3)

with col3:
    st.markdown('<div class="feature-box">⚡<div class="feature-title">Fast & Easy</div><p>Detect spam instantly in one click.</p></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="feature-box">🔒<div class="feature-title">Safe & Secure</div><p>Your messages are never stored.</p></div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="feature-box">🎉<div class="feature-title">Fun & Friendly</div><p>Interactive results with emojis!</p></div>', unsafe_allow_html=True)

st.write("---")

# ---------- FAQ Section ----------
st.subheader("❓ Frequently Asked Questions")

with st.expander("🔹 What is Spam Shield?"):
    st.write("Spam Shield is a simple app to detect if a message is spam or safe. It uses machine learning behind the scenes, but is designed for everyone!")

with st.expander("🔹 Do I need technical skills?"):
    st.write("No! Just type your message, click a button, and see the result instantly.")

with st.expander("🔹 Is my data safe?"):
    st.write("Yes! The app processes your message only for detection and does not store any data.")

st.write("---")

# ---------- Footer ----------
st.markdown("<p style='text-align:center; color:black;'>Made with ❤️ using Python & Streamlit</p>", unsafe_allow_html=True)
