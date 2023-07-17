from .Scene import Scene as Sc
import pygame
from .TextManager import AnimatedText, StaticText, BlinkableText

class WaitingScene(Sc):
     def __init__(self, width, height, background_image_url):
          super().__init__(width, height, background_image_url)
          self.init()
          self.unable_to_connect_text = StaticText((70, 100), (0,0,0),60, 'comicsans', "Coudn't connet to server")
          self.connecting_text = AnimatedText((250, 600),(0,0,0), 40,'comicsans','Connecting.','Connecting..','Connecting...')
          self.waiting_for_opponent_text = BlinkableText((100,100),(0,0,0),60, 'comicsans', 'Waiting for Opponent')
          

     def init(self, *args):
         pass
         
     def draw(self):
         self.surface.blit(self.background_image, (0, 0))
         self.unable_to_connect_text.render(self.surface)
         self.unable_to_connect_text.update()
         self.connecting_text.render(self.surface)
         self.connecting_text.update()
         self.waiting_for_opponent_text.render(self.surface)
         self.waiting_for_opponent_text.update()


     def update(self, **kwargs):
         if kwargs.get("player"):
            game = kwargs.get("game")
            if game.ready():
                pass
            else:
                self.waiting_for_opponent_text.show = True
                self.unable_to_connect_text.show = False
                self.connecting_text.show = False
         else:
             self.unable_to_connect_text.show = True
             self.connecting_text.show = True         

         pygame.display.flip()

