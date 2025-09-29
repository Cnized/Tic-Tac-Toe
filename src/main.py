import random
class TicTacToe:
    def __init__(self):
        self.board =[' '] * 10
        #self.player_turn = random.choice(["X","O"])
        self.player_turn = "X"
    
    def show_board(self):
        print("\n")
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3] )
        print("-----")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6] )
        print("-----")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9] )
        print("\n")
        
    def fill_board(self, player, cell):
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
                user_input = int(input("Enter a numebr between 1-9: "))
            except ValueError:
                print("Enter A Number!! (between 1-9)")
                continue
            
            if self.board[user_input] and user_input in range(1,10):
                self.show_board()
                self.fill_board(self.player_turn, user_input)
                
                if self.is_board_fill() and self.has_player_won is False:
                    self.show_board()
                    print("Draw!!")
                    break
                
                elif self.has_player_won(self.player_turn):
                    self.show_board()
                    print(f"{self.player_turn} has won the game!!")
                    break
                
                self.change_turn()
                
            else:
                print("Invalid Cell Number, Try again!")
                
