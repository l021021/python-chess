import chess

# 创建一个新的棋盘
board = chess.Board()

# 打印初始棋盘状态
print("初始棋盘状态:")
print(board)

# 移动棋子：e2 到 e4
move = chess.Move.from_uci("e2e4")
if move in board.legal_moves:
    board.push(move)

# 打印移动后的棋盘状态
print("\n移动 e2 到 e4 后的棋盘状态:")
print(board)

# 检查某个位置上的棋子
square = chess.E4
piece = board.piece_at(square)
print(f"\n位置 e4 上的棋子: {piece}")

# 检查是否为合法移动
move = chess.Move.from_uci("e7e5")
print(f"\n移动 e7 到 e5 是否合法: {move in board.legal_moves}")

# 执行合法移动
if move in board.legal_moves:
    board.push(move)

# 打印移动后的棋盘状态
print("\n移动 e7 到 e5 后的棋盘状态:")
print(board)
