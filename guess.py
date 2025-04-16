import pygame
from random import choice
from sys import exit

def move_color(color, name):
    keys = pygame.mouse.get_pressed()
    if keys[0]:
        color.x = pygame.mouse.get_pos()[0]-22
        color.y = pygame.mouse.get_pos()[1]-22
        pygame.draw.ellipse(screen, name, color)

def check_collision(color, name):
    for j in range(10):
        if guess == j:
            for i in range(j*4 +1, j*4 +5):
                if color.colliderect(sockets[f'socket{i}']):
                    sockets[f'socket_{i}'] = name
                    return False
    return color

def check_colours(args):
    if (args == answer):
        return (4,0,0)
    correct = 0
    uncorrect = 0
    copy = answer.copy()
    user_copy = args.copy()
    for i in range(4):
      if args[i] == answer[i]:
        correct += 1
        copy.remove(args[i])
        user_copy.remove(args[i])
    for i in range(len(user_copy)):   
      if user_copy[i] in copy:
        uncorrect += 1
        copy.remove(user_copy[i])

    return(correct, uncorrect, 4-correct - uncorrect)

pygame.init()
screen = pygame.display.set_mode((500, 680))
pygame.display.set_caption("Guess")
refresh = pygame.time.Clock()

yellow, red, green, blue, orange, purple = 0, 0, 0, 0, 0, 0
yellow_copy, red_copy, green_copy, blue_copy, orange_copy, purple_copy = [False]*6
run,win,guess = True, False, 0
rules= 'Rules:\n1. A random sequence of 4 colours will be generated.\n2. You will have to guess the sequence.\n3. Drag the colours to socket and press Enter to guess.\n4. You will get hints after every guess.\n5. You have 10 guesses.\n6. Number of black dots is the number of correct colours\n    in correct position.\n7. Number of white dots is the number of correct colours\n    in wrong position.\n8. Number of grey dots is the number of wrong colours.\n9. Press any key to continue.'
rules = list(rules.split('\n'))
colour_names = ['yellow', 'red', 'green', 'blue', 'orange', 'purple']
answer = [choice(colour_names), choice(colour_names), choice(colour_names), choice(colour_names)]
#print(answer)

wallpaper = pygame.Surface((500, 700))
wallpaper.fill('grey')
pygame.font.init()
font = pygame.font.Font(None, 50)
font2= pygame.font.Font(None, 25)
text = font.render('GUESS', True, (255,0,255))
text_rect = text.get_rect(topleft = (200,20))

j = 170
for i in colour_names:
    surface = pygame.Rect((40, j, 45, 45))
    globals()[i] = surface
    j += 60

sockets = {}
j=40
for i in range(40):
    if i%4 == 0:
        j += 55
        k = 0
    sockets[f"socket{i+1}"] = pygame.Rect((150+(k*57), j, 45, 45))
    sockets[f"socket_{i+1}"]= 'grey'
    k +=1

answers = {}
color = {}
j = 60
for i in range(1, 41):
    if i % 2 == 0:
        x = 405
    else:
        x = 385
        j += 20
    if (i-1) % 4 == 0:
        j += 15
    answers[i] = pygame.Rect(x, j, 18, 18)
    color[i] = 'grey'

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN: 
            run = False
            sockets['socket_1'], sockets['socket_2'], sockets['socket_3'], sockets['socket_4'] = ['azure4']*4
    screen.blit(wallpaper, (0,0))
    screen.blit(text, text_rect)
    j = 100
    for lines in rules:
        screen.blit(font2.render(lines, True, 'black'), (20, j))
        j += 40
    pygame.display.update()
    refresh.tick(6)

run, index = True, 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if yellow.collidepoint(pygame.mouse.get_pos()): yellow_copy = yellow.copy()
            if red.collidepoint(pygame.mouse.get_pos()):    red_copy = red.copy()
            if green.collidepoint(pygame.mouse.get_pos()):  green_copy = green.copy()
            if blue.collidepoint(pygame.mouse.get_pos()):   blue_copy = blue.copy()
            if orange.collidepoint(pygame.mouse.get_pos()): orange_copy = orange.copy()
            if purple.collidepoint(pygame.mouse.get_pos()): purple_copy = purple.copy()

        if event.type == pygame.MOUSEBUTTONUP:
            if yellow_copy:
                yellow_copy = check_collision(yellow_copy, 'yellow')
            if red_copy:
                red_copy = check_collision(red_copy, 'red')
            if green_copy:  
                green_copy = check_collision(green_copy, 'green')
            if blue_copy:
                blue_copy = check_collision(blue_copy, 'blue')
            if orange_copy:
                orange_copy = check_collision(orange_copy, 'orange')
            if purple_copy:
                purple_copy = check_collision(purple_copy, 'purple')
            yellow_copy, red_copy, green_copy, blue_copy, orange_copy, purple_copy = [False]*6

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                for j in range(10):
                    if guess == j:   
                        i = guess*4 +1
                        values = check_colours([sockets[f'socket_{i}'], sockets[f'socket_{i+1}'], sockets[f'socket_{i+2}'], sockets[f'socket_{i+3}']])
                        sockets[f'socket_{i+4}'], sockets[f'socket_{i+5}'], sockets[f'socket_{i+6}'], sockets[f'socket_{i+7}'] = ['azure4']*4
                if values[0] == 4:
                    run = False
                    win = True
                guess += 1
                if guess == 10: run = False

                for _ in range(values[0]):
                    color[index] = 'black'
                    index += 1
                for _ in range(values[1]):
                    color[index] = 'white'
                    index += 1
                for _ in range(values[2]):
                    color[index] = 'azure4'
                    index += 1

    screen.blit(wallpaper, (0,0))
    pygame.draw.ellipse(screen, 'black', pygame.Rect(180, 11, 160, 50))
    screen.blit(text, text_rect)

    pygame.draw.ellipse(screen, 'yellow', yellow)
    pygame.draw.ellipse(screen, 'red', red)
    pygame.draw.ellipse(screen, 'green', green)
    pygame.draw.ellipse(screen, 'blue', blue)
    pygame.draw.ellipse(screen, 'orange', orange)
    pygame.draw.ellipse(screen, 'purple', purple)

    for i in range(1,41):
        pygame.draw.ellipse(screen, sockets[f'socket_{i}'], sockets[f'socket{i}'])
        pygame.draw.ellipse(screen, color[i], answers[i])

    if yellow_copy:
        move_color(yellow_copy, 'yellow')
    if red_copy:
        move_color(red_copy, 'red')
    if green_copy:
        move_color(green_copy, 'green')
    if blue_copy:
        move_color(blue_copy, 'blue')
    if orange_copy:
        move_color(orange_copy, 'orange')
    if purple_copy:
        move_color(purple_copy, 'purple')

    pygame.display.update()
    refresh.tick(60)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(wallpaper, (0,0))
    if win:
        screen.blit(font.render("Your guess's correct", True, 'black'), (85,20))
    else:
        screen.blit(font.render("HAHA NOOB! You lost", True, 'black'), (72,20))
    screen.blit(pygame.font.Font(None, 40).render("Correct answer:", True, 'black'), (20, 120))

    pygame.draw.ellipse(screen, answer[0], pygame.Rect(250, 113, 40, 40))
    pygame.draw.ellipse(screen, answer[1], pygame.Rect(300, 113, 40, 40))
    pygame.draw.ellipse(screen, answer[2], pygame.Rect(350, 113, 40, 40))
    pygame.draw.ellipse(screen, answer[3], pygame.Rect(400, 113, 40, 40))
    pygame.display.update()
    refresh.tick(6)