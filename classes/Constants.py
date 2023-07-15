import os

class Constants:
    SCREEN_WIDTH = 700
    SCREEN_HEIGHT = 700
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WAITING_SCREEN_BACKGROUND = os.path.abspath('./images/waiting-scene.jpg')
    PLAYING_SCREEN_BACKGROUND = os.path.abspath('./images/playing-scene1.jpg')
    ROCK_BUTTON_IMAGE = os.path.abspath('./images/rock.png')
    PAPER_BUTTON_IMAGE = os.path.abspath('./images/paper.png')
    SCISSOR_BUTTON_IMAGE = os.path.abspath('./images/scissor.png')
    RPS_BUTTON_SIZE = (100, 100)
    ROCK_BUTTON_POSITION = (100, 500)
    PAPER_BUTTON_POSITION = (500, 500)
    SCISSOR_BUTTON_POSITION = (300, 500)
    ROCK_BUTTON_HIGHLIGHTED_COLOR = (0,255, 255)
    SCISSOR_BUTTON_HIGHLIGHTED_COLOR = (255, 255, 0)
    PAPER_BUTTON_HIGHLIGHTED_COLOR = (255, 0, 0)
    LOCKED_IN_TEXT_POSITION = (455,400)
    PLAY_TEXT_POSITION = (80,400)
    OPPONENT_WAITING_TEXT_POSITION = (470,400)
    MOVE_TEXT_POSITION = (80,400)
    LOCKED_IN_TEXT_COLOR = (255, 0, 0)
    PLAY_TEXT_COLOR = (255, 255, 255)
    MOVE_TEXT_COLOR = (0, 0, 0)
    OPPONENT_WAITING_TEXT_COLOR = (0,0,0)
    GAME_SOUND = os.path.abspath('./audio/game-sound.ogg')

   