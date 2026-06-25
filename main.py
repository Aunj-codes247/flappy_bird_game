
import random
import sys
import pygame
import pygame.locals
from pygame.locals import *


#global variable for the game

FPS =  32

SCREEN_WIDTH = 289
SCREEN_HEIGHT = 511

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


GROUND_Y = SCREEN_HEIGHT * 0.8

GAME_SPRITES = {}
GAME_SOUND = {}

PLAYER = 'sprites/bird.png'
BACKGROUND = 'sprites/background.png'

PIPE = 'sprites/pillar.png'



def welcomeScreen():

    """
    show welcome image on the screen

    """

    playerx = int(SCREEN_WIDTH/5)

    playery = int(SCREEN_HEIGHT- GAME_SPRITES['player'].get_height())/2

    massagex = int(SCREEN_WIDTH - GAME_SPRITES['massage'].get_width())/2

    massagey = int(SCREEN_HEIGHT*0.13)

    basex = 0
    while True:

        for event in pygame.event.get(): # tells us about the clicks by keyboard or mourse or any thing

            if event.type == QUIT or (event.type == KEYDOWN and event.key== K_ESCAPE) :
                pygame.quit()
                sys.exit()
        
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):

                return 
            
            else:

                SCREEN.blit(GAME_SPRITES['background'],(0,0))
                SCREEN.blit(GAME_SPRITES['player'],(playerx,playery))
                SCREEN.blit(GAME_SPRITES['massage'],(massagex,massagey))
                SCREEN.blit(GAME_SPRITES['base'],(basex,GROUND_Y))
                pygame.display.update()
                FPSCLOCK.tick(FPS)




def maingame():

    score = 0
    playerx = int(SCREEN_WIDTH/5)

    playery = int(SCREEN_WIDTH/2)

    basex = 0


    # create two pipes for blitting on screen 

    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()


    upperPipes = [
         
         {'x': SCREEN_WIDTH+200, 'y':newPipe1[0]['y']},
         {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y':newPipe2[0]['y']}
    ]

    lowerPipes = [
         

         {'x': SCREEN_WIDTH+200, 'y':newPipe1[1]['y']},
         {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y':newPipe2[1]['y']}
         ]
    
    pipeVelx = -4

    playerVelY = -9

    playerMaxVely = 18

    playerMinVely = -8

    playerAccy = 1

    playerFlapAccv = -8
    playerFlapped = False


    while True:
         
         for event in pygame.event.get():
              
              if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                   pygame.quit()

                   sys.exit()

              if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                   
                   if playery > 5:
                        playerVelY = playerFlapAccv

                        playerFlapped = True
                        GAME_SOUND['wing'].play()

         crushTest = isCollide(playerx,playery,upperPipes,lowerPipes)
         if crushTest:
              
              return
         


         playerMidpos = playerx + GAME_SPRITES['player'].get_width()/2

         for pipe in upperPipes:
              
              pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2

              if pipeMidPos <= playerMidpos < pipeMidPos +4:
                   score += 1

                   print(f"your scroe {score} ")


                   GAME_SOUND['point'].play()
        
         if playerVelY < playerMaxVely and not playerFlapped:
              playerVelY += playerAccy

         if playerFlapped:
              
              playerFlapped = False
         
         playerHeight = GAME_SPRITES['player'].get_height()
         playery = playery + min(playerVelY, GROUND_Y - playery - playerHeight+100)

     #     playery = playery + playerVelY
     #     if playery >= GROUND_Y- playerHeight:
              
     #          return

         for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
              
              upperPipe['x'] += pipeVelx
              lowerPipe['x'] += pipeVelx

         if 0< upperPipe['x'] < 5:
              
              newpipe = getRandomPipe()

              upperPipes.append(newpipe[0])

              lowerPipes.append(newpipe[1])

         if upperPipe['x'] < - GAME_SPRITES['pipe'][0].get_width():

             upperPipe.pop(0)



             lowerPipe.pop(0)

         SCREEN.blit(GAME_SPRITES['background'])

         for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
              SCREEN.blit(GAME_SPRITES['pipe'][0],(upperPipe['x'],upperPipe['y']))
              SCREEN.blit(GAME_SPRITES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))


              


         SCREEN.blit(GAME_SPRITES['base'], (basex, GROUND_Y))

         SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
         mydigits = [int(x) for x in list(str(score))]

         width =0 

         sclar_factor = 0.25
         for digit in mydigits:
              width += (GAME_SPRITES['numbers'][digit].get_width())*sclar_factor

         Xoffset = (SCREEN_WIDTH- width)*0.5

         for digit in mydigits:
             img = GAME_SPRITES['numbers'][digit] #(Xoffset, SCREEN_HEIGHT*0.02))

             new_w = int(img.get_width()*sclar_factor)
             new_h = int(img.get_width()* sclar_factor)
             scaled_image = pygame.transform.smoothscale(img, (new_w, new_h))

             SCREEN.blit(scaled_image,(Xoffset,SCREEN_HEIGHT*0.12))

             Xoffset += new_w

         pygame.display.update()
         FPSCLOCK.tick(FPS)
         
         





def isCollide(playerx,playery,upperPipes,lowerPipes):

 

    

     if playery > GROUND_Y -25 or playery<0:
       GAME_SOUND['hit'].play()
       return True
     
     for pipe in upperPipes:

            pipeHeight = GAME_SPRITES['pipe'][0].get_height()
            if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width() ):
                return True

#      player_w = GAME_SPRITES['player'].get_width()
#      player_h = GAME_SPRITES['player'].get_height()
#      player_rect = pygame.Rect(playerx, playery, player_w, player_h)

#      pipe_w = GAME_SPRITES['pipe'][0].get_width()
#      pipe_h = GAME_SPRITES['pipe'][0].get_height()


#      pipe_rects = []

#      for pipe in upperPipes:
#         pipe_rects.append(pygame.Rect(pipe['x'], pipe['y'], pipe_w, pipe_h))
        
#      for pipe in lowerPipes:
#         pipe_rects.append(pygame.Rect(pipe['x'], pipe['y'], pipe_w, pipe_h))

#     t
#      if player_rect.collidelist(pipe_rects) != -1:
#         GAME_SOUND['hit'].play()  # Added sound trigger for pipe hits too
#         return True
     
           
     # for pipe in lowerPipes:
     #       pass


# def is isCollide()
         





def getRandomPipe():

         """

         this is for generating position of two pipes (one the bottom one and one the top one ) for blitting on the screen

         """

         pipeHeight = GAME_SPRITES['pipe'][0].get_height()

         offset = SCREEN_HEIGHT/3

         y2 = offset + random.randrange(0, int(SCREEN_HEIGHT- GAME_SPRITES['base'].get_height() - 1.2*offset))

         pipeX = SCREEN_WIDTH + 10

         y1 = pipeHeight - y2 + offset

         pipe = [
              
              {'x': pipeX, 'y':-y1},
              {'x':pipeX, 'y': y2}
         ]


         return pipe





    


if __name__ == "__main__":

    # this will be the main function where our game strarts

    pygame.init() # initilize by games modules 

    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy bird')

    GAME_SPRITES['numbers'] = (

        pygame.image.load('sprites/0.PNG').convert_alpha(),
        pygame.image.load('sprites/1.PNG').convert_alpha(),
        pygame.image.load('sprites/2.PNG').convert_alpha(),
        pygame.image.load('sprites/3.PNG').convert_alpha(),
        pygame.image.load('sprites/4.PNG').convert_alpha(),
        pygame.image.load('sprites/5.PNG').convert_alpha(),
        pygame.image.load('sprites/6.PNG').convert_alpha(),
        pygame.image.load('sprites/7.PNG').convert_alpha(),
        pygame.image.load('sprites/8.PNG').convert_alpha(),
        pygame.image.load('sprites/0.PNG').convert_alpha()

    )
    GAME_SPRITES['massage'] = pygame.image.load('sprites/interface.png').convert_alpha()

    GAME_SPRITES['base'] = pygame.image.load('sprites/base.png').convert_alpha()

    GAME_SPRITES['pipe'] = (
    
   pygame.transform.rotate( pygame.image.load(PIPE).convert_alpha(), 180),
    pygame.image.load(PIPE).convert_alpha()

    
    )

 # Game sounds

    GAME_SOUND['die'] = pygame.mixer.Sound('music/die.wav.mp3')
    GAME_SOUND['hit'] = pygame.mixer.Sound('music/hit.wave.mp3')
    GAME_SOUND['point'] = pygame.mixer.Sound('music/point.wav.mp3')
    GAME_SOUND['swoosh'] = pygame.mixer.Sound('music/swoosh.wav.mp3')
    GAME_SOUND['wing'] = pygame.mixer.Sound('music/wing.wav.mp3')


    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()

    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()


    while True:

        welcomeScreen()
        maingame()


