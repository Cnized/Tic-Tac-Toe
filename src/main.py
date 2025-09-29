import random
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10
        self.player_turn = random.choice(["X","O"])
    
    def show_board(self):
        print("\n")
        print(f" {self.board[1]} | {self.board[2]} | {self.board[3]}")
        print("---+---+---")
        print(f" {self.board[4]} | {self.board[5]} | {self.board[6]}")
        print("---+---+---")
        print(f" {self.board[7]} | {self.board[8]} | {self.board[9]}")
        print("\n")

    def fill_board(self, player, cell):
        self.board[cell] = player
    
    def has_player_won(self, player):
        b = self.board
        return ((b[1] == b[2] == b[3] == player) or
                (b[4] == b[5] == b[6] == player) or
                (b[7] == b[8] == b[9] == player) or
                (b[1] == b[4] == b[7] == player) or
                (b[2] == b[5] == b[8] == player) or
                (b[3] == b[6] == b[9] == player) or
                (b[1] == b[5] == b[9] == player) or
                (b[3] == b[5] == b[7] == player))
    
    def change_turn(self):
        if self.player_turn == "X":
            self.player_turn = "O"
        else:
            self.player_turn = "X"
        return self.player_turn
    
    def is_board_fill(self):
        return ' ' not in self.board[1:]
    
    def start(self):
        while True:
            self.show_board()
            try:
                user_input = int(input(f"Player {self.player_turn}, Enter a number (1-9): "))
                if user_input not in range(1, 10):
                    print("Number out of range. Choose 1-9.")
                    continue
                if self.board[user_input] != ' ':
                    print("Cell already filled. Choose another.")
                    continue
            except ValueError:
                print("Invalid input! Enter a number between 1-9.")
                continue
            
            self.fill_board(self.player_turn, user_input)
                
            if self.is_board_fill():
                    self.show_board()
                    print("It's a draw!")
                    if input("Play again? (\"yes\" to continue): ").lower() == "yes":
                        self.board = [' '] * 10
                        continue
                    else:
                        break
                    
            elif self.has_player_won(self.player_turn):
                self.show_board()
                print(f"{self.player_turn} has won the game!!")
                if input("Play again? (\"yes\" to continue): ").lower() == "yes":
                    self.board = [' '] * 10
                    continue
                else:
                    break
                    
            self.change_turn()
                
if __name__ == "__main__":
    game = TicTacToe()
    game.start()