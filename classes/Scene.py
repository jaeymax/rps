import pygame

class Scene:
    
    def __init__(self, width, height, background_image_url):
        self.width = width
        self.height = height
        if background_image_url:
            self.background_image = pygame.transform.scale(pygame.image.load(background_image_url).convert_alpha(), (width, height))
        else:
            self.background_image = None
        self.surface = pygame.Surface((width, height))

    def init(self):
        pass    

    def draw(self):
        pass

    def update(self):
        pass

