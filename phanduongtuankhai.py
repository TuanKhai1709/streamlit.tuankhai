import streamlit as st

# Tiêu đề
st.title("🔐 Đăng nhập hệ thống")

# Tạo form đăng nhập
with st.form("login_form"):
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    submit = st.form_submit_button("Đăng nhập")

# Xử lý khi người dùng nhấn nút đăng nhập
if submit:
    if username == "admin" and password == "123456":
        st.success("✅ Đăng nhập thành công!")
    else:
        st.error("❌ Sai tên đăng nhập hoặc mật khẩu.")
