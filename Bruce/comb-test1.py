import pygame
import chess
import chess.engine
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口大小和标题
WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess with Stockfish")

# 定义颜色
WHITE = (255, 255, 255)
LIGHT_COLOR = (238, 238, 210)
DARK_COLOR = (118, 150, 86)
HIGHLIGHT_COLOR = (0, 255, 0)

# 加载棋子图像
pieces = {
    'P': pygame.image.load('images/wP.png'),
    'R': pygame.image.load('images/wR.png'),
    'N': pygame.image.load('images/wN.png'),
    'B': pygame.image.load('images/wB.png'),
    'Q': pygame.image.load('images/wQ.png'),
    'K': pygame.image.load('images/wK.png'),
    'p': pygame.image.load('images/bP.png'),
    'r': pygame.image.load('images/bR.png'),
    'n': pygame.image.load('images/bN.png'),
    'b': pygame.image.load('images/bB.png'),
    'q': pygame.image.load('images/bQ.png'),
    'k': pygame.image.load('images/bK.png'),
}

# 初始化棋盘
board = chess.Board()

# 设置 Stockfish 引擎路径
engine_path = "D:\\stockfish\\stockfish-windows-x86-64-avx2.exe"  # 替换为你的 Stockfish 引擎路径

# 启动引擎
engine = chess.engine.SimpleEngine.popen_uci(engine_path)

# 创建棋盘


def draw_board():
    for row in range(8):
        for col in range(8):
            color = LIGHT_COLOR if (row + col) % 2 == 0 else DARK_COLOR
            pygame.draw.rect(screen, color, (col * 50, (7 - row) * 50, 50, 50))

# 绘制棋子


def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            piece_image = pieces[piece.symbol()]
            row, col = divmod(square, 8)
            screen.blit(piece_image, (col * 50, (7 - row) * 50))

# 主循环


def main():
    selected_square = None
    last_move = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                engine.quit()
                pygame.quit()
                sys.exit()
            screen.fill(WHITE)
            draw_board()

            # 提示白方下棋并显示引擎建议
            if board.turn == chess.WHITE and selected_square is None:
                print("白方请下棋...")
                # 获取引擎建议
                result = engine.play(board, chess.engine.Limit(time=2.0))
                suggested_move = result.move
                print(f"引擎建议: {suggested_move.uci()}")

            if event.type == pygame.MOUSEBUTTONDOWN:
                # 按下鼠标则为选中棋子
                pos = pygame.mouse.get_pos()
                col = pos[0] // 50
                row = 7 - (pos[1] // 50)
                square = chess.square(col, row)
                # print(square)

                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                        # print(square)
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        last_move = move
                        # 打印走法
                        print(move.uci())
                        # 刷新棋盘
                        selected_square = None

                        # 检查是否将死
                        if board.is_checkmate():
                            print("白方胜利！")
                            # 等待1秒然后退出
                            pygame.time.wait(1000)
                            engine.quit()
                            pygame.quit()
                            sys.exit()

                        # 让 Stockfish 下棋
                        print('thinking...')
                        result = engine.play(board, chess.engine.Limit(time=2.0))
                        board.push(result.move)
                        last_move = result.move
                        # 打印它的uci走法
                        print(result.move.uci())

                        # 检查是否将死
                        if board.is_checkmate():
                            print("黑方胜利！")
                            pygame.time.wait(1000)  # 等待1秒
                            engine.quit()
                            pygame.quit()
                            sys.exit()
                    else:
                        selected_square = None

        screen.fill(WHITE)
        draw_board()

        # 高亮显示最近移动的棋子
        if last_move:
            row, col = divmod(last_move.to_square, 8)
            pygame.draw.rect(screen, HIGHLIGHT_COLOR, (col * 50, (7 - row) * 50, 50, 50), 4)

        draw_pieces()
        pygame.display.flip()


if __name__ == "__main__":
    main()
