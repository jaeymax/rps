from .Scene import Scene
from .Button import NormalButton
from .Constants import Constants
from .Game import Game
from .TextManager import BlinkableText
import pygame

class GameOverScene(Scene):
    
    def __init__(self, width, height, background_image_url):
        super().__init__(width, height, background_image_url)
        self.play_again_text = BlinkableText(Constants.PLAY_AGAIN_TEXT_POSITION, Constants.PLAY_AGAIN_TEXT_COLOR, Constants.PLAY_AGAIN_TEXT_SIZE, Constants.PLAY_AGAIN_TEXT_NAME, Constants.PLAY_AGAIN_TEXT)
        self.play_again_text.show = True
        self.background_image = background_image_url

    def init(self, player:str, game:Game):
        winner = game.getWinner()
        
        winner = 1 if game.player1_score == Constants.MAX_SCORE else 2
        if winner == int(player):
            print('you won')
            self.background_image = pygame.transform.scale(pygame.image.load(Constants.WIN_BACKGROUND_IMAGE).convert_alpha(), (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        else:
            print('you lost')
            self.background_image = pygame.transform.scale(pygame.image.load(Constants.LOSE_BACKGROUND_IMAGE).convert_alpha(), (Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

    def draw(self):
        self.surface.blit(self.background_image, (0, 0))
        self.play_again_text.render(self.surface)

    def update(self, **kwargs):
        player = int(kwargs.get('player'))
        game = kwargs.get('game')
        self.play_again_text.update()
        pygame.display.update()