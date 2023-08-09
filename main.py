import pygame

clock = pygame.time.Clock()

pygame.init() #обязательный метод в начале

screen = pygame.display.set_mode((800,400)) #установка размера экрана

pygame.display.set_caption("Tutorial") #установка тайтла окна

#установка иконки
icon = pygame.image.load('resources/package_toys.png').convert_alpha()
pygame.display.set_icon(icon)

running = True

bg = pygame.image.load('resources/bg.jpg').convert()

walk_right = [
    pygame.image.load('resources/player/right/right1.png').convert_alpha(),
    pygame.image.load('resources/player/right/right2.png').convert_alpha(),
    pygame.image.load('resources/player/right/right3.png').convert_alpha(),
    pygame.image.load('resources/player/right/right4.png').convert_alpha()
]

walk_left = [
    pygame.image.load('resources/player/left/left1.png').convert_alpha(),
    pygame.image.load('resources/player/left/left2.png').convert_alpha(),
    pygame.image.load('resources/player/left/left3.png').convert_alpha(),
    pygame.image.load('resources/player/left/left4.png').convert_alpha()
]

ghost = pygame.image.load('resources/ghost_left.png').convert_alpha()

#ghost_x = 620
ghost_list_in_game = []

player_anim_count = 0

bg_x = 0

player_speed = 5
player_x = 300
player_y = 310

is_Jump = False
jump_count = 8

bg_sound = pygame.mixer.Sound('resources/sounds/bg.mp3')
#bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)

label = pygame.font.Font('resources/Roboto/Roboto-Black.ttf', 48)

lose_label = label.render('You lose!',False, (255,0,0))
restart_label = label.render('Play again',False, (115,132,148))

restart_label_rect = restart_label.get_rect(topleft=(280,250))

score = 0

gameplay = True

while running:

    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x+800,0))
    
    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
    
        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 7

                if el.x < -10:
                    ghost_list_in_game.pop(i)
                    score += 10

                if(player_rect.colliderect(el)):
                    gameplay = False    

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x,player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x,player_y))

        if not is_Jump:
            if keys[pygame.K_SPACE]:
                is_Jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -=  (jump_count**2)/2
                else:
                    player_y += (jump_count**2)/2
                jump_count -=1
            else:
                is_Jump = False
                jump_count = 8

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
    else:
        screen.fill((87,88,89))
        screen.blit(lose_label, (280,150))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 300
            ghost_list_in_game.clear()
            score = 0
    
    score_label = label.render(f'Score: {score}', True, (255, 255, 0))  
    screen.blit(score_label, (10, 10))


   

    pygame.display.update() #обновление экрана

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 310)))

    clock.tick(20)