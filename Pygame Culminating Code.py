import pygame, sys
from pygame.locals import QUIT
pygame.init()

#starting page function

def startingPage(screen, background):
    
    #load background
    background = pygame.image.load("startingPage.png")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #draw start clickable button
    pygame.draw.rect(background, (245, 236, 213), [130, 290, 380, 90], 0)
    
    #start labels
    instructionLabel = myTitleFont.render("Click Here to Begin", False, (0, 0, 0))
    nameLabel = myButtonFont.render("Enter Your Name And Press Enter!", False, (255, 255, 255))
    
    #input surface
    name_surf = pygame.Surface((380, 50)).convert()
    name_surf.fill((245,236,213))
    name_value = ""
    name = myTextFont.render(name_value, True, (0,0,0))
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(instructionLabel, (140, 300))
    screen.blit(nameLabel, (130, 150))
    screen.blit(name_surf, (130, 200))
    screen.blit(name, (140, 205))
    pygame.display.flip()

#show game story
    
def gameStory(screen, background):
    
    #setting fonts
    myTitleFont = pygame.font.SysFont("helvetica", 50)
    myButtonFont = pygame.font.SysFont("helvetica", 35)
    myTextFont = pygame.font.SysFont("helvetica", 20)
    
    #load background
    background = pygame.image.load("gameStory.png")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #getting name from file
    file = open("name.txt" , "r")
    playerName = file.read()
    file.close()
    
    #start labels
    instructionLabel = myButtonFont.render("Go To Space", False, (0, 0, 0))
    addressUserLabel = myButtonFont.render("Dear, ", False, (255, 255, 255))
    playerNameLabel = myButtonFont.render(playerName, False, (255, 255, 255))
    
    #draw start clickable button
    pygame.draw.rect(background, (245, 236, 213), [130, 230, 380, 50], 0)
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(instructionLabel, (240, 235))
    screen.blit(addressUserLabel, (100, 50))
    screen.blit(playerNameLabel, (175, 50))
    pygame.display.flip()

#show the first planet story

def introStory(screen, background):
    
    #load background
    background = pygame.image.load("intro.png")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #setting fonts
    myTitleFont = pygame.font.SysFont("helvetica", 50)
    myButtonFont = pygame.font.SysFont("helvetica", 35)
    myTextFont = pygame.font.SysFont("helvetica", 25)
    
    #getting name from file
    file = open("name.txt" , "r")
    playerName = file.read()
    file.close()
    
    #text 
    playerNameLabel = myTextFont.render(playerName, False, (255, 255, 255))
    mapLabel = myTextFont.render("Back To Map", False, (0, 0, 0))
    continueLabel = myTextFont.render("Continue!", False, (0, 0, 0))
    
    #back to map button and continue button
    pygame.draw.rect(background, (221, 192, 237), [250, 400, 150, 50], 0)
    pygame.draw.rect(background, (192, 237, 214), [410, 400, 150, 50], 0)
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(playerNameLabel, (45, 110))
    screen.blit(mapLabel, (265, 410))
    screen.blit(continueLabel, (440, 410))
    pygame.display.flip()

#going to page one function

def goToPage1(screen, background):
    
    #load background
    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #setting fonts
    myTitleFont = pygame.font.SysFont("helvetica", 50)
    myButtonFont = pygame.font.SysFont("helvetica", 35)
    myTextFont = pygame.font.SysFont("helvetica", 20)
    
    #back to map button
    pygame.draw.rect(background, (221, 192, 237), [320, 25, 300, 50], 0)
    
    #title box
    pygame.draw.rect(background, (237, 178, 181), [20, 25, 290, 50], 0)
    
    #question one box
    pygame.draw.rect(background, (245, 236, 213), [20, 100, 200, 180], 0)
    
    #question two box
    pygame.draw.rect(background, (245, 236, 213), [20, 290, 200, 180], 0)
    
    #question files
    fileOne = open("pageOneQuestionOne.txt" , "r")
    questionOne = fileOne.read()
    fileOne.close()
    
    fileTwo = open("pageOneQuestionTwo.txt" , "r")
    questionTwo = fileTwo.read()
    fileTwo.close()
    
    #text for title and back to map button
    titleLabel = myTitleFont.render("Click To Reveal", False, (0, 0, 0))
    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
    questionOneLabel = myTextFont.render(questionOne, False, (0, 0, 0))
    questionTwoLabel = myTextFont.render(questionTwo, False, (0, 0, 0))
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(titleLabel, (20, 20))
    screen.blit(backButtonLabel, (370, 30))
    screen.blit(questionOneLabel, (25, 105))
    screen.blit(questionTwoLabel, (25, 290))
    pygame.display.flip()

#intro to true or false

def trueOrFalseIntro(screen, background):
    
    #load background
    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #getting name from file
    file = open("name.txt" , "r")
    playerName = file.read()
    file.close()
    
    #buttons
    pygame.draw.rect(background, (221, 192, 237), [40, 400, 250, 50], 0)
    pygame.draw.rect(background, (192, 237, 214), [310, 400, 250, 50], 0)
    
    #title, text, and button labels
    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
    continueLabel = myButtonFont.render("Let's Go!", False, (0, 0, 0))
    playerNameLabel = myTextFont.render(playerName, False, (0, 0, 0))
    
    #load alien
    alienTwo = pygame.image.load("alienTwo.png")
    alienTwo = pygame.transform.scale(alienTwo, (480,290))
    alienTwo = alienTwo.convert()
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(alienTwo, (40, 40))
    screen.blit(backButtonLabel, (80, 400))
    screen.blit(continueLabel, (340, 400))
    screen.blit(playerNameLabel, (150, 63))
    pygame.display.flip()

#going to page two function
            
def goToPage2(screen, background):
    
    #load background
    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #setting fonts
    myTitleFont = pygame.font.SysFont("helvetica", 50)
    myButtonFont = pygame.font.SysFont("helvetica", 35)
    myTextFont = pygame.font.SysFont("helvetica", 20)
    
    #title, text, and button labels
    titleLabel = myTitleFont.render("True or False?", False, (0, 0, 0))
    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
    trueLabel = myTextFont.render("True", False, (0, 0, 0))
    falseLabel = myTextFont.render("False", False, (0, 0, 0))
    
    #title box
    pygame.draw.rect(background, (237, 178, 181), [20, 25, 290, 50], 0)
    
    #question boxes
    pygame.draw.rect(background, (221, 192, 237), [320, 25, 300, 50], 0)
    pygame.draw.rect(background, (245, 236, 213), [20, 100, 200, 180], 0)
    pygame.draw.rect(background, (245, 236, 213), [225, 100, 200, 180], 0)
    pygame.draw.rect(background, (245, 236, 213), [430, 100, 200, 180], 0)
    
    #True and false boxes
    pygame.draw.rect(background, (237, 192, 216), [20, 300, 95, 50], 0)
    pygame.draw.rect(background, (192, 237, 214), [120, 300, 95, 50], 0)
    
    pygame.draw.rect(background, (237, 192, 216), [225, 300, 95, 50], 0)
    pygame.draw.rect(background, (192, 237, 214), [325, 300, 95, 50], 0)
    
    pygame.draw.rect(background, (237, 192, 216), [430, 300, 95, 50], 0)
    pygame.draw.rect(background, (192, 237, 214), [530, 300, 95, 50], 0)
    
    #True and false question files
    fileOne = open("pageTwoQuestionOne.txt" , "r")
    questionOne = fileOne.read()
    fileOne.close()
    
    fileTwo = open("pageTwoQuestionTwo.txt" , "r")
    questionTwo = fileTwo.read()
    fileTwo.close()
    
    fileThree = open("pageTwoQuestionThree.txt" , "r")
    questionThree = fileThree.read()
    fileThree.close()
    
    #True or false question labels
    questionOne = myTextFont.render(questionOne, False, (0, 0, 0))
    questionTwo = myTextFont.render(questionTwo, False, (0, 0, 0))
    questionThree = myTextFont.render(questionThree, False, (0, 0, 0))
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(titleLabel, (20, 20))
    screen.blit(backButtonLabel, (370, 30))
    screen.blit(questionOne, (25, 110))
    screen.blit(questionTwo, (230, 110))
    screen.blit(questionThree, (435, 110))
    screen.blit(trueLabel, (50, 310))
    screen.blit(trueLabel, (255, 310))
    screen.blit(trueLabel, (460, 310))
    screen.blit(falseLabel, (150, 310))
    screen.blit(falseLabel, (355, 310))
    screen.blit(falseLabel, (560, 310))
    pygame.display.flip()

#going to page three function
            
def goToPage3(screen, background):
    
    #load background
    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #setting fonts
    myTitleFont = pygame.font.SysFont("helvetica", 50)
    myButtonFont = pygame.font.SysFont("helvetica", 35)
    myMessageFont = pygame.font.SysFont("helvetica", 24)
    myTextFont = pygame.font.SysFont("helvetica", 20)
    
    #getting name from file
    file = open("name.txt" , "r")
    playerName = file.read()
    file.close()
    
    #load alien
    alien = pygame.image.load("alienStoryMessage.png")
    alien = pygame.transform.scale(alien, (480,290))
    alien = alien.convert()
    
    #title, text, and button labels
    titleLabel = myTitleFont.render("Choose a story!", False, (0, 0, 0))
    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
    storyOneButtonLabel = myButtonFont.render("Story One", False, (0, 0, 0))
    storyTwoButtonLabel = myButtonFont.render("Story Two", False, (0, 0, 0))
    greetingLabel = myMessageFont.render("Hello, ", False, (0, 0, 0))
    playerNameLabel = myMessageFont.render(playerName, False, (0, 0, 0))
    messageLabel = myMessageFont.render("Welcome to planet X53IO4! Choose a \ntraditional story we tell about social media!", False, (0, 0, 0))
    
    #back to map button and title box
    pygame.draw.rect(background, (237, 178, 181), [20, 25, 290, 50], 0)
    pygame.draw.rect(background, (221, 192, 237), [320, 25, 300, 50], 0)
    
    #story buttons
    pygame.draw.rect(background, (237, 192, 216), [40, 400, 250, 50], 0)
    pygame.draw.rect(background, (192, 237, 214), [310, 400, 250, 50], 0)

    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(titleLabel, (20, 20))
    screen.blit(backButtonLabel, (370, 30))
    screen.blit(storyOneButtonLabel, (80, 400))
    screen.blit(storyTwoButtonLabel, (340, 400))
    screen.blit(alien, (80, 95))
    screen.blit(greetingLabel, (140, 110))
    screen.blit(playerNameLabel, (195, 110))
    screen.blit(messageLabel, (140, 150))
    pygame.display.flip()
    
#going to page four function
            
def goToPage4(screen, background):
    
    #load background
    background = pygame.image.load("galaxy.jpg")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #setting fonts 
    myTitleFont = pygame.font.SysFont("helvetica", 50)
    myButtonFont = pygame.font.SysFont("helvetica", 30)
    myTextFont = pygame.font.SysFont("helvetica", 20)
    
    #title, button, and text labels
    titleLabel = myTitleFont.render("Experience", False, (0, 0, 0))
    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
    endButtonLabel = myButtonFont.render("End", False, (0, 0, 0))
    promptLabel = myTextFont.render(" Rate the Experience! (Around 30 Characters! This is kept to improve our site!)", False, (255, 255, 255))
    
    #back to map and end button
    pygame.draw.rect(background, (221, 192, 237), [310, 25, 160, 50], 0)
    pygame.draw.rect(background, (237, 178, 181), [20, 25, 210, 50], 0)
    pygame.draw.rect(background, (192, 226, 237), [480, 25, 150, 50], 0)

    #input surface
    field_surf = pygame.Surface((600, 50)).convert()
    field_surf.fill((245,236,213))
    field_value = ""
    field = myTextFont.render(field_value, True, (0,0,0))

    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(titleLabel, (20, 20))
    screen.blit(backButtonLabel, (323, 30))
    screen.blit(endButtonLabel, (530, 30))
    screen.blit(promptLabel, (20, 110))
    screen.blit(field_surf, (20, 150))
    screen.blit(speechBubble, (20, 220))
    screen.blit(field, (30, 155))
    pygame.display.flip()

#end game screen function

def endGame(screen, background):
    #load background
    background = pygame.image.load("endGame.png")
    background = pygame.transform.scale(background, (640,480))
    background = background.convert()
    
    #getting name from file
    file = open("name.txt" , "r")
    playerName = file.read()
    file.close()
    
    #draw end clickable button
    pygame.draw.rect(background, (245, 236, 213), [130, 290, 380, 90], 0)
    
    #end labels
    endLabel = myTitleFont.render("Thank You For Playing!", False, (255, 255, 255))
    instructionLabel = myTitleFont.render("Click Here to Exit", False, (0, 0, 0))
    addressUserLabel = myButtonFont.render("Dear, ", False, (255, 255, 255))
    playerNameLabel = myButtonFont.render(playerName, False, (255, 255, 255))
    
    #blit to screen
    screen.blit(background, (0, 0))
    screen.blit(endLabel, (100, 100))
    screen.blit(instructionLabel, (140, 300))
    screen.blit(addressUserLabel, (100, 50))
    screen.blit(playerNameLabel, (175, 50))
    pygame.display.flip()

#setting screen, caption, background, and fonts
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Culminating.")

colourBackground = pygame.Surface(size).convert()
colourBackground.fill((100,100,100))
background = pygame.image.load("galaxy.jpg")
background = pygame.transform.scale(background, (640,480))
background = background.convert()

myTitleFont = pygame.font.SysFont("helvetica", 50)
myButtonFont = pygame.font.SysFont("helvetica", 30)
myTextFont = pygame.font.SysFont("helvetica", 20)

#map title
mapTitleLabel = myButtonFont.render("Media Void! Use The Arrow Keys To Move!", False, (255, 255, 255))

#background music
pygame.mixer.music.load("1pm.mid")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

#making the rectangles, planets and avatar for map as well as x and y coordinates for avatar
blueRectangle = pygame.Rect(535,362,80,120)
redRectangle = pygame.Rect(400, 350, 100, 100)
greenRectangle = pygame.Rect(150, 290, 100, 100)
yellowRectangle = pygame.Rect(320, 50, 100, 100)
purpleRectangle = pygame.Rect(20, 50, 100, 100)

blueRectangle_x = 535
blueRectangle_y = 362

planet = pygame.image.load("planet.png")
planet = pygame.transform.scale(planet, (100, 100))
planet = planet.convert()

planet2 = pygame.image.load("planet2.png")
planet2 = pygame.transform.scale(planet2, (100, 100))
planet2 = planet2.convert()

planet3 = pygame.image.load("planet3.png")
planet3 = pygame.transform.scale(planet3, (100, 100))
planet3 = planet3.convert()

planet4 = pygame.image.load("planet4.png")
planet4 = pygame.transform.scale(planet4, (100, 100))
planet4 = planet4.convert()

astro = pygame.image.load("astro.png")
astro = pygame.transform.scale(astro, (80, 120))
astro = astro.convert()

#stars on planets
stars = pygame.image.load("stars1.png")
stars = pygame.transform.scale(stars, (150, 150))

stars2 = pygame.image.load("stars2.png")
stars2 = pygame.transform.scale(stars2, (150, 150))

stars22 = pygame.image.load("stars2.png")
stars22 = pygame.transform.scale(stars22, (150, 150))

stars3 = pygame.image.load("stars3.png")
stars3 = pygame.transform.scale(stars3, (100, 100))

stars4 = pygame.image.load("stars.png")
stars4 = pygame.transform.scale(stars4, (150, 150))

pygame.draw.rect(colourBackground, (0, 0, 255), blueRectangle, 0)
pygame.draw.rect(colourBackground, (255, 0, 0), redRectangle, 0)
pygame.draw.rect(colourBackground, (0, 255, 0), greenRectangle, 0)
pygame.draw.rect(colourBackground, (255, 255, 0), yellowRectangle, 0)
pygame.draw.rect(colourBackground, (255,0,255), purpleRectangle, 0)

#loading images/songs and declaring variables for the activities
check = pygame.image.load("check mark.png")
check = pygame.transform.scale(check, (100,100))
check = check.convert()

wrong = pygame.image.load("wrong.jpg")
wrong = pygame.transform.scale(wrong, (100,100))
wrong = wrong.convert()

speechBubble = pygame.image.load("speech bubble.png")
speechBubble = pygame.transform.scale(speechBubble, (600,250))
speechBubble = speechBubble.convert()

story1 = pygame.image.load("Story1.png")
story1 = pygame.transform.scale(story1, (600,380))
story1 = story1.convert()

story2 = pygame.image.load("Story2.png")
story2 = pygame.transform.scale(story2, (600,380))
story2 = story2.convert()

field_value = ""

name_value = ""

viewedStory = "No"

answeredQuestionOne = "No"
answeredQuestionTwo = "No"
answeredQuestionThree = "No"

planetSound = pygame.mixer.Sound("enter planet.mp3")
rightSound = pygame.mixer.Sound("right.mp3")
wrongSound = pygame.mixer.Sound("wrong.mp3")
story1Sound = pygame.mixer.Sound("facebook.mp3")
story1Sound.set_volume(1.0)
story2Sound = pygame.mixer.Sound("ryan.mp3")
story2Sound.set_volume(1.0)

#starting page number and previous position
pageNumber = -1
prevPosition = 0

#blit screen and set clock
screen.blit(colourBackground, (0, 0))
screen.blit(background, (0,0))
screen.blit(planet, (400, 350))
screen.blit(planet2, (150, 290))
screen.blit(planet3, (320, 50))
screen.blit(planet4, (20, 50))
screen.blit(stars, (380, 330))
screen.blit(stars2, (130, 270))
screen.blit(stars3, (320, 50))
screen.blit(stars22, (300, 30))
screen.blit(stars4, (0, 30))
screen.blit(astro, (blueRectangle_x, blueRectangle_y))
screen.blit(mapTitleLabel, (60, 6))
pygame.display.flip()
clock = pygame.time.Clock()

#main code - while true loop

while True:
    
    #determine which page to go to
        
    if pageNumber == -1 and prevPosition == 0:
        startingPage(screen, background)
    
    if pageNumber == -2 and prevPosition == 0:
        gameStory(screen, background)
    
    if pageNumber == 0.5 and prevPosition == 0:
        introStory(screen, background)
        
    if pageNumber == 1 and prevPosition == 0:
        goToPage1(screen, background)
        
    if pageNumber == 1.5 and prevPosition == 0:
        trueOrFalseIntro(screen, background)
    
    if pageNumber == 2 and prevPosition == 0:
        goToPage2(screen, background)

    if pageNumber == 3 and prevPosition == 0:
        goToPage3(screen, background)
    
    if pageNumber == 4 and prevPosition == 0:
        goToPage4(screen, background)
        
    clock.tick(30)
    
    for event in pygame.event.get():
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        #if the user clicks on a button
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = event.pos[0]
            y = event.pos[1]
            
            #if user clicks on a button on the starting page      
            
            if pageNumber == -1:
                
                #if user clicks on begin button
                
                if x >=130 and x <= 510 and y >= 290 and y <= 380:
                    
                    pageNumber = -2
                    prevPosition = 0
                    
            #if user clicks on a button on the starting page      
            
            if pageNumber == -2:
                
                #if user clicks on begin button
                
                if x >=130 and x <= 510 and y >= 230 and y <= 280: 
                    
                    pageNumber = 0
                    prevPosition = 0
            
            #if the user clicks on a button in the map
                    
            if pageNumber == 0:
                
                #if the user clicks on the end game button
                
                if x >= 20 and x <= 220 and y >= 400 and y <= 450:
                    #go to end game screen and set page number to 5
                    endGame(screen, background)
                    pageNumber = 5
            
            #if the user clicks on the social media intro story page
            
            if pageNumber == 0.5:
                
                #if the user clicks on the back to map button
            
                if x >=250 and x <= 400 and y >= 400 and y <= 450:
                    pageNumber = 0
                    prevPosition = 0
                    blueRectangle_x = 490
                    blueRectangle_y = 220
                    blueRectangle.x = 490
                    blueRectangle.y = 220
                    
                #if the user clicks on the continue button
                    
                if x >= 410 and x <= 560 and y >= 400 and y <= 450:
                    pageNumber = 1
                    prevPosition = 0
            
            #if the user clicks on a button in page one
            
            if pageNumber == 1:
            
                #if the user clicks on the back to map button
            
                if x >=320 and x <= 620 and y >= 25 and y <= 75:
                    #set previous position and new x and y coordinates
                    pageNumber = 0
                    prevPosition = 0
                    blueRectangle_x = 490
                    blueRectangle_y = 220
                    blueRectangle.x = 490
                    blueRectangle.y = 220
                
                #if the user clicks on the first question - reveal answer
                
                if x >=20 and x <= 220 and y >= 100 and y <= 280:
                    #set previous position, fonts, read answer file
                    prevPosition = 1
                    myTitleFont = pygame.font.SysFont("helvetica", 50)
                    myButtonFont = pygame.font.SysFont("helvetica", 35)
                    myTextFont = pygame.font.SysFont("helvetica", 20)
                    myAnswerFont = pygame.font.SysFont("helvetica", 15)

                    file = open("Text file.txt" , "r")
                    contents = file.read()
                    file.close()
                    
                    #background
                    background = pygame.image.load("galaxy.jpg")
                    background = pygame.transform.scale(background, (640,480))
                    background = background.convert()
                    
                    #back to map button
                    pygame.draw.rect(background, (221, 192, 237), [320, 25, 300, 50], 0)
                    
                    #question one box
                    pygame.draw.rect(background, (245, 236, 213), [20, 100, 200, 180], 0)
                    
                    #question two box
                    pygame.draw.rect(background, (245, 236, 213), [20, 290, 200, 180], 0)
                    
                    #question files
                    fileOne = open("pageOneQuestionOne.txt" , "r")
                    questionOne = fileOne.read()
                    fileOne.close()
                    
                    fileTwo = open("pageOneQuestionTwo.txt" , "r")
                    questionTwo = fileTwo.read()
                    fileTwo.close()
                    
                    #text for title and back to map button
                    titleLabel = myTitleFont.render("Click To Reveal", False, (0, 0, 0))
                    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
                    answerLabel = myAnswerFont.render(contents, False, (0, 0, 0))
                    questionOneLabel = myTextFont.render(questionOne, False, (0, 0, 0))
                    questionTwoLabel = myTextFont.render(questionTwo, False, (0, 0, 0))
                    
                    #title box
                    pygame.draw.rect(background, (237, 178, 181), [20, 25, 290, 50], 0)
                    
                    #answer one box
                    pygame.draw.rect(background, (245, 236, 213), [245, 100, 383, 180], 0)
                    
                    #blit to screen
                    screen.blit(background, (0, 0))
                    screen.blit(titleLabel, (20, 20))
                    screen.blit(backButtonLabel, (370, 30))
                    screen.blit(questionOneLabel, (25, 105))
                    screen.blit(questionTwoLabel, (25, 290))
                    screen.blit(answerLabel, (251, 110))
                    pygame.display.flip()
                
                #if the user clicks on the second question - reveal answer
                
                if x >=20 and x <= 220 and y >= 290 and y <= 470:
                    #set previous page and fonts as well as read answer file
                    prevPosition = 1
                    myTitleFont = pygame.font.SysFont("helvetica", 50)
                    myButtonFont = pygame.font.SysFont("helvetica", 35)
                    myTextFont = pygame.font.SysFont("helvetica", 20)
                    myAnswerFont = pygame.font.SysFont("helvetica", 15)

                    file = open("answer2.txt" , "r")
                    contents = file.read()
                    file.close()
                    
                    #background
                    background = pygame.image.load("galaxy.jpg")
                    background = pygame.transform.scale(background, (640,480))
                    background = background.convert()
                    
                    #back to map button
                    pygame.draw.rect(background, (221, 192, 237), [320, 25, 300, 50], 0)
                    
                    #question one box
                    pygame.draw.rect(background, (245, 236, 213), [20, 100, 200, 180], 0)
                    
                    #question two box
                    pygame.draw.rect(background, (245, 236, 213), [20, 290, 200, 180], 0)
                    
                    #question files
                    fileOne = open("pageOneQuestionOne.txt" , "r")
                    questionOne = fileOne.read()
                    fileOne.close()
                    
                    fileTwo = open("pageOneQuestionTwo.txt" , "r")
                    questionTwo = fileTwo.read()
                    fileTwo.close()
                    
                    #title box
                    pygame.draw.rect(background, (237, 178, 181), [20, 25, 290, 50], 0)
                    
                    #text for title and back to map button
                    titleLabel = myTitleFont.render("Click To Reveal", False, (0, 0, 0))
                    backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
                    
                    #answer two box
                    pygame.draw.rect(background, (245, 236, 213), [250, 290, 373, 180], 0)
                    questionOneLabel = myTextFont.render(questionOne, False, (0, 0, 0))
                    questionTwoLabel = myTextFont.render(questionTwo, False, (0, 0, 0))
                    answerLabel = myAnswerFont.render(contents, False, (0, 0, 0))
                    
                    #blit to screen
                    screen.blit(background, (0, 0))
                    screen.blit(titleLabel, (20, 20))
                    screen.blit(backButtonLabel, (370, 30))
                    screen.blit(questionOneLabel, (25, 105))
                    screen.blit(questionTwoLabel, (25, 290))
                    screen.blit(answerLabel, (255, 300))
                    pygame.display.flip()
            
            #if the user clicks ona button in the true or false story page
                    
            if pageNumber == 1.5:    
                    
                #if the user clicks on the back to map button
                
                if x >= 40 and x <= 290 and y >= 400 and y <= 450:
                    #set previous page number and x and y coordinates
                    pageNumber = 0
                    prevPosition = 0
                    blueRectangle_x = 40
                    blueRectangle_y = 250
                    blueRectangle.x = 40
                    blueRectangle.y = 250
                    
                #if the user clicks in the continue button
                
                if x >= 310 and x <= 560 and y >= 400 and y <= 450:
                    prevPosition = 0
                    pageNumber = 2
            
            #if the user clicks on a button in page two
                
            if pageNumber == 2:    
                    
                #if the user clicks on the back to map button
                
                if x >=320 and x <= 620 and y >= 25 and y <= 75:
                    #set previous page number and x and y coordinates
                    pageNumber = 0
                    prevPosition = 0
                    blueRectangle_x = 40
                    blueRectangle_y = 250
                    blueRectangle.x = 40
                    blueRectangle.y = 250
                
                #if the user clicks on the first true button
                
                if x >=20 and x <= 115 and y >= 300 and y <= 350 and answeredQuestionOne == "No":
                    prevPosition = 2
                    screen.blit(check, (20, 370))
                    pygame.display.flip()
                    rightSound.play()
                    answeredQuestionOne = "Yes"
                
                #if the user clicks on the first false button
                
                elif x >=120 and x <= 215 and y >= 300 and y <= 350 and answeredQuestionOne == "No":
                    prevPosition = 2
                    screen.blit(wrong, (120, 370))
                    pygame.display.flip()
                    wrongSound.play()
                    answeredQuestionOne = "Yes"
                
                #if the user clicks on the second true button
                
                if x >=225 and x <= 320 and y >= 300 and y <= 350 and answeredQuestionTwo == "No":
                    prevPosition = 2
                    screen.blit(wrong, (225, 370))
                    pygame.display.flip()
                    wrongSound.play()
                    answeredQuestionTwo = "Yes"
                    
                #if the user clicks on the second false button
                    
                elif x >=325 and x <= 420 and y >= 300 and y <= 350 and answeredQuestionTwo == "No":
                    prevPosition = 2
                    screen.blit(check, (325, 370))
                    pygame.display.flip()
                    rightSound.play()
                    answeredQuestionTwo = "Yes"
                    
                #if the user clicks on the third true button
                    
                if x >=430 and x <= 525 and y >= 300 and y <= 350 and answeredQuestionThree == "No":
                    prevPosition = 2
                    screen.blit(check, (430, 370))
                    pygame.display.flip()
                    rightSound.play()
                    answeredQuestionThree = "Yes"
                    
                #if the user clicks on the third false button
                    
                elif x >=530 and x <= 625 and y >= 300 and y <= 350 and answeredQuestionThree == "No":
                    prevPosition = 2
                    screen.blit(wrong, (530, 370))
                    pygame.display.flip()
                    wrongSound.play()
                    answeredQuestionThree = "Yes"
            
            #if the user clicks on a button in page three
            
            if pageNumber == 3:
            
                #if the user clicks on the back to map button
                
                if x >=320 and x <= 620 and y >= 25 and y <= 75:
                    #set previous page number and x and y coordinates
                    pageNumber = 0
                    prevPosition = 0
                    blueRectangle_x = 200
                    blueRectangle_y = 50
                    blueRectangle.x = 200
                    blueRectangle.y = 50
                    
                    #stop the story audio
                    story1Sound.stop()
                    story2Sound.stop()
                    pygame.mixer.music.unpause()
                    
                #if the user clicks on the story one box
                
                if x >= 40 and x <= 290 and y >= 400 and y <= 450 and viewedStory == "No":
                    prevPosition = 3
                    screen.blit(story1, (20, 86))
                    pygame.display.flip()
                    viewedStory = "Yes"
                    
                    #story audio file
                    pygame.mixer.music.pause()
                    story1Sound.play()
                    
                #if the user clicks on the story two box
                
                if x >= 310 and x <= 560 and y >= 400 and y <= 450 and viewedStory == "No":
                    prevPosition = 3
                    screen.blit(story2, (20, 86))
                    pygame.display.flip()
                    viewedStory = "Yes"
                    
                    #story audio file
                    pygame.mixer.music.pause()
                    story2Sound.play()
            
            #if the user clicks on a button in page four
            
            if pageNumber == 4:
            
                #if the user clicks on the back to map button
            
                if x >=310 and x <= 470 and y >= 25 and y <= 75:
                    #set previous page number and x and y coordinates
                    pageNumber = 0
                    prevPosition = 0
                    blueRectangle_x = 40
                    blueRectangle_y = 160
                    blueRectangle.x = 40
                    blueRectangle.y = 160
                
                #if the user clicks on the end button
                
                if x >= 480 and x <= 630 and y >= 25 and y <= 75:
                    endGame(screen, background)
                    pageNumber = 5
                  
            #if user clicks on a button on the fifth page      
            
            if pageNumber == 5:
                
                #if user clicks on end button
                
                if x >=130 and x <= 510 and y >= 290 and y <= 380:
                    
                    pygame.quit()
                    sys.exit() 
        
        #starting position (map and not coming from a previous page)
        
        if pageNumber == 0 and prevPosition == 0:
            #background
            background = pygame.image.load("galaxy.jpg")
            background = pygame.transform.scale(background, (640,480))
            background = background.convert()
            
            #reset activity variables
            answeredQuestionOne = "No"
            answeredQuestionTwo = "No"
            answeredQuestionThree = "No"
            viewedStory = "No"
            
            #fonts
            myTitleFont = pygame.font.SysFont("helvetica", 50)
            myButtonFont = pygame.font.SysFont("helvetica", 35)
            myTextFont = pygame.font.SysFont("helvetica", 20)
            
            #map title and end button
            mapTitleLabel = myButtonFont.render("Media Void! Use The Arrow Keys To Move!", False, (255, 255, 255))
            pygame.draw.rect(background, (192, 226, 237), [20, 420, 150, 50], 0)
            endButtonLabel = myButtonFont.render("End Game", False, (0, 0, 0))

            #planets and avatar rectangles
            pygame.draw.rect(colourBackground, (0, 0, 255), blueRectangle, 0)
            pygame.draw.rect(colourBackground, (255, 0, 0), redRectangle, 0)
            pygame.draw.rect(colourBackground, (0, 255, 0), greenRectangle, 0)
            pygame.draw.rect(colourBackground, (255, 255, 0), yellowRectangle, 0)
            pygame.draw.rect(colourBackground, (255,0,255), purpleRectangle, 0)
            
            #blit to screen
            screen.blit(background, (0,0))
            screen.blit(planet, (400, 350))
            screen.blit(planet2, (150, 290))
            screen.blit(planet3, (320, 50))
            screen.blit(planet4, (20, 50))
            screen.blit(mapTitleLabel, (60, 6))
            screen.blit(endButtonLabel, (30, 420))
            screen.blit(stars, (380, 330))
            screen.blit(stars2, (130, 270))
            screen.blit(stars3, (320, 50))
            screen.blit(stars4, (0, 30))
            screen.blit(stars22, (300, 30))
            screen.blit(astro, (blueRectangle_x, blueRectangle_y))
            pygame.display.flip()
            
            #controlled animation code
            
            if event.type == pygame.KEYDOWN:
                background = pygame.image.load("galaxy.jpg")
                background = pygame.transform.scale(background, (640,480))
                background = background.convert()
                
                if event.key == pygame.K_RIGHT:
                    blueRectangle_x = blueRectangle_x + 10
                    blueRectangle.x = blueRectangle.x + 10
                    pygame.draw.rect(colourBackground, (0, 0, 255), blueRectangle, 0)
                    
                elif event.key == pygame.K_UP:
                    blueRectangle_y = blueRectangle_y - 10
                    blueRectangle.y = blueRectangle.y - 10
                    
                elif event.key == pygame.K_LEFT:
                    blueRectangle_x = blueRectangle_x - 10
                    blueRectangle.x = blueRectangle.x - 10
                    
                elif event.key == pygame.K_DOWN:
                    blueRectangle_y = blueRectangle_y + 10
                    blueRectangle.y = blueRectangle.y + 10
                
                pygame.draw.rect(colourBackground, (0, 0, 255), blueRectangle, 0)
                pygame.draw.rect(colourBackground, (255, 0, 0), redRectangle, 0)
                pygame.draw.rect(colourBackground, (0, 255, 0), greenRectangle, 0)
                pygame.draw.rect(colourBackground, (255, 255, 0), yellowRectangle, 0)
                pygame.draw.rect(colourBackground, (255,0,255), purpleRectangle, 0)
            
            #if avatar comes into contanct with planet, move to a page
            
            if blueRectangle.colliderect(redRectangle):
                planetSound.play()
                pageNumber = 0.5
                
            elif blueRectangle.colliderect(greenRectangle):
                planetSound.play()
                pageNumber = 1.5
            
            elif blueRectangle.colliderect(yellowRectangle):
                planetSound.play()
                pageNumber = 3
                
            elif blueRectangle.colliderect(purpleRectangle):
                planetSound.play()
                pageNumber = 4
            
            #draw end button on background
            pygame.draw.rect(background, (192, 226, 237), [20, 420, 150, 50], 0)
            
            #blit to screen
            screen.blit(colourBackground, (0, 0))
            screen.blit(background, (0,0))
            screen.blit(planet, (400, 350))
            screen.blit(planet2, (150, 290))
            screen.blit(planet3, (320, 50))
            screen.blit(planet4, (20, 50))
            screen.blit(mapTitleLabel, (60, 6))
            screen.blit(endButtonLabel, (30, 420))
            screen.blit(stars, (380, 330))
            screen.blit(stars2, (130, 270))
            screen.blit(stars3, (320, 50))
            screen.blit(stars4, (0, 30))
            screen.blit(stars22, (300, 30))
            screen.blit(astro, (blueRectangle_x, blueRectangle_y))
            pygame.display.flip()
            
        #input from the user (rate experience)    
        
        if event.type == pygame.KEYDOWN:
            
            if pageNumber == -1:
                
                prevPosition = -1
                
                #load background
                background = pygame.image.load("startingPage.png")
                background = pygame.transform.scale(background, (640,480))
                background = background.convert()
                
                #setting fonts and background
                myTitleFont = pygame.font.SysFont("helvetica", 50)
                myButtonFont = pygame.font.SysFont("helvetica", 30)
                myTextFont = pygame.font.SysFont("helvetica", 20)
                
                #draw start clickable button
                pygame.draw.rect(background, (245, 236, 213), [130, 290, 380, 90], 0)
                
                #create all the labels
                instructionLabel = myTitleFont.render("Click Here to Begin", False, (0, 0, 0))
                nameLabel = myButtonFont.render("Enter Your Name And Press Enter!", False, (255, 255, 255))
                            
                #name surface and name
                name_surf = pygame.Surface((380, 50)).convert()
                name_surf.fill((245,236,213))
                name = myTextFont.render(name_value, True, (0,0,0))
                
                #when enter is pressed, your text is written in a file
                
                if event.key == pygame.K_RETURN:
                    
                    #write name in file
                    file = open("name.txt" , "w")
                    file.write(name_value)
                    file.close()
                    
                    #change label
                    nameLabel = myButtonFont.render("Success!", False, (255, 255, 255))
                                        
                #cut off last character
                    
                elif event.key == pygame.K_BACKSPACE and len(name_value) > 0:
                    name_value = name_value[:-1] 
                    
                #adds character value of key
                
                elif (event.unicode.isalnum() or event.key==pygame.K_SPACE) and len(name_value) < 36:
                    name_value += event.unicode 
                
                #set field label
                name = myTextFont.render(name_value, True, (0,0,0))
                
                #blit to screen
                screen.blit(background, (0, 0))
                screen.blit(instructionLabel, (140, 300))
                screen.blit(nameLabel, (130, 150))
                screen.blit(name_surf, (130, 200))
                screen.blit(name, (140, 205))
                pygame.display.flip()
            
            if pageNumber == 4:
                
                prevPosition = 4
                
                #read from files
                file = open("username.txt" , "r")
                userName = file.read()
                file.close()
                
                file = open("experience.txt" , "r")
                file_experience = file.read()
                file.close()
                
                #setting fonts and background
                myTitleFont = pygame.font.SysFont("helvetica", 50)
                myButtonFont = pygame.font.SysFont("helvetica", 30)
                myTextFont = pygame.font.SysFont("helvetica", 20)
                
                #create all the labels
                titleLabel = myTitleFont.render("Experience", False, (0, 0, 0))
                backButtonLabel = myButtonFont.render("Back To Map", False, (0, 0, 0))
                endButtonLabel = myButtonFont.render("End", False, (0, 0, 0))
                promptLabel = myTextFont.render(" Rate the Experience! (Around 30 Characters! This is kept to improve our site!)", False, (255, 255, 255))
                experience = myTextFont.render(file_experience, False, (0, 0, 0))
                userNameLabel = myTextFont.render(userName, False, (0, 0, 0))
                
                #redraw back to map 
                pygame.draw.rect(background, (221, 192, 237), [310, 25, 160, 50], 0)
                pygame.draw.rect(background, (237, 178, 181), [20, 25, 210, 50], 0)
                pygame.draw.rect(background, (192, 226, 237), [480, 25, 150, 50], 0)
                
                #field surface and field
                field_surf = pygame.Surface((600, 50)).convert()
                field_surf.fill((245,236,213))
                field = myTextFont.render(field_value, True, (0,0,0))
                
                #when enter is pressed, your text is printed on a comment bubble as if commented by the user
                
                if event.key == pygame.K_RETURN:
                    
                    #write in username file
                    file = open("username.txt" , "w")
                    file.write("anonymousUser")
                    file.close()

                    file = open("username.txt" , "r")
                    userName = file.read()
                    file.close()
                    
                    #write and read experience file
                    file = open("experience.txt" , "w")
                    file.write(field_value)
                    file.close()

                    file = open("experience.txt" , "r")
                    file_experience = file.read()
                    file.close()
                    
                    experience = myTextFont.render(file_experience, False, (0, 0, 0))
                    userNameLabel = myTextFont.render(userName, False, (0, 0, 0))
                    speechBubble = pygame.image.load("user comment.png")
                    speechBubble = pygame.transform.scale(speechBubble, (600,250))
                    speechBubble = speechBubble.convert()

                #cut off last character
                    
                elif event.key == pygame.K_BACKSPACE and len(field_value) > 0:
                    field_value = field_value[:-1] 
                    
                #adds character value of key
                
                elif (event.unicode.isalnum() or event.key==pygame.K_SPACE) and len(field_value) < 36:
                    field_value += event.unicode 
                
                #set field label
                field = myTextFont.render(field_value, True, (0,0,0))
                
                #blit to screen
                screen.blit(background, (0, 0))
                screen.blit(titleLabel, (20, 20))
                screen.blit(backButtonLabel, (323, 30))
                screen.blit(endButtonLabel, (530, 30))
                screen.blit(promptLabel, (20, 110))
                screen.blit(speechBubble, (20, 220))
                screen.blit(field_surf, (20, 150))
                screen.blit(field, (30, 155))
                screen.blit(experience, (337, 395))
                screen.blit(userNameLabel, (337, 370))
                pygame.display.flip()
       
                
