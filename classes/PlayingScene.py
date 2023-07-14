from .Scene import Scene as Sc
from typing import List
from .Button import Button, RPSBUTTON, NormalButton
from .Constants import Constants
import pygame

class PlayingScene(Sc):
    def __init__(self, width, height, background_image_url):
        super().__init__(width, height, background_image_url)
        self.buttons:List[Button] = [RPSBUTTON(Constants.RPS_BUTTON_SIZE, Constants.ROCK_BUTTON_POSITION, Constants.ROCK_BUTTON_IMAGE,'ROCK'), RPSBUTTON(Constants.RPS_BUTTON_SIZE, Constants.SCISSOR_BUTTON_POSITION, Constants.SCISSOR_BUTTON_IMAGE, 'SCISSOR'), RPSBUTTON(Constants.RPS_BUTTON_SIZE, Constants.PAPER_BUTTON_POSITION, Constants.PAPER_BUTTON_IMAGE, 'PAPER')]
        self.init()


    def init(self):
        pass

    def draw(self):
        self.surface.blit(self.background_image, (0, 0))

        for button in self.buttons:
            button.draw(self.surface)
            button.update()

        for button in self.buttons:
            mouse_position = pygame.mouse.get_pos()
            if button.clicked(mouse_position):
                print(f'{button.tag_name} was clicked')    
        


    def update(self, **kwargs):
        pygame.display.flip()