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
        self.play_text = BlinkableText(Constants.PLAY_TEXT_POSITION, Constants.PLAY_TEXT_COLOR, 60, 'comicsans', 'PLAY')
        self.opponent_waiting_text = BlinkableText(Constants.OPPONENT_WAITING_TEXT_POSITION, Constants.OPPONENT_WAITING_TEXT_COLOR, 60, 'comicsans','WAITING')
        self.locked_in_text = StaticText(Constants.LOCKED_IN_TEXT_POSITION,Constants.LOCKED_IN_TEXT_COLOR, 60, 'comicsans', 'LOCKED IN')
        self.move_text = StaticText(Constants.MOVE_TEXT_POSITION,Constants.MOVE_TEXT_COLOR, 60, 'comicsans', '')
        self.init()


    def init(self):
        pass


    def draw(self):
        self.surface.blit(self.background_image, (0, 0))

        self.rock_button.draw(self.surface)
        self.scissor_button.draw(self.surface)
        self.paper_button.draw(self.surface)   
        self.play_text.render(self.surface)
        self.opponent_waiting_text.render(self.surface)
        self.locked_in_text.render(self.surface)
        self.move_text.render(self.surface)   

    def update(self, **kwargs):
        game:Game = kwargs.get('game')
        player = int(kwargs.get('player'))
        client_network:ClientNetwork = kwargs.get('client_network')
        self.rock_button.update()
        self.scissor_button.update()
        self.paper_button.update()
        self.play_text.update()
        self.opponent_waiting_text.update()
        self.locked_in_text.update()
        self.move_text.update()
        mouse_position = pygame.mouse.get_pos()

        if self.rock_button.clicked(mouse_position):
            if player == 1:
                if not game.player1_moved:
                    client_network.send('R')
                    
                print('Rock button was clicked by player 1')
            else:
                if not game.player2_moved:
                    client_network.send('R')
                print('Rock button was clicked by player 2')
        elif self.scissor_button.clicked(mouse_position):
            if player == 1:
                if not game.player1_moved:
                    client_network.send('S')
                print('Scissor button was clicked by player 1')    
            else:
                if not game.player2_moved:
                    client_network.send('S')
                print('Scissor button was clicked by player 2')
        elif self.paper_button.clicked(mouse_position):
            if player == 1:
                if not game.player1_moved:
                    client_network.send('P')
                print('Paper button was clicked by player 1')
            else:
                if not game.player2_moved:
                    client_network.send('P')
                print('Paper button was clicked by player 2')

        if player == 1:
            if game.player1_moved:
               move:str = game.player1_move
               if move == 'R':
                   self.rock_button.selected = True
               elif move == 'S':
                   self.scissor_button.selected = True
               else:
                   self.paper_button.selected = True  
        else:
            if game.player2_moved:
               move:str = game.player2_move
               if move == 'R':
                   self.rock_button.selected = True
               elif move == 'S':
                   self.scissor_button.selected = True
               else:
                   self.paper_button.selected = True

        if player == 1:
            if game.player1_moved:
                print(f'you chose {game.player1_move}')
                move:str = game.player1_move
                text = ''
                if move == 'R':
                    text = 'ROCK'
                elif move == 'S':
                    text = 'PAPER'
                else:
                    text = 'SCISSORS'
                self.move_text =  StaticText(Constants.MOVE_TEXT_POSITION,Constants.MOVE_TEXT_COLOR, 60, 'comicsans', text)
                self.move_text.show = True
                self.play_text.show = False
            else:
                print('play!')
                self.play_text.show = True
                self.move_text.show = False

            if game.player2_moved:
                print('opponent locked in')
                self.locked_in_text.show = True
                self.opponent_waiting_text.show = False
            else:
                print('waiting for opponents move')        
                self.opponent_waiting_text.show = True
                self.locked_in_text.show = False
        else:
            if game.player2_moved:
                print(f'you chose {game.player2_move}')
                move:str = game.player2_move
                text = ''
                if move == 'R':
                    text = 'ROCK'
                elif move == 'S':
                    text = 'PAPER'
                else:
                    text = 'SCISSORS'
                self.move_text =  StaticText(Constants.MOVE_TEXT_POSITION,Constants.MOVE_TEXT_COLOR, 60, 'comicsans', text)
                self.move_text.show = True
                self.play_text.show = False

            else:
                print('play!')
                self.play_text.show = True
                self.move_text.show = False
            
            if game.player1_moved:
                print('opponent locked in')
                self.locked_in_text.show = True
                self.opponent_waiting_text.show = False
            else:
                print('waiting for opponents move')
                self.opponent_waiting_text.show = True    
                self.locked_in_text.show = False
        
        if game.both_moved:
            winner = game.getWinner()

            
        
        pygame.display.flip()