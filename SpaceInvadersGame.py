# Alexander Valera

# ANALYSIS:
# 1. Write a GUI program that plays the game of Space Invaders: SE!:
#    - Create a window containing the Space Invaders game
#    - Initialize counters for lives and for score
#    - Initialize set of enemies for user to combat
#    - Allows user to control spaceship with arrow keys
#    - Allows user to shoot missiles towards enemies
#    - Display that the user has lost if there are no more remaining lives
#    - Display that the user has won if there are no more remaining enemies
#    It must allow a user to count up and/or down using buttons, reset the counter using a button,
#    set the counter by entering a value and pressing <Enter> on the keyboard
#    It may not go below zero, and will warn the user when the user attempts to do so
# 2. Output:
#    - movement of spaceship
#    - movement of projectiles
#    - results of the game (win/loss) in another window
# 3. Input:
#    - arrow keys for movement
#    - spacebar for projectile shooting
#    - spacebar to quit game
# 4. Tasks:
#    Create GUI having:
#    - Class for creating Space Invaders
#    - Class for creating instances of sprites
#    - Classes for win and loss results
#    - Intersect Functions: detect intersection of missile and either alien or hero spaceship
#    - Counting Function: Keeps count of enemies on screen
#    - Moving Function: Controls movement of aliens across screen
#    - Create Enemies Function: Appends enemies into lists to display on screen
#    - Loop functions to keep game animating
#    - Loop functions to control count for lives and score
#    - Loop functions to control enemy movement from side to side
#    - Loop functions to control upgrade for user
#    - Loop functions to delete enemies as they are hit
#    - Condition statements to control user movement
#    - Condition statements to stop or end the game
#    - Condition statements to control enemy fire
#    - Collision detection for removal of player and/or enemies
#    - Score amount and lives amount
#    - Instance to being GUI
#    - User input to control ship movement
#    - Moving enemies for user to shoot
#    - Results that display whether the user has won or lost
#
# DESIGN:
# (embedded in code below)
#
# -------------------------------------------------------------------------------------------------------

# Import Modules
from pygame import *
import random

# This class provides the GUI representation of Space Invaders
class SpaceInvaders:

    # Constructor: creates, confitures, and places all the widgets of game
    def __init__(self):
        # Initiate GUI window
        self.__mainWindow = init()

        # Set Constants
        SPRITE_INTERSECT = 32
        #print(SPRITE_INTERSECT)
        #print(type(SPRITE_INTERSECT))

        ENEMY_SPEED = 2
        #print(ENEMY_SPEED)
        #print(type(ENEMY_SPEED))

        ENEMY_MISSILE_SPEED = 3
        #print(ENEMY_MISSILE_SPEED)
        #print(type(ENEMY_MISSILE_SPEED))

        MISSILE_SPEED = 5
        #print(MISSILE_SPEED)
        #print(type(MISSILE_SPEED))

        FIRST_ROW = 200
        #print(FIRST_ROW)
        #print(type(FIRST_ROW))

        SECOND_ROW = 150
        #print(SECOND_ROW)
        #print(type(SECOND_ROW))

        THIRD_ROW = 100
        #print(THIRD_ROW)
        #print(type(THIRD_ROW))

        FOURTH_ROW = 50
        #print(FOURTH_ROW)
        #print(type(FOURTH_ROW))
        
        # Create window for video game
        screen = display.set_mode((640,480))
        key.set_repeat(1, 1)
        self.__display = display.set_caption('Space Invaders: SE!')
        self.__backdrop = image.load("/Users/AlexValera/Python/FinalProject/Final Project/img/BlackBackground-1.bmp")
        self.__musicLoad = mixer.music.load("/Users/AlexValera/battleheroes.wav")
        self.__musicPlay = mixer.music.play(0,0)
        
        # This class provides the the instance for a sprite in the game
        class Sprite:

            # Constructor: creates, confitures, and places all the widgets for a sprite
            def __init__(self, xPosition, yPosition, filename):
                self.x = xPosition
                self.y = yPosition
                self.bitmap = image.load(filename)
                self.bitmap.set_colorkey((0,0,0))
                
            # Mutator: sets position of sprite
            def set_position(self, xpos, ypos):
                self.x = xpos
                self.y = ypos

            # Mutator: renders images of sprites on screen
            def render(self):
                screen.blit(self.bitmap, (self.x, self.y))                

        # Determines if missiles have intersected with enemy or hero
        # Takes in coordinates of missles and space objects
        # Returns 1 or 0 to represent if object has intersected with missile
        def intersect(oneX, oneY, twoX, twoY):
            if (oneX > twoX - SPRITE_INTERSECT) and (oneX < twoX + SPRITE_INTERSECT) and (oneY > twoY - SPRITE_INTERSECT) and (oneY < twoY + SPRITE_INTERSECT):
                return 1
            else:
                 return 0

        # This class provides the instance if the user wins the game              
        class Win:

            # Constructor: creates, confitures, and places all the widgets in the win window
            def __init__(self):
                init()
                screen = display.set_mode((640,480))
                key.set_repeat(1, 1)
                self.__display = display.set_caption('Space Invaders: SE!')
                self.__backdrop = image.load("/Users/AlexValera/Python/FinalProject/Final Project/img/BlackBackground-1.bmp")
                
                # Set the type of font for winning scren
                self.__theFont = font.Font(None, 30)

                # Render text to show lives remaining for user
                self.__text = self.__theFont.render("CONGRATULATIONS, YOU WIN!, press <SPACE>  to quit", True, (0,
                255, 0))

                # Create a rectangle
                self.__textRect = self.__text.get_rect()

                # Center the rectangle
                self.__textRect.centerx = (screen.get_rect().centerx)
                self.__textRect.centery = (screen.get_rect().centery)
                
                self.__stop = 0

                while self.__stop == 0:
                    screen.blit(self.__backdrop, (0,0))
                    screen.blit(self.__text, self.__textRect)

                    #Generic pygame decision statement, the event is QUIT, then the game ends
                    for event_ in event.get():
                        if event_.type == QUIT:
                            stop +=1

                    keyPressed = key.get_pressed()
                    #print(keyPressed)
                    #print(type(keyPressed))
                    
                    if keyPressed[K_SPACE]:
                        self.__stop += 1

                    display.update()
                    
                quit()

        # This class provides the instance if the user loses the game
        class Lose:

            # Constructor: creates, confitures, and places all of the widgets in the lose window
            def __init__(self):
                init()
                screen = display.set_mode((640,480))
                key.set_repeat(1, 1)
                self.__display = display.set_caption('Space Invaders: SE!')
                self.__backdrop = image.load("/Users/AlexValera/Python/FinalProject/Final Project/img/BlackBackground-1.bmp")
                
                # Set the type of font for winning scren
                self.__theFont = font.Font(None, 30)

                # Render text to show lives remaining for user
                self.__text = self.__theFont.render("I'm sorry, you lose, press <SPACE> to quit", True, (0,
                255, 0))

                # Create a rectangle
                self.__textRect = self.__text.get_rect()

                # Center the rectangle
                self.__textRect.centerx = (screen.get_rect().centerx)
                self.__textRect.centery = (screen.get_rect().centery)
                
                self.__stop = 0

                while self.__stop == 0:
                    screen.blit(self.__backdrop, (0,0))
                    screen.blit(self.__text, self.__textRect)

                    #Generic pygame decision statement, the event is QUIT, then the game ends
                    for event_ in event.get():
                        if event_.type == QUIT:
                            stop +=1

                    keyPressed = key.get_pressed()
                    #print(keyPressed)
                    #print(type(keyPressed))
                    
                    if keyPressed[K_SPACE]:
                        self.__stop += 1

                    display.update()
                    
                quit()
                
        # Function that will set the count for enemies on the screen
        # Takes in count for each row of enemies
        # Returns value of total enemies
        def countEnemies(value1,value2,value3,value4):
            self.__totalEnemies = 0
            #print(totalEnemies)
            #print(type(totalEnemies))
            self.__totalList = value1 + value2 + value3 + value4
            #print(totalList)
            #print(type(totalList))
            for count in self.__totalList:
                self.__totalEnemies += 1
                #print(totalEnemies)
                #print(type(totalEnemies)
            return self.__totalEnemies

        # Set up images for sprites
        self.__hero = Sprite(20, 400, '/Users/AlexValera/Python/FinalProject/Final Project/img/player.bmp')
        self.__ourmissile = Sprite(0, 480, '/Users/AlexValera/Python/FinalProject/Final Project/img/missile_player.bmp')
        self.__enemymissile = Sprite(0, 480, '/Users/AlexValera/Python/FinalProject/Final Project/img/missile_alien.bmp')
        self.__upgrade = Sprite(random.randint(0,480),0, '/Users/AlexValera/Python/FinalProject/Final Project/img/star.bmp')

        # Create empty lists for enemies
        self.__enemiesOne = []
        self.__enemiesTwo = []
        self.__enemiesThree = []
        self.__enemiesFour = []

        # Accumulator for enemies on screen
        self.__enemyCreation = 0

        # Create a function that takes in the four empty lists created, and adds 10 enemies per
        # each row through a while loop. 
        def createEnemies(listOne, listTwo, listThree, listFour):
            self.__enemiesOne = listOne
            self.__enemiesTwo = listTwo
            self.__enemiesThree = listThree
            self.__enemiesFour = listFour
            while self.__enemyCreation < 10 :
                if self.__enemyCreation < 10:
                    self.__enemiesOne.append(Sprite(50 * self.__enemyCreation + 50, FIRST_ROW, '/Users/AlexValera/Python/FinalProject/Final Project/img/alien1.bmp'))
                    self.__enemiesTwo.append(Sprite(50 * self.__enemyCreation + 50, SECOND_ROW, '/Users/AlexValera/Python/FinalProject/Final Project/img/alien2.bmp'))
                    self.__enemiesThree.append(Sprite(50 * self.__enemyCreation + 50, THIRD_ROW, '/Users/AlexValera/Python/FinalProject/Final Project/img/alien1.bmp'))
                    self.__enemiesFour.append(Sprite(50 * self.__enemyCreation + 50, FOURTH_ROW, '/Users/AlexValera/Python/FinalProject/Final Project/img/alien2.bmp'))
                    self.__enemyCreation += 1
                    #print(self.__enemyCreation)
                    #print(type(self.__enemyCreation))
                    
        # Call the createEnemies function to create the four rows of enemies
        createEnemies(self.__enemiesOne, self.__enemiesTwo, self.__enemiesThree, self.__enemiesFour)

        # This function takes in an enemy list, and makes them start to move
        def makeEnemiesMove(enemies):
            self.__enemies = enemies
            for enemy in range(len(self.__enemies)):
                self.__enemies[enemy].x += ENEMY_SPEED
                self.__enemies[enemy].render()

        # Create a string to represent lives
        self.__lives = [1,1,1,1,1]

        # Create a variable for the length of the string lives, then create
        # a substitute variable to be used in order to avoid break statements. 
        self.__livesLen = len(self.__lives)
        #print(livesLen)
        #print(type(livesLen))
        self.__livesSub = self.__livesLen
        #print(livesSub)
        #print(type(livesSub))
    
        # Create lives list
        self.__livesText = ["X", "LIVES = 1", "LIVES = 2", "LIVES = 3", "LIVES = 4 ", "LIVES = 5"]

        # Create len(livesText) variable and another dummy variable to compensate
        # for no break statements
        self.__livesTextLen = len(self.__livesText)
        #print(livesTextLen)
        #print(type(livesTextLen))
        self.__livesTextSub = self.__livesTextLen
        #print(livesTextSub)
        #print(type(livesTextSub))
        
#------------------------------------------------------------------------------------------------------

        # Create text that shows how many lives the user currently has
        # Set the type of font for the Lives = X text
        self.__theFont = font.Font(None, 50)

        # Render text to show lives remaining for user
        self.__text = self.__theFont.render(self.__livesText[len(self.__livesText)-1], True, (0,
        255, 0))

        # Create a rectangle
        self.__textRect = self.__text.get_rect()

        # Center the rectangle
        self.__textRect.centerx = ((screen.get_rect().centerx) - 225)
        self.__textRect.centery = ((screen.get_rect().centery) - 210)
        
#---------------------------------------------------------------------------------------------------------

        # Create a Score counter to appear at the top right corner of screen
        self.__score = 0

        # Set the type of font for the Lives = X text
        self.__theFont = font.Font(None, 50)

        # Render text to show lives remaining for user
        self.__scoreText = self.__theFont.render("Score = ", True, (0,
        255, 0))

        # Create a rectangle
        self.__scoreTextRect = self.__scoreText.get_rect()

        # Center the rectangle
        self.__scoreTextRect.centerx = ((screen.get_rect().centerx) + 150)
        self.__scoreTextRect.centery = ((screen.get_rect().centery) - 210)

        # Set the type of font for the Lives = X text
        self.__theFont = font.Font(None, 50)

        # Render text to show lives remaining for user
        self.__scoreNumText = self.__theFont.render(str(self.__score), True, (0,
        255, 0))

        # Create a rectangle
        self.__scoreNumTextRect = self.__scoreNumText.get_rect()

        # Center the rectangle
        self.__scoreNumTextRect.centerx = ((screen.get_rect().centerx) + 250)
        self.__scoreNumTextRect.centery = ((screen.get_rect().centery) - 210)

        # Create enemy length variables and dummy variables in order to
        # Avoid break statements
        self.__enemiesOneLen = len(self.__enemiesOne)
        #print(self.__enemiesOneLen)
        #print(type(self.__enemiesOneLen))
        self.__enemiesOneSub = self.__enemiesOneLen
        #print(self.__enemiesOneSub)
        #print(type(self.__enemiesOneSub))
        self.__enemiesTwoLen = len(self.__enemiesTwo)
        #print(enemiesTwoLen)
        #print(type(enemiesTwoLen))
        self.__enemiesTwoSub = self.__enemiesTwoLen
        #print(self.__enemiesTwoSub)
        #print(type(self.__enemiesTwoSub))
        self.__enemiesThreeLen = len(self.__enemiesThree)
        #print(self.__enemiesThreeLen)
        #print(type(self.__enemiesThreeLen))
        self.__enemiesThreeSub = self.__enemiesThreeLen
        #print(self.__enemiesThreeSub)
        #print(type(self.__enemiesThreeSub))
        self.__enemiesFourLen = len(self.__enemiesFour)
        #print(self.__enemiesFourLen)
        #print(type(self.__enemiesFourLen))
        self.__enemiesFourSub = self.__enemiesFourLen
        #print(self.__enemiesFourSub)
        #print(type(self.__enemiesFourSub))

        # Set up variable that will check if the game is still running, if it is
        # above 0, or 1, then the game will stop. 
        self.__stop = 0

        # Set up while loop to animate the game continually
        while self.__stop == 0:

            # Show the backdrop
            screen.blit(self.__backdrop, (0, 0))

            # For every count in self.__livesText, every time the hero sprite intersects with an enemy missile
            # the hero sprite will lose a life from self.__livesText list. 
            for count in range(0,len(self.__livesText)):
                if self.__livesTextSub == self.__livesTextLen:
                    if intersect(self.__hero.x, self.__hero.y, self.__enemymissile.x, self.__enemymissile.y):
                        if len(self.__livesText) >= 0:
                            del self.__livesText[len(self.__livesText)-1]
                            self.__text = self.__theFont.render(self.__livesText[len(self.__livesText)-1], True, (0,255, 0))
                            self.__livesTextLen -= 1
            self.__livesTextSub = self.__livesTextLen

            # Show how many lives you have on the top right corner of the screen                    
            screen.blit(self.__text, self.__textRect)

            # Show the score you have
            screen.blit(self.__scoreText, self.__scoreTextRect)
            screen.blit(self.__scoreNumText, self.__scoreNumTextRect)

            # Render the enemy sprites and make them start to move
            makeEnemiesMove(self.__enemiesOne)
            makeEnemiesMove(self.__enemiesTwo)
            makeEnemiesMove(self.__enemiesThree)
            makeEnemiesMove(self.__enemiesFour)        
                                      
#--------------------------------------------------------------------------
                
            # Make the 4 rows of enemies change direction to go to the left when
            # hitting the right border.
            for count in range(len(self.__enemiesFour)):
                if self.__enemiesFour[count].x > 590:
                    ENEMY_SPEED = (ENEMY_SPEED - (2*ENEMY_SPEED))
                    for count in range(len(self.__enemiesFour)):
                        self.__enemiesFour[count].y += 5
                    for count in range(len(self.__enemiesThree)):
                        self.__enemiesThree[count].y += 5
                    for count in range(len(self.__enemiesTwo)):
                        self.__enemiesTwo[count].y += 5
                    for count in range(len(self.__enemiesOne)):
                        self.__enemiesOne[count].y += 5
            # Make the 4 rows of enemies change direction to go to the right when
            # hitting the left border
            if self.__enemiesFour[0].x < 10:
                ENEMY_SPEED = (ENEMY_SPEED - (2*ENEMY_SPEED))
                for count in range(len(self.__enemiesFour)):
                    self.__enemiesFour[count].y += 5
                for count in range(len(self.__enemiesThree)):
                    self.__enemiesThree[count].y += 5
                for count in range(len(self.__enemiesTwo)):
                    self.__enemiesTwo[count].y += 5
                for count in range(len(self.__enemiesOne)):
                    self.__enemiesOne[count].y += 5   
                             
#-------------------------------------------------------------------------

            # Render the hero's missile off screen..ready for firing
            if self.__ourmissile.y < 479 and self.__ourmissile.y > 0:
                self.__ourmissile.render()
                self.__ourmissile.y -= MISSILE_SPEED
                
#-------------------------------------------------------------------------
                
            # The furthers down enemy row will fire from random enemies of that
            # particular row. If that enemy row is demolished by cats and it no
            # longer exists, the next row will begin firing.        
            if (len(self.__enemiesOne)) > 0:
                if self.__enemymissile.y >= 480 and len(self.__enemiesOne) > 0:
                    self.__enemymissile.x = self.__enemiesOne[random.randint(0, len(self.__enemiesOne) - 1)].x
                    self.__enemymissile.y = self.__enemiesOne[0].y
                        
            if (len(self.__enemiesTwo)) > 0:
                if self.__enemymissile.y >=480 and len(self.__enemiesTwo) > 0:
                    self.__enemymissile.x = self.__enemiesTwo[random.randint(0, len(self.__enemiesTwo) - 1)].x
                    self.__enemymissile.y = self.__enemiesTwo[0].y
                        
            if (len(self.__enemiesThree)) > 0:
                if self.__enemymissile.y >=480 and len(self.__enemiesThree) > 0:
                    self.__enemymissile.x = self.__enemiesThree[random.randint(0, len(self.__enemiesThree) - 1)].x
                    self.__enemymissile.y = self.__enemiesThree[0].y

            if (len(self.__enemiesFour)) > 0:
                if self.__enemymissile.y >=480 and len(self.__enemiesFour) > 0:
                    self.__enemymissile.x = self.__enemiesFour[random.randint(0, len(self.__enemiesFour) - 1)].x
                    self.__enemymissile.y = self.__enemiesFour[0].y
                        
#-------------------------------------------------------------------------

        # If the hero and enemy missile intersect, the hero loses a life from the
        # self.__lives list. 

            for count in range(0,len(self.__lives)):
                if self.__livesSub == self.__livesLen:
                    if intersect(self.__hero.x, self.__hero.y, self.__enemymissile.x, self.__enemymissile.y):
                        self.__enemymissile.x = 500
                        self.__enemymissile.y = 500
                        del self.__lives[count]
                        if not self.__lives:
                            self.__stop +=1
                            #print(stop)
                            #print(type(stop))
                        self.__livesLen -= 1
                            #print(livesLen)
                            #print(type(livesLen))
                                
            self.__livesSub = self.__livesLen
            #print(livesSub)
            #print(type(livesSub))

#------------------------------------------------------------------------------------------------------

            # If the enemy gets hit by the hero's projectile, then that enemy
            # gets deleted from the list.       
            for count in range(0, len(self.__enemiesOne)):
                if self.__enemiesOneSub == self.__enemiesOneLen:
                        if intersect(self.__ourmissile.x, self.__ourmissile.y, self.__enemiesOne[count].x, self.__enemiesOne[count].y):
                                self.__score += 100
                                self.__scoreNumText = self.__theFont.render(str(self.__score), True, (0,255, 0))
                                screen.blit(self.__scoreNumText, self.__scoreNumTextRect)
                                self.__ourmissile.x = 500
                                self.__ourmissile.y = 500
                                del self.__enemiesOne[count]
                                self.__enemiesOneLen -= 1
                                #print(enemiesOneLen)
                                #print(type(enemiesOneLen))
                            
            self.__enemiesOneSub = self.__enemiesOneLen
            #print(enemiesOneSub)
            #print(type(enemiesOneSub))
                        
            for count in range(0, len(self.__enemiesTwo)):
                if self.__enemiesTwoSub == self.__enemiesTwoLen:
                    if intersect(self.__ourmissile.x, self.__ourmissile.y, self.__enemiesTwo[count].x, self.__enemiesTwo[count].y):
                            self.__score += 100
                            self.__scoreNumText = self.__theFont.render(str(self.__score), True, (0,255, 0))
                            screen.blit(self.__scoreNumText, self.__scoreNumTextRect)
                            self.__ourmissile.x = 500
                            self.__ourmissile.y = 500
                            del self.__enemiesTwo[count]
                            self.__enemiesTwoLen -= 1
                            #print(enemiesTwoLen)
                            #print(type(enemiesTwoLen))
                            
            self.__enemiesTwoSub = self.__enemiesTwoLen
            #print(enemiesTwoSub)
            #print(type(enemiesTwoSub))
                           
            for count in range(0, len(self.__enemiesThree)):
                if self.__enemiesThreeSub == self.__enemiesThreeLen:
                    if intersect(self.__ourmissile.x, self.__ourmissile.y, self.__enemiesThree[count].x, self.__enemiesThree[count].y):
                        self.__score += 100
                        self.__scoreNumText = self.__theFont.render(str(self.__score), True, (0,255, 0))
                        screen.blit(self.__scoreNumText, self.__scoreNumTextRect)
                        self.__ourmissile.x = 500
                        self.__ourmissile.y = 500
                        del self.__enemiesThree[count]
                        self.__enemiesThreeLen -= 1
                        #print(enemiesThreeLen)
                        #print(type(enemiesThreeLen))
                            
            self.__enemiesThreeSub = self.__enemiesThreeLen
            #print(enemiesThreeSub)
            #print(type(enemiesThreeSub))
                
            for count in range(0, len(self.__enemiesFour)):
                if self.__enemiesFourSub == self.__enemiesFourLen:
                        if intersect(self.__ourmissile.x, self.__ourmissile.y, self.__enemiesFour[count].x, self.__enemiesFour[count].y):
                                self.__score += 100
                                self.__scoreNumText = self.__theFont.render(str(self.__score), True, (0,255, 0))
                                screen.blit(self.__scoreNumText, self.__scoreNumTextRect)
                                self.__ourmissile.x = 500
                                self.__ourmissile.y = 500
                                del self.__enemiesFour[count]
                                self.__enemiesFourLen -= 1
                                #print(enemiesFourLen)
                                #print(type(enemiesFourLen))
                                
            self.__enemiesFourSub = self.__enemiesFourLen
            #print(enemiesFourSub)
            #print(type(enemiesFourSub))
            
#----------------------------------------------------------------------------------
        
            # Generic pygame decision statement, the event is QUIT, then the game end       
            for event_ in event.get():
                if event_.type == QUIT:
                    self.__stop +=1
                    #print(stop)
                    #print(type(stop))
                
#----------------------------------------------------------------------------------
                        
            # When the enemy count is at a certain values, an upgrade will render
            # from the top of the screen, and one when touched  by the hero,
            # enemies will temporarily slow down and the missile speed will increase
                
            if countEnemies(self.__enemiesOne,self.__enemiesTwo,self.__enemiesThree,self.__enemiesFour) <= 30:
                self.__upgrade.render()
                self.__upgrade.y += 2
                if intersect(self.__upgrade.x, self.__upgrade.y, self.__hero.x, self.__hero.y)== 1:
                    self.__lives = [1,1,1,1,1]
                    self.__livesText = ["X", "LIVES = 1 ", "LIVES = 2 ", "LIVES = 3", "LIVES = 4", "LIVES = 5"]
                    self.__text = self.__theFont.render(self.__livesText[len(self.__livesText)-1], True, (0,255, 0))
                    screen.blit(self.__text, self.__textRect)
                    #print(MISSILE_SPEED)
                    #print(type(MISSILE_SPEED))
                    self.__upgrade.x = 500
                    self.__upgrade.y = 500
                    
            if countEnemies(self.__enemiesOne,self.__enemiesTwo,self.__enemiesThree,self.__enemiesFour) <= 20:
                self.__upgrade.render()
                self.__upgrade.y += 2
                if intersect(self.__upgrade.x, self.__upgrade.y, self.__hero.x, self.__hero.y)== 1:
                    self.__lives = [1,1,1,1,1]
                    self.__livesText = ["X", "LIVES = 1 ", "LIVES = 2 ", "LIVES = 3", "LIVES = 4", "LIVES = 5"]
                    self.__text = self.__theFont.render(self.__livesText[len(self.__livesText)-1], True, (0,255, 0))
                    screen.blit(self.__text, self.__textRect)
                    #print(MISSILE_SPEED)
                    #print(type(MISSILE_SPEED))
                    self.__upgrade.x = 500
                    self.__upgrade.y = 500

            if countEnemies(self.__enemiesOne,self.__enemiesTwo,self.__enemiesThree,self.__enemiesFour) <= 10:
                self.__upgrade.render()
                self.__upgrade.y += 2
                if intersect(self.__upgrade.x, self.__upgrade.y, self.__hero.x, self.__hero.y)== 1:
                    self.__lives = [1,1,1,1,1]
                    self.__livesText = ["X", "LIVES = 1 ", "LIVES = 2 ", "LIVES = 3", "LIVES = 4", "LIVES = 5"]
                    self.__text = self.__theFont.render(self.__livesText[len(self.__livesText)-1], True, (0,255, 0))
                    screen.blit(self.__text, self.__textRect)
                    #print(MISSILE_SPEED)
                    #print(type(MISSILE_SPEED))
                    self.__upgrade.x = 500
                    self.__upgrade.y = 500

            if countEnemies(self.__enemiesOne,self.__enemiesTwo,self.__enemiesThree,self.__enemiesFour) <= 10:
                self.__upgrade.render()
                self.__upgrade.y += 4
                if intersect(self.__upgrade.x, self.__upgrade.y, self.__hero.x, self.__hero.y)== 1:
                    self.__lives = [1,1,1,1,1]
                    self.__livesText = ["X", "LIVES = 1 ", "LIVES = 2 ", "LIVES = 3", "LIVES = 4", "LIVES = 5"]
                    self.__text = self.__theFont.render(self.__livesText[len(self.__livesText)-1], True, (0,255, 0))
                    screen.blit(self.__text, self.__textRect)
                    #print(MISSILE_SPEED)
                    #print(type(MISSILE_SPEED))
                    self.__upgrade.x = 500
                    self.__upgrade.y = 500
                   
            if countEnemies(self.__enemiesOne,self.__enemiesTwo,self.__enemiesThree,self.__enemiesFour) == 0:
                self.__stop += 2 
                
#-------------------------------------------------------------------------------
        
            # Make the method key._getpressed() from pygame equal to
            # another variable.
            self.__keyPressed = key.get_pressed()
            #print(keyPressed)
            #print(type(keyPressed))

            # If you click the right directional button, and the hero's x-axis value
            # is less than the screen's dimensional max, then the hero will move to the right. 
            if self.__keyPressed[K_RIGHT] and self.__hero.x < 590:
                self.__hero.x += 5

            # If you click the left directional button, and the hero's x-axis value
            # is more than the screen's dimensional min, then the hero will move to the left. 
            if self.__keyPressed[K_LEFT] and self.__hero.x > 10:
                self.__hero.x -= 5

            # Assign the keyPressed[K_SPACE] to another variable
            self.__fire = self.__keyPressed[K_SPACE]
            # If you fire, the missile will copy the hero's dimensions and be created
            if self.__fire:
                self.__ourmissile.x = self.__hero.x
                self.__ourmissile.y = self.__hero.y
                self.__ourmissile.render()

            # The enemy missile will be created
            self.__enemymissile.render()
            # The enemy missile will begin to move upwards
            self.__enemymissile.y += ENEMY_MISSILE_SPEED
            # The hero is then created
            self.__hero.render()

            # Display Update, necessary in every PYGame
            display.update()
            # Make the time.delay parameter equal to 2 in order to keep the game moving quickly
            time.delay(2)

    # If stop is not equal to zero, quit the game!        
        quit()
        if self.__stop == 2:
            win = Win()
        if self.__stop == 1:
            lose = Lose()

# Create instance of GUI
spaceinvaders = SpaceInvaders()

