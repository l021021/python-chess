import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口和颜色
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (255, 255, 255)
LIGHT_COLOR = (238, 238, 210)
DARK_COLOR = (118, 150, 86)

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Board")

# 加载棋子图像
pieces = {
    'bR': pygame.image.load('images/bR.png'),
    'bN': pygame.image.load('images/bN.png'),
    'bB': pygame.image.load('images/bB.png'),
    'bQ': pygame.image.load('images/bQ.png'),
    'bK': pygame.image.load('images/bK.png'),
    'bP': pygame.image.load('images/bP.png'),
    'wR': pygame.image.load('images/wR.png'),
    'wN': pygame.image.load('images/wN.png'),
    'wB': pygame.image.load('images/wB.png'),
    'wQ': pygame.image.load('images/wQ.png'),
    'wK': pygame.image.load('images/wK.png'),
    'wP': pygame.image.load('images/wP.png'),
}

# 创建棋盘


def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, (col * 50, row * 50, 50, 50))

# 绘制棋子


def draw_pieces(board):
    for row in range(8):
        for col in range(8):
            piece = board[row][col]
            if piece != ' ':
                screen.blit(pieces[piece], (col * 50, row * 50))

# 主循环


def main():
    board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
    ]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND_COLOR)
        draw_board()
        draw_pieces(board)
        pygame.display.flip()


if __name__ == "__main__":
    main()
