import streamlit as st

# Cấu hình page
st.set_page_config(page_title="Login", layout="centered")

# CSS để làm đẹp giao diện
st.markdown("""
    <style>
    .login-box {
        background-color: white;
        padding: 40px 30px;
        border-radius: 15px;
        width: 350px;
        margin: 0 auto;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    .login-title {
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .login-button {
        background: linear-gradient(to right, #4a00e0, #8e2de2);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px;
        width: 100%;
        font-size: 16px;
        margin-top: 10px;
    }
    .signup-text {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
    }
    .signup-text a {
        color: #4a00e0;
        text-decoration: none;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# HTML layout
st.markdown('<div class="login-box">', unsafe_allow_html=True)

st.markdown('<div class="login-title">Login</div>', unsafe_allow_html=True)

# Form nhập username và password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Nút đăng nhập
if st.button("Login", key="login_btn"):
    if username == "admin" and password == "123456":
        st.success("Đăng nhập thành công!")
    else:
        st.error("Sai tên đăng nhập hoặc mật khẩu!")

# Dòng chữ đăng ký
st.markdown("""
    <div class="signup-text">
        Don't have account? <a href="#">Sign up</a>
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
