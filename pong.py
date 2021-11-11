# importing modules
import pygame
import random
# initializing pygame
pg = pygame
pg.init()

# loading the images
icon = pg.image.load('img/icon.png')
bg = pg.image.load('img/bg.png')
pause_i = pg.image.load('img/pause.png')
pause_2 = pg.image.load('img/pause_2.png')

# creating the screen
d = pg.display
s = d.set_mode((900,700))
d.set_caption('pong')
d.set_icon(icon)

# creating variables for colours
black = (0,0,0)
white = (200,200,200)
bright_white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
green = (0,200,0)
blue = (0,0,200)
bright_blue = (0,0,255)
yellow = (200,200,0)
bright_yellow = (255,255,0)
neon = (0,200,200)
bright_neon = (0,255,255)

# controling fps 
clock = pg.time.Clock()

# music and sound 
hit = pg.mixer.Sound('sounds/hit.wav')
music = pg.mixer.music.load('sounds/house_lo.mp3')

# creating the paddles
class paddle():
    def __init__(self,x,y,width,height,colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.xvel = 7
        self.yvel = 7
    #method for drawing the paddles
    def draw(self):
        pg.draw.rect(s,self.colour,(self.x,self.y,self.width,self.height))

# creating the ball

class ball():
    def __init__(self,x,y,radius,colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.xvel = 5
        self.yvel = 3
    #  method for drawing the balls
    def draw(self,s):
        pg.draw.circle(s,self.colour,(self.x,self.y),self.radius)


# making the buttons for the start menu
class button():
    def __init__(self,x,y,width,height,colour):
        self.x = x 
        self.y = y 
        self.width = width 
        self.height = height 
        self.colour = colour
    
    # drawing the buttons 
    def draw(self,s,text = "",font_size = 25):
        pg.draw.rect(s,self.colour,(self.x,self.y,self.width,self.height))
        if text != "":
                font = pg.font.Font('freesansbold.ttf',font_size)
                text = font.render(text, 1, (0,0,0))
                s.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
             return True

# displaying the score

def display_message(text,pos,size,colour= black):
    font = pg.font.Font('freesansbold.ttf',size)
    mytext = font.render(text,True,colour)
    s.blit(mytext,pos)

# function for collision
def collision1(paddlex,paddley,ballx,bally):
    if ballx <= paddlex  and ballx > 10 and bally >= paddley -1 and bally <= paddley + 101:
        return True
    else:
        return False

def collision2(paddlex,paddley,ballx,bally):
    if ballx >= paddlex and ballx < paddlex + 5 and bally >= paddley -1 and bally <= paddley + 101:
        return True
    else:
        return False

#initializing the paddles
paddle1 = paddle(10,350,25,100,white)
paddle2 = paddle(865,350,25,100,white)

# initializing the ball
ball = ball(450,350,10,black)

# function to  display instructions

def how_to_play():
    instructions = True
    menu = button(400,450,300,100,yellow)

    while instructions:

        pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                instructions= False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                if menu.is_over(pos):
                    instructions = False
            
        s.fill(white)
        menu.draw(s,"return back",30)
        display_message("Welcome to pong game",(220,0),45)
        display_message("To play this game vs computer click play vs computer",(0,45),32)
        display_message("in the main menu",(0,45+32),32)
        display_message("Move your padlle up and down using up and down arrow",(0,45+(2*32)),32)
        display_message("keys respectively",(0,45+(3*32)),32)
        display_message("when the ball goes behind the computers paddle your",(0,45+(4*32)),32)
        display_message("score increases by 10 points and vice versa",(0,45+(5*32)),32)
        display_message("To play with you friend on the same pc click on",(0,45+(6*32)),32)
        display_message("play vs friend",(0,45+(7*32)),32)
        display_message("The left paddle is moved using \"W\" and\"S\" Keys",(0,45+(8*32)),32)
        display_message("The other rules are Similar to computer mode",(0,45+(9*32)),32)

        if menu.is_over(pos):
            menu.colour= bright_yellow
        else:
            menu.colour = yellow
        

        d.update()
# making the pause button

def pause_func():
    pause = True
    
    resume =  button(210,210,380,50,white)
    quit_b = button(210,270,380,50,white) 
    return_start = button(210,330,380,50,white)
    how_to_play_b= button(210,390,380,50,white)
    
    while pause:
        pos = pg.mouse.get_pos()
    
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if resume.is_over(pos):
                    pg.mixer_music.play(-1)
                    pause = False
                if quit_b.is_over(pos):
                    pg.quit()
                    quit()
                if return_start.is_over(pos):
                    return "start"
                if how_to_play_b.is_over(pos):
                    how_to_play()             
                
        pg.draw.rect(s,black,(200,200,400,250))
        resume.draw(s,"Resume",40)
        quit_b.draw(s,"QUIT",40)
        return_start.draw(s,"return to main menu",38)
        how_to_play_b.draw(s,"how to play",40)
        
        if resume.is_over(pos):
            resume.colour = bright_white
        else:
            resume.colour = white
        
        if quit_b.is_over(pos):
            quit_b.colour = bright_white
        else:
            quit_b.colour = white
        
        if return_start.is_over(pos):
            return_start.colour = bright_white
        else:
            return_start.colour = white
        
        if how_to_play_b.is_over(pos):
            how_to_play_b.colour = bright_white
        else:
            how_to_play_b.colour = white
        
        d.update()


def main(scorea,scoreb):
    # game loop 
    run = True
    pause_b = button(10,640,50,50,blue)
    pg.mixer.music.play(-1)
    while run:
        pos = pg.mouse.get_pos()

        # for loop to check for events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.mixer.music.stop()
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if pause_b.is_over(pos):
                    pg.mixer.music.stop()
                    if pause_func() == "start":
                        run = False
                    
        # drawing the background
        s.blit(bg,(0,0))
        

        # paddle movement
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] and paddle2.y >5:
            paddle2.y-=paddle2.yvel

        if keys[pg.K_DOWN] and paddle2.y < 595:
            paddle2.y+=paddle2.yvel

        if keys[pg.K_w] and paddle1.y > 5:
            paddle1.y-=paddle1.yvel

        if keys[pg.K_s] and paddle1.y < 595:
            paddle1.y+=paddle1.yvel

        # ball movement
        ball.x+=ball.xvel
        ball.y+=ball.yvel

        # ball bouncing 
        if ball.y >=690:
            ball.yvel*=-1
        
        if ball.y<=0:
            ball.yvel*=-1

        # score
        if ball.x > 890:
            ball.x = 450
            ball.y = 350
            ball.xvel*=-1
            ball.yvel*=-1
            scorea+=10
            
        if ball.x <0:
            ball.x = 450
            ball.y = 350
            ball.xvel*=-1
            scoreb+=10

        display_message('player A:' + str(scorea) + ' Player B:' + str(scoreb),(250,10),35)

        # collision 
        if collision1(paddle1.x+paddle1.width,paddle1.y,ball.x,ball.y):
            ball.xvel*=-1
            pg.mixer.Sound.play(hit)

        if collision2(paddle2.x,paddle2.y,ball.x,ball.y):
            ball.xvel*=-1
            pg.mixer.Sound.play(hit)

        #drawing the paddles
        paddle1.draw()
        paddle2.draw()

        #drawing the ball 
        ball.draw(s)

        # drawing the pause button
        if pause_b.is_over(pos):
            s.blit(pause_2,(pause_b.x,pause_b.y))
        else:
            s.blit(pause_i,(pause_b.x,pause_b.y))

        
        # updating the screen
        d.update()
        clock.tick(65)

def play_with_computer(scorea,scoreb):
    run = True
    pg.mixer.music.play(-1)
    down = False
    pause_b = button(10,640,50,50,blue)
    no_of_hits = 0

    while run:
        pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.mixer.music.stop()
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pause_b.is_over(pos):
                    pg.mixer.music.stop()
                    if pause_func() == "start":
                        run = False
        
        # drawing the background
        s.blit(bg,(0,0))
        
        # paddle movement
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] and paddle2.y >5:
            paddle2.y-=paddle2.yvel

        if keys[pg.K_DOWN] and paddle2.y < 595:
            paddle2.y+=paddle2.yvel
        
        # ball movement
        ball.x+=ball.xvel
        ball.y+=ball.yvel

        # ball bouncing 
        if ball.y >=690:
            ball.yvel*=-1
        if ball.y<=0:
            ball.yvel*=-1

        # score
        if ball.x > 890:
            ball.x = 450
            ball.y = 350
            ball.xvel*=-1
            ball.yvel*=-1
            scorea+=10
            
        if ball.x <0:
            ball.x = 450
            ball.y = 350
            ball.xvel*=-1
            scoreb+=10

        display_message('computer:' + str(scorea) + ' player:' + str(scoreb),(250,10),35)

        # collision 
        if collision1(paddle1.x+paddle1.width,paddle1.y,ball.x,ball.y):
            ball.xvel*=-1
            pg.mixer.Sound.play(hit)
            no_of_hits+=1
        
        if collision2(paddle2.x,paddle2.y,ball.x,ball.y):
            ball.xvel*=-1
            pg.mixer.Sound.play(hit)
            no_of_hits+=1
        
        #AI
        if no_of_hits%7 != 0 or no_of_hits==0 :
            paddle1.yvel=7
            if paddle1.y +random.randint(0,100) < ball.y and paddle1.y <= 600:
                paddle1.y+=paddle1.yvel
                down = True

            if paddle1.y + random.randint(0,100) > ball.y:
                paddle1.y -=paddle1.yvel
                down = False

        # small glitch to let our player win 
        else:
            
            if down == True and paddle1.y <= 600:
                paddle1.y+=paddle1.yvel
            
            if down == False and paddle1.y >= 0 :
                paddle1.y-=paddle1.yvel
            
            if paddle1.y <= 0:
                down = True
            
            if paddle1.y >=600:
                down = False            
            
        #drawing the paddles
        paddle1.draw()
        paddle2.draw()

        #drawing the ball 
        ball.draw(s)


        #drawing the pause button
        
        if pause_b.is_over(pos):
            s.blit(pause_2,(pause_b.x,pause_b.y))
        else:
            s.blit(pause_i,(pause_b.x,pause_b.y))
        
        # updating the screen
        d.update()
        clock.tick(65)
    


# function for start menu
def start():
    
    # initializing buttons
    play_friend = button(500,250,300,50,red)
    play_computer = button(500,100,300,50,blue)
    Quit = button(500,400,300,50,green)
    instructions = button(500,550,300,50,neon)
    
    start = True
    while start:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                start = False
        s.fill(white)
        pos = pg.mouse.get_pos()
                
        # drawing the buttons 
        play_friend.draw(s,"Play vs friend",40)
        Quit.draw(s,"Quit",40)
        play_computer.draw(s,"Play vs computer",35)
        instructions.draw(s,"How to play",40)

        # changing button colour if mouse is over the play_friend button
        if play_friend.is_over(pos):
            play_friend.colour = bright_red
        else:
            play_friend.colour = red
        
        # changing quit button colour if mouse is over it
        if Quit.is_over(pos):
            Quit.colour = bright_green
        else:
            Quit.colour = green

        # changing play_computer button colour if mouse is over it
        if play_computer.is_over(pos):
            play_computer.colour = bright_blue
        else:
            play_computer.colour = blue
        
        # changing instructions button colour if mouse is over it
        if instructions.is_over(pos):
            instructions.colour = bright_neon
        else:
            instructions.colour = neon
        
        # checking if buttons are clicked 
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if play_friend.is_over(pos):
                    main(0,0)
                elif Quit.is_over(pos):
                    pg.quit()
                    quit()
                    
                elif instructions.is_over(pos):
                    how_to_play()
                elif play_computer.is_over(pos):
                    play_with_computer(0,0)

        display_message("pong",(0,200),200,neon)
        d.update()

start()
