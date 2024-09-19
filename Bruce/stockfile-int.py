import chess
import chess.engine

# 初始化棋盘
board = chess.Board()

# 设置 Stockfish 引擎路径
engine_path = "path/to/stockfish"  # 替换为你的 Stockfish 引擎路径

# 启动引擎
with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
    # 获取引擎推荐的最佳走法
    result = engine.play(board, chess.engine.Limit(time=2.0))
    best_move = result.move

    # 打印最佳走法
    print(f"引擎推荐的最佳走法: {best_move}")

    # 执行最佳走法
    board.push(best_move)

    # 打印更新后的棋盘
    print(board)
