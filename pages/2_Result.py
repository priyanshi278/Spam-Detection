import streamlit as st
import random  # For dummy spam probability (replace with model if available)

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

st.set_page_config(page_title="Spam Shield - Result", page_icon="🛡️", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(255, 255, 255, 0.7), rgba(255, 255, 255, 0.7)),
                    url("https://media.istockphoto.com/id/1094130172/vector/isometric-digital-padlock-abstract-technology-background-vector-illustration.jpg?s=612x612&w=0&k=20&c=DOWwK6yDOh35hV25CZt0lr44pxQ8ng9sntB-NTM7JEY=") no-repeat center center fixed;
        background-size: cover;
    }
    .center-heading {
        text-align: center;
        font-size: 55px;
        font-weight: bold;
        color: black;
        margin-bottom: 20px;
    }
    .result-text {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-top: 15px;
    }
    .score-box {
        background: rgba(0,0,0,0.08);
        padding: 16px;
        border-radius: 12px;
        font-size: 28px;
        text-align: center;
        margin: 20px auto;
        width: 350px;
        font-weight: bold;
    }
    .rating-text {
        text-align: center;
        font-size: 22px;
        margin-top: 15px;
        font-weight: 500;
    }
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: white;
        font-size: 22px;
        font-weight: bold;
        padding: 14px 30px;
        border-radius: 12px;
        border: none;
        transition: 0.3s;
        display: block;
        margin: 0 auto;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.05);
        box-shadow: 0px 4px 15px rgba(0, 255, 255, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Heading ----------
st.markdown("<h1 class='center-heading'>🛡️ Spam Shield</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

if "result" not in st.session_state:
    st.markdown("<p style='text-align:center; font-size:22px;'>⚠️ No message checked yet. Please go back and check a message first.</p>", unsafe_allow_html=True)

else:
    result = st.session_state["result"]


    # Create two columns
col3,col1, col2,col4 = st.columns([0.5,1.5,1.8,0.3])  # col2 wider



with col1:
    if result == "spam":
        st.markdown("<div style='margin-top: 50px; text-align:center;'>", unsafe_allow_html=True)
        st.image(
            "https://camo.githubusercontent.com/3e4ba60aaf08d8e8b8b91661ac3c263e3b0bb8ded371128dc3fe9b84b5464e42/68747470733a2f2f6d656469612e74656e6f722e636f6d2f726550446644574f33586f41414141642f6861636b696e672e676966",
            width=350
            #https://camo.githubusercontent.com/3e4ba60aaf08d8e8b8b91661ac3c263e3b0bb8ded371128dc3fe9b84b5464e42/68747470733a2f2f6d656469612e74656e6f722e636f6d2f726550446644574f33586f41414141642f6861636b696e672e676966
            #https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUyaWFrM25naDcycWx1dmtpNWQ2cjI1bnJjYXgzbG8zbmc4djV2N2tpYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hun4DFmfnDId3lid5b/source.gif
        )
        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown("<div style='margin-top: 50px; text-align:center;'>", unsafe_allow_html=True)
        st.image("https://media.tenor.com/lxsLq2IcHhgAAAAM/spongebob-its-no-trouble.gif", width=350)
        st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3 style='color:black;text-align: center;'>📢 Spam Detection Result</h3>", unsafe_allow_html=True)
    if result == "spam":
        st.markdown(f"<div class='score-box'> <span style='color:red;'>🚨 This message seems <b>SPAM</b> ❌</span></div>", unsafe_allow_html=True)
        st.markdown("<p class='result-text' style='color:red;'>Suspicious content detected. Do NOT share personal info!</p>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='score-box'><span style='color:green;'>🟢 This message looks <b>SAFE</b> </span></div>", unsafe_allow_html=True)
        st.markdown("<p class='result-text' style='color:green;'>Looks safe - feel free to reply or take action</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✍️ Check Another Message"):
        st.switch_page("pages/1_Spam_Detector.py")

# ---------- Separator + Rating ----------
st.markdown("---")
st.markdown("<p class='rating-text'>⭐ Was this prediction helpful? Give us a rating below!</p>", unsafe_allow_html=True)

rating = st.slider("Rate Spam Shield (1 = Poor, 5 = Excellent)", 1, 5, 3)

if st.button("✅ Submit Rating"):
    st.markdown(
        f"<p style='text-align:center; font-size:20px;'>👍 Thank you for rating us <b>{rating} ⭐</b>!</p>",
        unsafe_allow_html=True
    )
