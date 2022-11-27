import random as rand
import pygame
 
x = 530
y = 0
 
reverse_x = False
reverse_y = False

SIZE = WIDTH, HEIGHT = 600, 400 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('black') #The background colod of our window
FPS = 10 #Frames per second

pygame.display.set_caption('PySaver - DvD')

class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        super(MySprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('./PyL1.png'))
        self.images.append(pygame.image.load('./PyL2.png'))
        self.images.append(pygame.image.load('./PyL3.png'))
        self.images.append(pygame.image.load('./PyL4.png'))
 
        self.index = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(x, y, 64, 64)
 
    def update(self):
        global reverse_x
        global reverse_y
        global x
        if reverse_x == False:
            x = x - 5
        elif reverse_x == True:
            x = x + 5
        
        if x <= 0:
            reverse_x = True
            self.index += 1
        if x >= 535:
            reverse_x = False
            self.index += 1
        global y

        if reverse_y == False:
            y = y + 5
        elif reverse_y == True:
            y = y - 5
        if y >= 335:
            reverse_y = True
            self.index += 1
        if y <= 0:
            reverse_y = False
            self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.rect = pygame.Rect(x, y, 64, 64)
        
        self.image = self.images[self.index]
 
def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    my_sprite = MySprite()
    my_group = pygame.sprite.Group(my_sprite)
    clock = pygame.time.Clock()
 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        my_group.update()
        screen.fill(BACKGROUND_COLOR)
        my_group.draw(screen)
        pygame.display.update()
        clock.tick(20)
 
if __name__ == '__main__':
    main()
 