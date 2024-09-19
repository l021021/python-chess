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
    'bP': pygame.image.load('images/bP.png'),
    'bR': pygame.image.load('images/bR.png'),
    'bN': pygame.image.load('images/bN.png'),
    'bB': pygame.image.load('images/bB.png'),
    'bQ': pygame.image.load('images/bQ.png'),
    'bK': pygame.image.load('images/bK.png'),
    'wP': pygame.image.load('images/wP.png'),
    'wR': pygame.image.load('images/wR.png'),
    'wN': pygame.image.load('images/wN.png'),
    'wB': pygame.image.load('images/wB.png'),
    'wQ': pygame.image.load('images/wQ.png'),
    'wK': pygame.image.load('images/wK.png'),
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

# 检查合法移动（示例）


def is_valid_move(board, start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]
    target_piece = board[end_row][end_col]

    # 示例：仅允许直线移动（车的移动）
    if piece in ['wR', 'bR']:
        if start_row == end_row or start_col == end_col:
            # 检查路径是否被阻挡
            if start_row == end_row:
                step = 1 if start_col < end_col else -1
                for col in range(start_col + step, end_col, step):
                    if board[start_row][col] != ' ':
                        return False
            else:
                step = 1 if start_row < end_row else -1
                for row in range(start_row + step, end_row, step):
                    if board[row][start_col] != ' ':
                        return False
            # 检查目标位置是否为空或包含敌方棋子
            if target_piece == ' ' or (piece[0] != target_piece[0]):
                return True
    return True

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

    selected_piece = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // 50
                row = pos[1] // 50
                print(f"Mouse clicked at: {pos}, Board position: ({row}, {col})")  # 调试信息

                if selected_piece:
                    # 尝试移动棋子
                    if is_valid_move(board, selected_piece, (row, col)):
                        print('Legal move!')
                        board[row][col] = board[selected_piece[0]][selected_piece[1]]
                        board[selected_piece[0]][selected_piece[1]] = ' '
                    selected_piece = None  # 取消选择
                else:
                    # 选择棋子
                    if board[row][col] != ' ':
                        selected_piece = (row, col)
                        print(f"Selected piece at: {selected_piece}")  # 调试信息

        screen.fill(BACKGROUND_COLOR)
        draw_board()
        draw_pieces(board)
        pygame.display.flip()


if __name__ == "__main__":
    main()
