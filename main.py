import pygame

clock = pygame.time.Clock()

pygame.init() #обязательный метод в начале

screen = pygame.display.set_mode((800,400)) #установка размера экрана

pygame.display.set_caption("Tutorial") #установка тайтла окна

#установка иконки
icon = pygame.image.load('resources/package_toys.png')
pygame.display.set_icon(icon)

running = True

bg = pygame.image.load('resources/bg.jpg')
#player = pygame.image.load('resources/package_toys(2).png')
#player = pygame.image.load('resources/player/right/right1.png')

walk_right = [
    pygame.image.load('resources/player/right/right1.png'),
    pygame.image.load('resources/player/right/right2.png'),
    pygame.image.load('resources/player/right/right3.png'),
    pygame.image.load('resources/player/right/right4.png')
]

walk_left = [
    pygame.image.load('resources/player/left/left1.png'),
    pygame.image.load('resources/player/left/left2.png'),
    pygame.image.load('resources/player/left/left3.png'),
    pygame.image.load('resources/player/left/left4.png')
]

player_anim_count = 0

bg_x = 0

bg_sound = pygame.mixer.Sound('resources/sounds/bg.mp3')
bg_sound.play()

while running:

    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x+800,0))
    screen.blit(walk_right[player_anim_count], (300,310))

    if player_anim_count == 3: 
        player_anim_count = 0
    else: 
        player_anim_count +=1

    bg_x -=2
    if bg_x == -800:
        bg_x = 0

    pygame.display.update() #обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(20)