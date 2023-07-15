import pygame
import time

class Text:

    def __init__(self, position:tuple[int,int], color:pygame.Color, size:int, name:str, text:str) -> None:
        pygame.font.init()
        self.size = size
        self.font = pygame.font.SysFont(name, self.size, False, True)
        self.font_image = self.font.render(text, 1, color, None)
        self.font_rect = self.font_image.get_rect()
        self.font_rect.x, self.font_rect.y = position
        self.show = False

    def render(self, surface:pygame.Surface):
       pass

    def update(self):
        pygame.display.flip()



class StaticText(Text):

    def __init__(self, position: tuple[int, int], color: pygame.Color, size: int, name: str, text: str) -> None:
        super().__init__(position, color, size, name, text)

    def render(self, surface: pygame.Surface):
        if self.show:
            surface.blit(self.font_image, self.font_rect)   
    
    def update(self):
        return super().update()
    


class AnimatedText(Text):

      def __init__(self, position: tuple[int, int], color: pygame.Color, size: int, name:str, *text: str) -> None:
          pygame.font.init()
          self.size = size
          self.font = pygame.font.SysFont(name, self.size)
          self.font_images = [self.font.render(text[i], 1, color, None) for i in range(len(text))]
          self.image_rect = self.font_images[0].get_rect()
          self.image_rect.x, self.image_rect.y = position
          self.frame_index = 0
          self.animation_speed = 1000
          self.last_update_animation_time = pygame.time.get_ticks()
          self.show = False

      def render(self, surface: pygame.Surface):
          if self.show:
            if pygame.time.get_ticks() - self.last_update_animation_time >= self.animation_speed:
                self.frame_index += 1
                self.last_update_animation_time = pygame.time.get_ticks()

            surface.blit(self.font_images[self.frame_index % len(self.font_images)], self.image_rect)    

      def update(self):
          return super().update()



class BlinkableText(Text):
    def __init__(self, position: tuple[int, int], color: pygame.Color, size: int, name: str, text: str) -> None:
        super().__init__(position, color, size, name, text)
    
    def render(self, surface: pygame.Surface):
        if self.show:
            if time.time() % 1 > 0.5:
                surface.blit(self.font_image, self.font_rect)
    
    def update(self):
        return super().update()