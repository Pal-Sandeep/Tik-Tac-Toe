from player import  NoobPlayer, ComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    # @staticmethod
    # def make_board():
    #     return 

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('|'+'|'.join(row)+'|')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'+'|'.join(row)+'|')
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        # moves[]
        #for(i,spot)in enumerate(self.board):
        #    #  ['X','X','O']→[(0,'X'),(1,'X'),(2,'O')]
        #    if spot == ' ':
        #        moves.append(i)
        #return moves
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self,square,letter):
        #ch3ching the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all(spot == letter for spot in row):
            return True
        #cheking the coloumn
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for  i in range(3)]
        if all(spot == letter for spot in column):
            return True
        #checking the diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False



def play(game,player_x,player_o,print_game=True):
    if print_game:
        game.print_board_nums()
    
    letter = 'X' #starting letter

    while game.empty_squares():
        #get the move from the appropriate user
        if letter == 'O':
            square = player_o.get_move(game)
        else:
            square = player_x.get_move(game)
        
        #function for making a move
        if game.make_move(square, letter):
            if print_game:
                print(letter+ f' makes a move to square: {square}\n')
                game.print_board()
                print("")

            if game.current_winner:
                if print_game:
                    print('✌🥳✌🥳 '+letter+' wins!✌🥳✌🥳')
                return letter

            # after the move changing the letter
            letter = 'O' if letter == "X" else 'X'  #swictching the player
    
        time.sleep(1.3)

    if print_game:
        print('🤞🤞It\'s a tie!🤞🤞')

if __name__ == '__main__':
    player_x = NoobPlayer('X')
    player_o = ComputerPlayer('O')
    ttt = TicTacToe()
    play(ttt, player_x, player_o, print_game = True)