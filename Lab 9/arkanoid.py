import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
transparent_surface = pygame.Surface((W, H), pygame.SRCALPHA)
transparent_surface.fill((255, 255, 255, 50))
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# paddle
paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


# block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                          100, 50) for i in range(10) for j in range(4)]
color_list = [(0,230,0)
              for i in range(10) for j in range(4)]
r = random.sample(range(0,40), 10)
unbreakable = r[:5]
bonus = r[5:]
for i in range(len(unbreakable)):
    color_list[unbreakable[i]]=(255,255,255)
for i in range(len(bonus)):
    color_list[bonus[i]]=(255,242,0)

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

#Pause Screen
pausefont = pygame.font.SysFont('comicsansms', 80)
pausetext = pausefont.render('Pause', 1, (255, 255, 255))
pausetextRect = pausetext.get_rect()
pausetextRect.center = (W // 2, H // 2-200)
paused = True

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while not done:
    for event in pygame.event.get():
        if not paused and event.type == INC_SPEED:
            ballSpeed += 0.2
            paddle.width -= 2
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: #check pause
            if event.key == pygame.K_SPACE:
                paused = not paused

    screen.fill(bg)

    if not paused:
        [pygame.draw.rect(screen, color_list[color], block)
         for color, block in enumerate(block_list)]  # drawing blocks
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
        pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

        # Ball movement
        ball.x += ballSpeed * dx
        ball.y += ballSpeed * dy

        # Collision left
        if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
            dx = -dx
        # Collision top
        if ball.centery < ballRadius + 50:
            dy = -dy
        # Collision with paddle
        if ball.colliderect(paddle) and dy > 0:
            dx, dy = detect_collision(dx, dy, ball, paddle)

        # Collision blocks
        hitIndex = ball.collidelist(block_list)

        if hitIndex != -1:
            if hitIndex not in unbreakable:
                if hitIndex in bonus:
                    paddle.width*=1.5
                    ballSpeed/=1.5
                hitRect = block_list.pop(hitIndex)
                hitColor = color_list.pop(hitIndex)
                game_score += 1
                for i in range(len(unbreakable)):
                    if hitIndex<unbreakable[i]:
                        unbreakable[i]-=1
                for i in range(len(bonus)):
                    if hitIndex<bonus[i]:
                        bonus[i]-=1
            else:
                hitRect = block_list[hitIndex]
                hitColor = color_list[hitIndex]
            dx, dy = detect_collision(dx, dy, ball, hitRect)
            collision_sound.play()

        # Game score
        game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
        screen.blit(game_score_text, game_score_rect)

        # Win/lose screens
        if ball.bottom > H:
            screen.fill((0, 0, 0))
            screen.blit(losetext, losetextRect)
        elif len(block_list)==len(unbreakable):
            screen.fill((255, 255, 255))
            screen.blit(wintext, wintextRect)

        # Paddle Control
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and paddle.left > 0:
            paddle.left -= paddleSpeed
        if key[pygame.K_RIGHT] and paddle.right < W:
            paddle.right += paddleSpeed
    else:  # If the game is paused, display the pause screen
        key = pygame.key.get_pressed()
        if key[pygame.K_e]:
            paddle.width+=1
        elif key[pygame.K_q]:
            paddle.width-=1
        if key[pygame.K_d]:
            ballSpeed+=0.05
        elif key[pygame.K_a]:
            ballSpeed-=0.05
        screen.blit(transparent_surface, (0, 0))
        screen.blit(pausetext, pausetextRect)
        settingsPaddlefont = pygame.font.SysFont('comicsansms', 40)
        settingsPaddletext = settingsPaddlefont.render(f'Paddle width: {paddle.width}', 1, (255, 255, 255))
        settingsPaddletextRect = settingsPaddletext.get_rect()
        settingsPaddletextRect.center = (W // 2, H // 2 - 50)
        settingsBallfont = pygame.font.SysFont('comicsansms', 40)
        settingsBalltext = settingsBallfont.render(f'Ball speed: {ballSpeed}', 1, (255, 255, 255))
        settingsBalltextRect = settingsBalltext.get_rect()
        settingsBalltextRect.center = (W // 2, H // 2 + 50)
        screen.blit(settingsPaddletext,settingsPaddletextRect)
        screen.blit(settingsBalltext,settingsBalltextRect)

    pygame.display.flip()
    clock.tick(FPS)