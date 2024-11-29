import tkinter as tk
import chess
import chess.engine
import sys

STOCKFISH_PATH = "D:\\stockfish\\stockfish-windows-x86-64-avx2.exe"


class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
        self.selected_square = None
        self.move_history = []
        self.last_move = None
        self.hint_move = None
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame, width=400, height=400)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_square_click)

        self.move_list = tk.Listbox(self.root, width=20, height=20)
        self.move_list.pack(side=tk.RIGHT, padx=10, pady=10)

        self.hint_button = tk.Button(self.root, text="提示", command=self.show_hint)
        self.hint_button.pack(side=tk.BOTTOM, pady=10)

        self.draw_board()
        self.draw_pieces()

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                x1 = col * 50
                y1 = row * 50
                x2 = x1 + 50
                y2 = y1 + 50
                color = "white" if (row + col) % 2 == 0 else "gray"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_pieces(self):
        self.canvas.delete("pieces")
        piece_images = {
            "P": "♙", "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔",
            "p": "♟", "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚"
        }
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                x = (square % 8) * 50 + 25
                y = (7 - square // 8) * 50 + 25
                color = "black"
                if self.last_move and square in (self.last_move.from_square, self.last_move.to_square):
                    color = "red"
                elif self.hint_move and square in (self.hint_move.from_square, self.hint_move.to_square):
                    color = "green"
                self.canvas.create_text(x, y, text=piece_images[piece.symbol()], tags="pieces", font=("Arial", 24), fill=color)

    def on_square_click(self, event):
        col = event.x // 50
        row = 7 - (event.y // 50)
        square = chess.square(col, row)

        if self.selected_square is None:
            if self.board.piece_at(square) and self.board.piece_at(square).color == self.board.turn:
                self.selected_square = square
                print(f"Selected {chess.square_name(square)}")
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.record_move(move, "Player")
                self.board.push(move)
                self.last_move = move
                self.hint_move = None
                self.draw_pieces()
                print(f"Moved to {chess.square_name(square)}")
                self.selected_square = None
                self.after_user_move()
            else:
                print("Illegal move")
                self.selected_square = None

    def after_user_move(self):
        if self.board.is_checkmate():
            print("Checkmate! Game over.")
            self.canvas.create_text(200, 200, text="Checkmate!", font=("Arial", 32), fill="red", tags="game_over")
            return
        if not self.board.is_game_over():
            result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
            self.record_move(result.move, "Stockfish")
            self.board.push(result.move)
            self.last_move = result.move
            self.hint_move = None
            self.draw_pieces()
            print(f"Stockfish moved to {result.move}")
            if self.board.is_checkmate():
                print("Checkmate! You lose.")
                self.canvas.create_text(200, 200, text="Checkmate! You lose.", font=("Arial", 32), fill="red", tags="game_over")

    def record_move(self, move, player):
        try:
            move_san = self.board.san(move)
        except ValueError:
            move_san = move.uci()
        move_text = f"{player}: {move_san}"
        self.move_history.append(move_text)
        self.move_list.insert(tk.END, move_text)
        self.move_list.see(tk.END)

    def show_hint(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=1.0))
        self.hint_move = result.move
        self.draw_pieces()
        print(f"Hint: {self.hint_move}")

    def run(self):
        self.check_window()
        self.root.mainloop()

    def check_window(self):
        if not self.root.winfo_exists():
            print("Window closed, exiting program.")
            self.engine.quit()
            sys.exit()
        else:
            self.root.after(100, self.check_window)


def main():
    root = tk.Tk()
    gui = ChessGUI(root)
    gui.run()


if __name__ == "__main__":
    main()
