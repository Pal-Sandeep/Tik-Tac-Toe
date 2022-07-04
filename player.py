import random
class Player:
    def __init__(self,letter):
        self.letter = letter
    
    def get_move(self,game):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self,game):
        square = random.choice(game.available_moves())
        return square


class NoobPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter+'\'s turn. Input move (0-8): ')
            print('\n')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try Again.😞😞")
        return val