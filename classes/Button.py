from .Clickable import Clickable
from .TextManager import StaticText
import pygame


class Button(Clickable):

    def __init__(self) -> None:
        pass

    def draw(self, surface:pygame.Surface)->None:
        pass

    def update(self, surface:pygame.Surface):
        #pygame.display.flip()
        pass

    def clicked(self, pos:tuple[int,int])->bool:
        pass



class RPSBUTTON(Button):
    
    def __init__(self, size:tuple[int,int], position: tuple[int, int], image_url: str, tag_name:str, highlighted_color:str) -> None:
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load(image_url).convert_alpha(), self.size)
        self.tag_name = tag_name
        self.image_rect = self.image.get_rect()
        self.image_rect.x = position[0]
        self.image_rect.y = position[1]
        self.highlighted = False
        self.selected = False
        self.last_clicked_time = None
        self.clicked_speed_time = 3000
        self.highlighted_color = highlighted_color


    def draw(self, surface: pygame.Surface):
        surface.blit(self.image, self.image_rect)
        if self.highlighted:
            pygame.draw.rect(surface, self.highlighted_color, self.image_rect, 5, 15, 15, 15, 15)
        if self.selected:
            pygame.draw.rect(surface, self.highlighted_color, self.image_rect, 5, 15, 15, 15, 15)
    
    def update(self):
        self.highlighted = True if self.image_rect.collidepoint(pygame.mouse.get_pos()) else False
    
    def clicked(self, pos: tuple[int, int]):
        if self.last_clicked_time == None:
            if pygame.mouse.get_pressed()[0] == 1 and self.image_rect.collidepoint(pos[0], pos[1]):
                self.last_clicked_time = pygame.time.get_ticks()
                return True
            return False
            

        
        if pygame.time.get_ticks() - self.last_clicked_time >= self.clicked_speed_time:
            if pygame.mouse.get_pressed()[0] == 1 and self.image_rect.collidepoint(pos[0], pos[1]):
                self.last_clicked_time = pygame.time.get_ticks()
                return True
            return False
    


class NormalButton(Button):

    def __init__(self, dimension:tuple[int,int,int,int], bg_color:pygame.Color, text_color:pygame.Color, text:str, size:int) -> None:
        self.rect = pygame.Rect(dimension[0], dimension[1], dimension[2], dimension[3])
        self.color = bg_color
        self.text_size = size
        self.text = StaticText((dimension[0], dimension[1]), text_color, self.text_size,'comicsans', text)

    def draw(self, surface: pygame.Surface):
        pygame.draw.rect(surface, self.color, self.rect, 0, 15, 15, 15, 15)
        self.text.render(surface)
    
    def update(self):
        self.text.update()
        pygame.display.update()
    
    def clicked(self, pos: tuple[int, int]):
        return pygame.mouse.get_pressed()[0] == 1 and self.rect.collidepoint(pos[0], pos[1])
    
       
    