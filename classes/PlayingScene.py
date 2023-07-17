from .Scene import Scene as Sc
from typing import List
from .Button import Button, RPSBUTTON, NormalButton
from .Constants import Constants
from .Game import Game
from .ClientNetwork import ClientNetwork
from .TextManager import BlinkableText, StaticText
import pygame


class PlayingScene(Sc):
    def __init__(self, width, height, background_image_url):
        super().__init__(width, height, background_image_url)
        self.rock_button:RPSBUTTON = RPSBUTTON(Constants.RPS_BUTTON_SIZE, Constants.ROCK_BUTTON_POSITION, Constants.ROCK_BUTTON_IMAGE,'ROCK', Constants.ROCK_BUTTON_HIGHLIGHTED_COLOR)
        self.scissor_button:RPSBUTTON = RPSBUTTON(Constants.RPS_BUTTON_SIZE, Constants.SCISSOR_BUTTON_POSITION, Constants.SCISSOR_BUTTON_IMAGE, 'SCISSOR', Constants.SCISSOR_BUTTON_HIGHLIGHTED_COLOR)
        self.paper_button:RPSBUTTON = RPSBUTTON(Constants.RPS_BUTTON_SIZE, Constants.PAPER_BUTTON_POSITION, Constants.PAPER_BUTTON_IMAGE, 'PAPER', Constants.PAPER_BUTTON_HIGHLIGHTED_COLOR)
        self.play_text = BlinkableText(Constants.PLAY_TEXT_POSITION, Constants.PLAY_TEXT_COLOR, Constants.PLAY_TEXT_SIZE, Constants.PLAY_TEXT_FONT, Constants.PLAY_TEXT_LABLE)
        self.opponent_waiting_text = BlinkableText(Constants.OPPONENT_WAITING_TEXT_POSITION, Constants.OPPONENT_WAITING_TEXT_COLOR, Constants.OPPONENT_WAITING_TEXT_SIZE, Constants.OPPONENT_MOVE_TEXT_FONT,Constants.OPPONENT_WAITING_TEXT_LABEL)
        self.locked_in_text = StaticText(Constants.LOCKED_IN_TEXT_POSITION,Constants.LOCKED_IN_TEXT_COLOR, Constants.LOCKED_IN_TEXT_SIZE, Constants.LOCKED_IN_TEXT_FONT, Constants.LOCKED_IN_TEXT_LABEL)
        self.move_text = StaticText(Constants.MOVE_TEXT_POSITION,Constants.MOVE_TEXT_COLOR, Constants.MOVE_TEXT_SIZE, Constants.MOVE_TEXT_FONT, '')
        self.opponent_move_text = StaticText(Constants.OPPONENT_MOVE_TEXT_POSITION, Constants.OPPONENT_MOVE_TEXT_COLOR, Constants.OPPONENT_MOVE_TEXT_SIZE, Constants.MOVE_TEXT_FONT, '')
        self.score_text = None
        self.opponent_score_text = None
        self.last_updated_win_text_time = None
        self.win_text_animation_time = 2000
        self.win_or_lose_text = StaticText(Constants.WIN_OR_LOSE_TEXT_POSITION, Constants.TIE_COLOR, Constants.WIN_OR_LOSE_TEXT_SIZE, Constants.WIN_OR_LOST_TEXT_FONT, '')



    def init(self, player, game):
        self.score_text = StaticText(Constants.SCORE_TEXT_POSITION, Constants.SCORE_TEXT_COLOR, Constants.SCORE_TEXT_SIZE, Constants.SCORE_TEXT_FONT, f'YOUR SCORE: {self.get_score(player, game)}')
        self.opponent_score_text = StaticText(Constants.OPPONENT_SCORE_TEXT_POSITION, Constants.OPPONENT_SCORE_TEXT_COLOR, Constants.OPPONENT_SCORE_TEXT_SIZE, Constants.OPPONENT_SCORE_TEXT_FONT, f"OPPONENT: {self.get_opponent_score(player, game)}")
        self.score_text.show = True
        self.opponent_score_text.show = True
    
    def get_score(self, player, game:Game)->int:
        if player == 1:
            return game.player1_score
        return game.player2_score
    
    def get_opponent_score(self, player, game:Game)->int:
        if player == 1:
            return game.player2_score
        return game.player1_score

    def draw(self):
        #self.surface.blit(self.background_image, (0, 0))
        #self.surface.fill((255, 184, 198))
        self.surface.fill((173, 216, 230))
        self.rock_button.draw(self.surface)
        self.scissor_button.draw(self.surface)
        self.paper_button.draw(self.surface)  
        self.score_text.render(self.surface)
        self.opponent_score_text.render(self.surface) 
        self.play_text.render(self.surface)
        self.opponent_waiting_text.render(self.surface)
        self.opponent_move_text.render(self.surface)
        self.locked_in_text.render(self.surface)
        self.move_text.render(self.surface)   
        self.win_or_lose_text.render(self.surface)


    def select_moves(self, player, game):  
        if player == 1:
            if game.player1_moved:
               move:str = game.player1_move
               if move == 'ROCK':
                   self.rock_button.selected = True
               elif move == 'SCISSOR':
                   self.scissor_button.selected = True
               else:
                   self.paper_button.selected = True  
            else:
                if self.rock_button.selected:
                    self.rock_button.selected = False
                elif self.paper_button.selected:
                    self.paper_button.selected = False
                elif self.scissor_button.selected:
                    self.scissor_button.selected = False    
        else:
            if game.player2_moved:
               move:str = game.player2_move
               if move == 'ROCK':
                   self.rock_button.selected = True
               elif move == 'SCISSOR':
                   self.scissor_button.selected = True
               else:
                   self.paper_button.selected = True  
            else:
                if self.rock_button.selected:
                    self.rock_button.selected = False
                elif self.paper_button.selected:
                    self.paper_button.selected = False
                elif self.scissor_button.selected:
                    self.scissor_button.selected = False    

    def update_move_texts(self, player:int, game:Game):
        if player == 1:
            if game.player1_moved:
                #if the current player is player 1 and he has made a move
                #print(f'you chose {game.player1_move}')
                self.move_text =  StaticText(Constants.MOVE_TEXT_POSITION,Constants.MOVE_TEXT_COLOR, Constants.MOVE_TEXT_SIZE, Constants.MOVE_TEXT_FONT, game.player1_move)
                self.move_text.show = True
                self.play_text.show = False
                if game.player2_moved:
                    #if the current player is player 1 and he made and move and player 2 has also made a move
                    self.opponent_move_text = StaticText(Constants.OPPONENT_MOVE_TEXT_POSITION, Constants.OPPONENT_MOVE_TEXT_COLOR, Constants.MOVE_TEXT_SIZE, Constants.MOVE_TEXT_FONT, game.player2_move)
                    self.opponent_move_text.show = True
                    self.locked_in_text.show = False
                    self.opponent_waiting_text.show = False
                else:
                    #if the current player is player 1 and he made a move and player 2 has not move yet
                    self.opponent_waiting_text.show = True
            else:
                #if current player is player 1 and he hasn't made a move
                #print('play!')
                self.play_text.show = True
                self.move_text.show = False

                if game.player2_moved:
                    #if current player is player 1 and he hasn't made a move and player 2 has made a move
                  #  print('opponent locked in')
                    self.locked_in_text.show = True
                    self.opponent_waiting_text.show = False
                else:
                    #if current player is 1 and he hasn't made a move and opponent also hasn't made a move
                 #   print('waiting for opponents move')        
                    self.opponent_waiting_text.show = True
                    self.locked_in_text.show = False
        else:
            if game.player2_moved:
                #if current  player is 2 and he has made a move
                #print(f'you chose {game.player2_move}')
                self.move_text =  StaticText(Constants.MOVE_TEXT_POSITION,Constants.MOVE_TEXT_COLOR, Constants.MOVE_TEXT_SIZE, Constants.MOVE_TEXT_FONT, game.player2_move)
                self.move_text.show = True
                self.play_text.show = False
                if game.player1_moved:
                    #if current player is 2 and he made a move and opponent made a move
                    self.opponent_move_text = StaticText(Constants.OPPONENT_MOVE_TEXT_POSITION, Constants.OPPONENT_MOVE_TEXT_COLOR, Constants.OPPONENT_MOVE_TEXT_SIZE, Constants.OPPONENT_MOVE_TEXT_FONT, game.player1_move)
                    self.opponent_move_text.show = True
                    self.locked_in_text.show = False
                    self.opponent_waiting_text.show = False
                else:
                    #if current player is 2 and  and he made a move and opponent has not moved yet
                    self.opponent_waiting_text.show = True
                    
            else:
                #if current player is 2 and he hasn't made a move
                #print('play!')
                self.play_text.show = True
                self.move_text.show = False
            
                if game.player1_moved:
                    #if current player is 2 and he hasn't made a move and opponent made a move
                  #  print('opponent locked in')
                    self.locked_in_text.show = True
                    self.opponent_waiting_text.show = False
                else:
                    #if current player is 2 and he hasn't made a move and opponent hasn't made a move
                   # print('waiting for opponents move')
                    self.opponent_waiting_text.show = True    
                    self.locked_in_text.show = False    

    def update_scores_text(self, player, game):
        self.score_text = StaticText(Constants.SCORE_TEXT_POSITION, Constants.SCORE_TEXT_COLOR, Constants.SCORE_TEXT_SIZE, Constants.SCORE_TEXT_FONT, f'YOUR SCORE: {self.get_score(player, game)}')
        self.opponent_score_text = StaticText(Constants.OPPONENT_SCORE_TEXT_POSITION, Constants.OPPONENT_SCORE_TEXT_COLOR, Constants.OPPONENT_SCORE_TEXT_SIZE, Constants.OPPONENT_SCORE_TEXT_FONT, f"OPPONENT: {self.get_opponent_score(player, game)}")
        self.score_text.show = True
        self.opponent_score_text.show = True

    def make_move(self, player, game, client_network, mouse_position):
        if self.rock_button.clicked(mouse_position):
            if player == 1:
                if not game.player1_moved:
                    client_network.send('ROCK')
                    
                #print('Rock button was clicked by player 1')
            else:
                if not game.player2_moved:
                    client_network.send('ROCK')
                #print('Rock button was clicked by player 2')
        elif self.scissor_button.clicked(mouse_position):
            if player == 1:
                if not game.player1_moved:
                    client_network.send('SCISSOR')
                #print('Scissor button was clicked by player 1')    
            else:
                if not game.player2_moved:
                    client_network.send('SCISSOR')
                #print('Scissor button was clicked by player 2')
        elif self.paper_button.clicked(mouse_position):
            if player == 1:
                if not game.player1_moved:
                    client_network.send('PAPER')
                #print('Paper button was clicked by player 1')
            else:
                if not game.player2_moved:
                    client_network.send('PAPER')
               # print('Paper button was clicked by player 2')

    def update(self, **kwargs):
        game:Game = kwargs.get('game')
        player = int(kwargs.get('player'))
        client_network:ClientNetwork = kwargs.get('client_network')

        self.move_text.show = False
        self.opponent_move_text.show = False
        self.locked_in_text.show = False
        self.play_text.show = True
        self.opponent_waiting_text.show = True
        
        self.win_or_lose_text.show = False
        self.rock_button.update()
        self.scissor_button.update()
        self.paper_button.update()
        self.play_text.update()
        self.score_text.update()
        self.opponent_score_text.update()
        self.opponent_waiting_text.update()
        self.locked_in_text.update()
        self.move_text.update()
        self.win_or_lose_text.update()
        mouse_position = pygame.mouse.get_pos()

        self.make_move(player, game, client_network, mouse_position)
        self.select_moves(player, game)
        self.update_move_texts(player, game)
        self.update_scores_text(player, game)

        if game.both_moved():
            winner = game.getWinner()

            
            if winner == player:
                self.win_or_lose_text = StaticText(Constants.WIN_OR_LOSE_TEXT_POSITION, Constants.WIN_COLOR, Constants.WIN_OR_LOSE_TEXT_SIZE, Constants.WIN_OR_LOST_TEXT_FONT, Constants.WIN_TEXT_LABLE)
                client_network.send(f'update {str(player)}')
            elif winner == None:
                self.win_or_lose_text = StaticText(Constants.WIN_OR_LOSE_TEXT_POSITION, Constants.TIE_COLOR, Constants.WIN_OR_LOSE_TEXT_SIZE, Constants.WIN_OR_LOST_TEXT_FONT, Constants.TIE_TEXT_LABLE)    

            else:
                self.win_or_lose_text = StaticText(Constants.WIN_OR_LOSE_TEXT_POSITION, Constants.LOSE_COLOR, Constants.WIN_OR_LOSE_TEXT_SIZE, Constants.WIN_OR_LOST_TEXT_FONT, Constants.LOST_TEXT_LABLE)
            
            self.win_or_lose_text.show = True
            
            client_network.send('reset moves')
            


        pygame.display.update()
            


 