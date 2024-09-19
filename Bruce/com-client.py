import pygame
import sys
import chess  # 导入 python-chess
import chess.svg  # 导入 SVG 处理（可选）

# 初始化 Pygame
pygame.init()

# 设置窗口和颜色
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (255, 255, 255)
LIGHT_COLOR = (238, 238, 210)
DARK_COLOR = (118, 150, 86)

# 创建窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess GUI")

# 加载棋子图像
pieces = {
    'p': pygame.image.load('images/bP.png'),
    'r': pygame.image.load('images/bR.png'),
    'n': pygame.image.load('images/bN.png'),
    'b': pygame.image.load('images/bB.png'),
    'q': pygame.image.load('images/bQ.png'),
    'k': pygame.image.load('images/bK.png'),
    'P': pygame.image.load('images/wP.png'),
    'R': pygame.image.load('images/wR.png'),
    'N': pygame.image.load('images/wN.png'),
    'B': pygame.image.load('images/wB.png'),
    'Q': pygame.image.load('images/wQ.png'),
    'K': pygame.image.load('images/wK.png'),
}

# 绘制棋盘


def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, (col * 50, row * 50, 50, 50))

# 绘制棋子


def draw_pieces(board):
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(i * 8 + j)
            if piece:
                piece_symbol = piece.symbol()
                screen.blit(pieces[piece_symbol], (j * 50, i * 50))

# 主循环


def main():
    board = chess.Board()  # 创建棋盘实例
    #Q:explain chess.Board()?
    #A:chess.Board() creates a new chess board with the standard starting position. It is the starting point for all chess games.
    #Q:What is the structure of the chess.Board()?
    #A:chess.Board() is a 1D list of 64 elements, each element representing a square on the chess board. The elements are in row-major order, starting from the top-left corner of the board.
    #Q: example of chess.Board()? demo code?
    #A: board = chess.Board()
    #Q:What is the output of the demo code?
    #说明一下Board的数据结构
    
    selected_square = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // 50
                row = pos[1] // 50

                # 检查是否点击在棋盘范围内
                if 0 <= row < 8 and 0 <= col < 8:
                    square = chess.square(col, 7 - row)  # 转换坐标

                    if selected_square is None:
                        # 选择棋子
                        if board.piece_at(square):
                            selected_square = square
                    else:
                        # 尝试移动棋子
                        if board.is_legal(chess.Move(selected_square, square)):
                            board.push(chess.Move(selected_square, square))  # 执行移动
                        selected_square = None  # 取消选择

        screen.fill(BACKGROUND_COLOR)
        draw_board()
        draw_pieces(board)
        pygame.display.flip()


if __name__ == "__main__":
    main()
