import pygame
import sys
from .Constants import Constants
from .Scene import Scene
from .WaitingScene import WaitingScene
from .PlayingScene import PlayingScene
from .GameOverScene import GameOverScene
from .ClientNetwork import ClientNetwork


class Window:
    CLOCK:pygame.time.Clock = pygame.time.Clock()
    FRAME_RATE:int = 30
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
    def changeScene(currentScene:Scene, player, game):
        Window.CURRENT_SCENE = currentScene
        Window.CURRENT_SCENE.init(player, game)
    
    @staticmethod
    def run(client_network:ClientNetwork):   
        game = None
        player = ClientNetwork.getId()
        while True:
            Window.CLOCK.tick(Window.FRAME_RATE)
            
            if player:
                try:
                    game = client_network.send('get-game')
                except:
                    print("couln't get game")    

            else:
                player = ClientNetwork.connect_to_server()
                if player:
                    game = client_network.send('get-game')
            
            
            
            Window.draw()
            Window.update(player = player, game=game, client_network = client_network)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            if isinstance(Window.CURRENT_SCENE, WaitingScene):
                if game and game.ready():
                    Window.changeScene(PlayingScene(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.PLAYING_SCREEN_BACKGROUND), player, game)


            elif isinstance(Window.CURRENT_SCENE, PlayingScene):
                 if game.both_moved():
                    Window.draw()
                    pygame.display.update()
                    pygame.time.delay(2000)
                 
                 if game.player1_score == Constants.MAX_SCORE or game.player2_score == Constants.MAX_SCORE:
                     client_network.send('game over')
                     Window.changeScene(GameOverScene(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, None), player, game)
                    #Window.CURRENT_SCENE.
                    #client_network.send('reset moves')
            elif isinstance(Window.CURRENT_SCENE, GameOverScene):
                if Window.CURRENT_SCENE.play_again_button.clicked(pygame.mouse.get_pos()):
                    client_network.send(f'ready {player}')
                    Window.changeScene(WaitingScene(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, Constants.WAITING_SCREEN_BACKGROUND), player, game)

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
