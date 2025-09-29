import random
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10
        self.player_turn = self.random_player_turn()
    
    def random_player_turn(self):
        return random.choice(["X","O"])
    
    def show_board(self):
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3] + "|" )
        print("-------")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6] + "|" )            
        print("-------")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9] + "|" )
        print("\n")

    def fill_board(self,cell, player):
        self.board[cell] = player
        
    def has_player_won(self, player):
        return ((self.board[7] == player and self.board[8] == player and self.board[9] == player) or 
                (self.board[4] == player and self.board[5] == player and self.board[6] == player) or 
                (self.board[1] == player and self.board[2] == player and self.board[3] == player) or 
                (self.board[7] == player and self.board[4] == player and self.board[1] == player) or 
                (self.board[8] == player and self.board[5] == player and self.board[2] == player) or 
                (self.board[9] == player and self.board[6] == player and self.board[3] == player) or     
                (self.board[7] == player and self.board[5] == player and self.board[3] == player) or 
                (self.board[9] == player and self.board[5] == player and self.board[1] == player))
        
    def is_board_fill(self):
        return ' ' not in self.board[1:]
    
    def swap_turn(self):
        self.player_turn = "X" if self.player_turn == "O" else "O"
        return self.player_turn
    
    def start(self):
        while True:
            self.show_board()
            try:
                cell = int(input((f"Enter your choice {self.player_turn} (between 1 to 9) : ")))
            except ValueError:
                print("Enter A *Number* (between 1 to 9)")
                
            if self.board[cell] == ' ' and cell in range(1,10):
                self.fill_board(cell, self.player_turn)
                
                if self.is_board_fill() and self.has_player_won() is False:
                    self.show_board()
                    print("Draw!!")
                    break
                elif self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f"{self.player_turn} has won!")
                    break
                self.swap_turn()
            else:
                print("Invalid Cell number, Try again.")


if __name__ == "__main__":
    game = TicTacToe()
    game.start()