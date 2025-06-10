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

def game_loop
