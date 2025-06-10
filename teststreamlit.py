import streamlit as st
import pygame
import math

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ trò chơi
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Angry Birds Mini")

# Màu sắc
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Lực bắn
force = 10
angle = 45

# Vị trí ban đầu của vật thể
x, y = 100, HEIGHT - 50
velocity_x = force * math.cos(math.radians(angle))
velocity_y = -force * math.sin(math.radians(angle))

def game_loop():
    global x, y, velocity_x, velocity_y
    running = True
    while running:
        screen.fill(WHITE)

        # Vẽ vật thể (chim)
        pygame.draw.circle(screen, RED, (int(x), int(y)), 20)

        # Cập nhật vị trí
        x += velocity_x
        y += velocity_y
        velocity_y += 0.5  # Giả lập trọng lực

        # Kiểm tra va chạm với mặt đất
        if y >= HEIGHT - 20:
            y = HEIGHT - 20
            velocity_y = 0

        # Kiểm tra sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

def streamlit_ui():
    st.title("Angry Birds Mini")
    st.write("Điều chỉnh lực và góc bắn:")
    
    global force, angle
    force = st.slider("Lực bắn", 5, 20, 10)
    angle = st.slider("Góc bắn", 0, 90, 45)

    if st.button("Bắt đầu trò chơi"):
        pygame.quit()  # Đảm bảo không có phiên bản Pygame nào chạy trước đó
        pygame.init()
        game_loop()

# Chạy ứng dụng Streamlit
streamlit_ui()
