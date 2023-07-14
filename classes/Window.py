import pygame
import sys
from .Constants import Constants
from .Scene import Scene
from .WaitingScene import WaitingScene
from .PlayingScene import PlayingScene
from .ClientNetwork import ClientNetwork
from .TextManager import StaticText, BlinkableText, AnimatedText

#from .PlayingScene import PlayingScene

class Window:
    CLOCK:pygame.time.Clock = pygame.time.Clock()
    FRAME_RATE:int = 60
    CURRENT_SCENE:Scene = None
    SURFACE:pygame.Surface = None

    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        Window.SURFACE = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        pygame.display.set_caption("ROCK PAPER SCISSORS")
        Window.CURRENT_SCENE = WaitingScene(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.WAITING_SCREEN_BACKGROUND)
        Window.CURRENT_SCENE.init()
        pygame.mixer.music.load(Constants.GAME_SOUND)
        pygame.mixer.music.play(-1)

    @staticmethod
    def changeScene(currentScene:Scene):
        Window.CURRENT_SCENE = currentScene
        Window.CURRENT_SCENE.init()
    
    @staticmethod
    def run(client_network:ClientNetwork):   
        game = None
        player = ClientNetwork.getId()
        while True:
            Window.CLOCK.tick(Window.FRAME_RATE)
            
            if player:
                game = client_network.send('get-game')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    Window.changeScene(PlayingScene(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.PLAYING_SCREEN_BACKGROUND))


            if isinstance(Window.CURRENT_SCENE, WaitingScene):
                if game and game.ready:
                    Window.changeScene(PlayingScene(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.PLAYING_SCREEN_BACKGROUND))
   

            Window.draw()
            Window.update(player=player, game = game)
       

    @staticmethod
    def check_for_event():
        pass

    @staticmethod        
    def draw():
        Window.CURRENT_SCENE.draw()
        Window.SURFACE.blit(Window.CURRENT_SCENE.surface, (0, 0))

    @staticmethod
    def update(**kwargs):
        Window.CURRENT_SCENE.update(**kwargs)

    @staticmethod
    def checkEvents():
        pass
