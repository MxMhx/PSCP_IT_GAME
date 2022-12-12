import pygame
from object.move import move
from object.cat import Cat

WIDTH, HEIGHT =  700, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("cats and Ladders")

WHITE = ((255, 255, 255))
FPS = 60

bg_image = pygame.image.load('Art/Ladders_Finish.png')
bg_size = pygame.transform.scale(bg_image, (700, 700))

amount = 4

cat = []
cat.append(Cat(1))
cat.append(Cat(2))
cat.append(Cat(3))
cat.append(Cat(4))

def draw2():
    screen.fill(WHITE)
    screen.blit(bg_size, (0, 0))
    move(cat,amount,screen)
    pygame.display.update()
def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw2()
    pygame.quit()

if __name__ == "__main__":
    main()
