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

player_speed = 5
player_x = 300
player_y = 310

is_Jump = False
jump_count = 7

bg_sound = pygame.mixer.Sound('resources/sounds/bg.mp3')
#bg_sound.play()

while running:

    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x+800,0))
    screen.blit(walk_right[player_anim_count], (player_x,player_y))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x,player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x,player_y))

    if not is_Jump:
        if keys[pygame.K_SPACE]:
            is_Jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -=  (jump_count**2)/2
            else:
                player_y += (jump_count**2)/2
            jump_count -=1
        else:
            is_Jump = False
            jump_count = 7

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 750:
        player_x += player_speed

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