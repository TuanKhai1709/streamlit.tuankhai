import streamlit as st
import random

# Các lựa chọn
choices = ["Kéo", "Búa", "Bao"]

def get_winner(player, computer):
    if player == computer:
        return "Hòa!"
    elif (player == "Kéo" and computer == "Bao") or \
         (player == "Búa" and computer == "Kéo") or \
         (player == "Bao" and computer == "Búa"):
        return "Bạn thắng!"
    else:
        return "Bạn thua!"

# Giao diện Streamlit
st.title("🎮 Trò chơi Oẳn Tù Tì 🎮")
st.write("Chọn một trong ba lựa chọn: Kéo, Búa, Bao")

player_choice = st.radio("Lựa chọn của bạn:", choices)

if st.button("Chơi!"):
    computer_choice = random.choice(choices)
    result = get_winner(player_choice, computer_choice)

    st.write(f"🤖 Máy chọn: **{computer_choice}**")
    st.write(f"🏆 Kết quả: **{result}**")

st.write("Hãy thử vận may của bạn và xem ai là người chiến thắng!")
