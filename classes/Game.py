
class Game:

    def __init__(self, id) -> None:
        self.id = id
        self.player1_moved = False
        self.player2_moved = False
        self.ready = False
        self.player1_score = 0
        self.player2_score = 0
        self.player1_move = None
        self.player2_move = None

    def both_moved(self):
        return self.player1_moved and self.player2_moved

    def play(self, player, move):
        if player == 1:
            self.player1_move = move
        else:
            self.player2_move = move

    def getWinner(self):
        winner = None

        if self.player1_move == 'R' and self.player2_move == 'S':
            winner = 1
        elif self.player1_move == 'R' and self.player2_move == 'P':
            winner = 2
        elif self.player1_move == 'S' and self.player2_move == 'R':
            winner = 2
        elif self.player1_move == 'S' and self.player2_move == 'P':
            winner = 1    
        elif self.player1_move == 'P' and self.player2_move == 'R':
            winner = 1
        elif self.player1_move == 'P' and  self.player2_move == 'S':
            winner = 2    

        return winner