import pygame
from pygame.locals import *
import random
import time
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 720
        self.hz = 80
        self.t = 1/self.hz
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.time = time.time()

        self.image = pygame.image.load("dvd-logo-png-19264.png").convert_alpha()
        self.image_rect = self.image.get_rect() 
        self.image_rect.center = (self.weight // 2, self.height // 2)
        self.iweight, self.iheight = self.image.get_size()
        self.vector = (-1/100*self.iweight, 1/100*self.iheight)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
    
    def on_loop(self):
        if self.image_rect.left + self.vector[0] <= 0 or self.image_rect.right + self.vector[0] >= self.weight: # colisión pared 
            self.vector = (-self.vector[0], self.vector[1])  
        if self.image_rect.top + self.vector[1] <= 0 or self.image_rect.bottom + self.vector[1] >= self.height: # colisión techo 
            self.vector = (self.vector[0], -self.vector[1])
        if time.time() - self.time > self.t:
            self.time = time.time()
            self.image_rect.topleft = self.image_rect.topleft[0] + self.vector[0], self.image_rect.topleft[1] + self.vector[1]  
            
    def on_render(self):
        self._display_surf.fill((0, 0, 0)) 
        self._display_surf.blit(self.image, self.image_rect)
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()