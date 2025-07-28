import streamlit as st
import joblib
import docx2txt
import fitz  # PyMuPDF for PDF

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

# Load model and vectorizer
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

st.set_page_config(page_title="Spam Detector", page_icon="✍️", layout="wide")

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
        font-size: 50px;
        font-weight: bold;
        color: black;
        margin-bottom: 10px;
    }
    .subheading {
        text-align: center;
        font-size: 22px;
        font-weight: 500;
        color: black;
        margin-bottom: 30px;
    }
    textarea {
        font-size: 18px !important;
    }
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
        box-shadow: 0px 4px 15px rgba(0, 255, 255, 0.4);
    }
            
    </style>
""", unsafe_allow_html=True)

# ---------- Heading ----------
st.markdown("<h1 class='center-heading'>🛡️ Spam Shield</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<p class='subheading'>📢 <b style='font-size:24px;'>Paste any message OR upload a file (TXT, PDF, DOCX) and let Spam Shield decide if it's safe or spam!</b></p>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)
# ---------- Layout Container with Padding ----------
st.markdown("<div style='padding-left:60px; padding-top:20px;'>", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])  # Adjusted widths

# ✅ Column 1 → File Upload + Button
with col1:
    st.markdown("<h3 style='color:black;'>📂 Upload a File</h3>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx"])
    uploaded_text = ""

    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            uploaded_text = uploaded_file.read().decode("utf-8")
        elif uploaded_file.type == "application/pdf":
            pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            for page in pdf_doc:
                uploaded_text += page.get_text()
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            uploaded_text = docx2txt.process(uploaded_file)

        st.markdown("<p style='font-size:18px; color:black;'>✅ File uploaded successfully!</p>", unsafe_allow_html=True)


     # ✅ Center the button in column 1
    btn1, btn2, btn3 = st.columns([1, 2, 1])
    with btn2:
        if st.button("🔍 Check Now"):
            final_msg = uploaded_text or st.session_state.get("typed_msg", "")
            if final_msg.strip() == "":
                st.markdown(
                    "<p style='text-align:center; color:red;'>⚠️ Please enter or upload a message first.</p>",
                    unsafe_allow_html=True,
                )
            else:
                msg_tfidf = vectorizer.transform([final_msg.lower()])
                prediction = model.predict(msg_tfidf)[0]
                st.session_state["result"] = prediction
                st.session_state["message"] = final_msg
                st.switch_page("pages/2_Result.py")

# ✅ Column 2 → Text Input
with col2:
    st.markdown("<h3 style='color:black;'>✏️ Type or Paste Your Message</h3>", unsafe_allow_html=True)
    typed_msg = st.text_area("📩 Your Message", value=uploaded_text, height=200)
    st.session_state["typed_msg"] = typed_msg

st.markdown("</div>", unsafe_allow_html=True)  # Close padding div
