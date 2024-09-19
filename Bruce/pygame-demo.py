import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Demo")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 定义矩形的初始位置和速度
rect_x, rect_y = 50, 50
rect_speed_x, rect_speed_y = 5, 5

# 主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 更新矩形位置
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # 碰撞检测并反转方向
    if rect_x < 0 or rect_x > WIDTH - 50:
        rect_speed_x = -rect_speed_x
    if rect_y < 0 or rect_y > HEIGHT - 50:
        rect_speed_y = -rect_speed_y

    # 填充背景色
    screen.fill(WHITE)

    # 绘制矩形
    pygame.draw.rect(screen, RED, (rect_x, rect_y, 50, 50))

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(60)
