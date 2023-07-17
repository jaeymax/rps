
class Game:

    def __init__(self, id) -> None:
        self.id = id
        self.player1_moved = False
        self.player2_moved = False
        self.player1_ready = True
        self.player2_ready = False
        self.player1_score = 0
        self.player2_score = 0
        self.player1_move = None
        self.player2_move = None

    def both_moved(self):
        return self.player1_moved and self.player2_moved


    def ready(self):
        return self.player1_ready and self.player2_ready

    def play(self, player, move):
        if player == 1:
            self.player1_move = move
        else:
            self.player2_move = move

    def reset_moves(self):
        self.player1_moved = False
        self.player2_moved = False
        self.player1_move = None
        self.player2_move = None

    def reset_game(self):
        self.player1_score = 0
        self.player2_score = 0
        self.reset_moves()    

    def getWinner(self):
        winner = None

        if self.player1_move == 'ROCK' and self.player2_move == 'SCISSOR':
            winner = 1
        elif self.player1_move == 'ROCK' and self.player2_move == 'PAPER':
            winner = 2
        elif self.player1_move == 'SCISSOR' and self.player2_move == 'ROCK':
            winner = 2
        elif self.player1_move == 'SCISSOR' and self.player2_move == 'PAPER':
            winner = 1    
        elif self.player1_move == 'PAPER' and self.player2_move == 'ROCK':
            winner = 1
        elif self.player1_move == 'PAPER' and  self.player2_move == 'SCISSOR':
            winner = 2    

        return winner