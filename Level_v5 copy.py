import pygame, sys
from pygame.locals import *

BLACK = (0,   0,   0  )
BROWN = (153, 76,  0  )
GREEN = (0,   255, 0  )
BLUE  = (0,   0,   255)
RED =   (255, 0,   0)
WHITE     = (255, 255, 255)
DARKGREEN = (  0, 155,   0)
BGCOLOR = BLACK 

TILESIZE = 48
size = 10
MAPWIDTH = size*TILESIZE
MAPHEIGHT = size*TILESIZE

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH,MAPHEIGHT))
pygame.display.set_caption("Rust Bucket")

char = pygame.image.load('RustBucket_char.GIF')
floor = pygame.image.load('RustBucket_tile1.PNG')
pig1 = pygame.image.load('RustBucket_boar_down1.PNG')
pig2 = pygame.image.load('RustBucket_boar_up1.PNG')
pig3 = pygame.image.load('RustBucket_boar_right1.PNG')
pig4 = pygame.image.load('RustBucket_boar_left1.PNG')
slime1 = pygame.image.load('RustBucket_slime_1.PNG')
slime2 = pygame.image.load('frame-15.GIF')
'''
slime = []
for i in range(16):
    slime.append(pygame.image.load('frame-%.2d.GIF'%(i+1)))
'''
skull = pygame.image.load('RustBucket_skull_bomb.PNG')
octopus = pygame.image.load('RustBucket_octopus.GIF')
wall = pygame.image.load('RustBucket_crate.PNG')
final = pygame.image.load('RustBucket_invisible_tile.PNG')
pot = pygame.image.load('RustBucket_rock.PNG')

colours  = {'P':char,'M':pig1,'W':pig2,'E':pig3,'3':pig4,'A':skull,'B':slime1,'K':slime2,'0':floor,'D':octopus,'S':wall, 'F':final, 'N':pot}
'''
for i in colours:
    if i!="F" and i!="0":
        colours[i] = pygame.transform.scale(colours[i], (TILESIZE, int(5*TILESIZE/4)))
    else:
        colours[i] = pygame.transform.scale(colours[i], (TILESIZE, TILESIZE))
'''

#'''
Level = [[  ['0', '0', '0', '0', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', 'P', '0', '0', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', '0', '0', 'B', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', '0', '0', '0', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', '0', 'B', '0'],
			['S', 'S', 'S', 'S', '0', 'B', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', 'F', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', '0', '0', '0']],
		 [  ['P', '0', 'S', 'S', 'D', '0', '0', '0', '0', '0'],
		 	['0', '0', 'S', 'S', '0', 'D', '0', '0', '0', '0'],
		 	['0', 'D', 'S', 'S', '0', '0', 'D', '0', '0', '0'],
		 	['0', 'D', 'S', 'S', '0', '0', '0', 'D', '0', '0'],
		 	['0', '0', 'S', 'S', '0', '0', '0', '0', 'D', '0'],
			['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
			['0', '0', 'S', 'S', '0', '0', '0', 'D', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', 'D', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', 'D', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', 'D', '0', '0', '0', '0', 'F']],
		 [  ['F', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
		 	['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '0'],
		 	['P', 'N', '0', '0', '0', '0', '0', '0', 'N', '0'],
		 	['0', 'N', '0', 'N', 'N', 'N', 'N', '0', 'N', '0'],
		 	['0', 'N', '0', 'N', '0', '0', '0', '0', 'N', '0'],
		 	['0', '0', '0', 'N', '0', 'N', 'N', 'N', 'N', '0'],
		 	['N', 'N', '0', 'N', '0', '0', 'N', '0', '0', '0'],
		 	['N', '0', '0', 'N', '0', '0', 'N', '0', 'N', 'A'],
		 	['A', '0', 'N', 'N', 'N', '0', '0', '0', 'N', 'N'],
		 	['N', 'N', 'N', 'N', 'A', '0', 'N', 'N', 'N', 'N']],
		 [  ['S', '0', '0', '0', 'S', 'S', 'S', 'S', 'S', 'S'],
		 	['S', '0', '0', '0', 'S', 'B', '0', 'B', '0', 'S'],
			['S', 'A', '0', '0', 'S', '0', 'B', '0', 'B', 'S'],
			['S', '0', '0', '0', 'S', 'B', '0', 'B', '0', 'S'],
			['S', '0', '0', '0', 'S', '0', 'B', '0', 'B', 'S'],
			['0', 'P', 'A', '0', 'N', 'B', '0', 'B', '0', 'F'],
			['S', '0', '0', '0', 'S', '0', 'B', '0', 'B', 'S'],
			['S', 'A', '0', '0', 'S', 'B', '0', 'B', '0', 'S'],
			['S', '0', '0', '0', 'S', '0', 'B', '0', 'B', 'S'],
			['S', '0', '0', '0', 'S', 'S', 'S', 'S', 'S', 'S']],
		 [  ['S', 'S', 'S', 'S', 'S', 'S', '0', '0', '0', '0'],
		 	['0', '0', '0', '0', '0', 'S', '0', '0', '0', '0'],
		 	['0', '0', 'W', '0', '0', 'S', '0', '0', 'F', '0'],
		 	['0', '3', 'P', 'E', '0', 'S', 'W', '0', '0', '0'],
		 	['0', '0', 'M', '0', '0', 'S', '0', '0', '0', '0'],
		 	['0', '0', '0', '0', '0', 'S', '0', '0', '0', '0'],
		 	['S', 'S', '0', 'S', 'S', 'S', '0', '0', 'W', '0'],
		 	['3', '0', 'M', '0', '0', 'N', '3', '0', '0', '0'],
		 	['0', '0', 'N', '0', '0', 'S', '0', '0', '0', '0'],
		 	['0', '0', '0', '0', '0', 'S', '0', '0', '0', '0']],
		 [  ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            ['N', 'A', '0', '0', 'N', 'S', '0', '0', '0', 'N'],
            ['0', 'S', 'S', 'S', 'N', 'S', 'N', 'N', 'N', 'N'],
            ['P', 'S', 'S', 'S', '0', 'S', '0', '0', '0', 'N'],
            ['0', 'S', 'S', 'S', 'A', 'N', '0', 'F', '0', 'N'],
            ['0', 'S', 'S', 'S', '0', 'S', '0', '0', '0', 'N'],
            ['N', 'N', '0', 'A', 'N', 'S', '0', '0', '0', 'N'],
            ['S', 'S', 'S', 'S', 'S', 'S', 'N', 'N', 'N', 'N'],
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S']],
         [  ['0', 'D', '0', '0', '0', '0', 'W', '0', '0', '0'],
            ['0', '0', '0', 'A', 'P', '3', 'B', '0', '0', '0'],
            ['0', '0', '0', '0', 'B', 'A', '0', 'A', '0', '0'],
            ['0', 'D', '0', '0', '0', '0', 'B', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', 'D', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', 'W', '0', '0', '0'],
            ['0', 'A', '0', '0', 'E', 'A', '0', 'F', 'A', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0']],
         [  ['P', 'N', 'N', 'N', 'N', 'N', 'N', 'N', '0', '0'],
            ['B', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['B', '0', '0', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            ['B', 'S', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['B', 'S', 'S', '0', '0', '0', '0', '0', '0', '0'],
            ['B', 'S', 'S', 'S', '0', '0', '0', '0', '0', '0'],
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', '0'],
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D'],
            ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'F']],
         [  ['P', 'N', 'S', 'S', 'S', 'S', 'S', 'S', 'N', 'N'],
            ['B', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['B', '0', '0', 'S', 'S', 'S', 'S', 'S', 'S', 'S'],
            ['0', 'S', 'B', '0', '0', '0', '0', '0', '0', '0'],
            ['0', 'S', 'S', '0', '0', '0', '0', '0', 'A', '0'],
            ['0', 'S', 'S', 'S', '0', '0', '0', '0', '0', 'A'],
            ['N', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'N'],
            ['0', 'A', '0', 'A', '0', '0', 'A', '0', '0', '0'],
            ['S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'D'],
            ['F', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B']]]   # list of all levels
'''
Level = [[  ['0', '0', '0', '0', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', 'P', '0', '0', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', '0', '0', 'B', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', '0', '0', '0', '0', 'S', 'S', 'S', 'S', 'S'],
			['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', '0', 'B', '0'],
			['S', 'S', 'S', 'S', '0', 'B', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', 'F', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', '0', '0', '0'],
			['S', 'S', 'S', 'S', '0', '0', '0', '0', '0', '0']]]
#'''

Board = [] # board state
cur = 0    # current level
endless = False
score = 0       # score
prev_score = 0  # previous score
mobsymbols = ["M", "W", "E", "3", "A", "B", "D", "N", "K"]

def InitBoard(n):
    '''Create a n * n board'''
    for i in range(n):
        Board.append(["0"]*n)
        

InitBoard(size)

def PrintBoard(board):
    '''Prints current board state in word form'''
    for i in board:
        for j in i:
            print(j, end = " ")
        print("")
    
def ResetBoard():
    '''Resets current board'''
    del mobs[:]
    for i in range(size):
        for j in range(size):
            Board[i][j] = "0"

def Restart():
    """
    Does what its name suggests
    """
    ResetBoard()
    global P
    global Board
    global cur
    global final
    if cur <= len(Level)-1:
        for i in range(size):
            for j in range(size):
                Board[i][j] = Level[cur][i][j]
        
        for i in range(size):
            for j in range(size):
                if Board[i][j]=="P":
                    P = Player(i+1, j+1)
                elif Board[i][j]=="W":
                    M = Pig(i+1, j+1, 0)
                    M.symbol = Board[i][j]
                elif Board[i][j]=="3":
                    M = Pig(i+1, j+1, 1)
                    M.symbol = Board[i][j]
                elif Board[i][j]=="E":
                    M = Pig(i+1, j+1, 2)
                    M.symbol = Board[i][j]
                elif Board[i][j]=="M":
                    M = Pig(i+1, j+1, 3)
                    M.symbol = Board[i][j]
                elif Board[i][j]=="B":
                    Slime(i+1, j+1)
                elif Board[i][j]=="A":
                    Skull(i+1, j+1)
                elif Board[i][j]=="N":
                    Stone(i+1, j+1)
                elif Board[i][j]=="D":
                    Octopus(i+1, j+1)
                elif Board[i][j]=="S":
                    Wall(i+1, j+1)
                elif Board[i][j]=="F":
                    final = (i+1,j+1)
    else:
        global endless
        endless = True
        Board = []
        InitBoard(10)
        P = Player(2,4)
        cur+=3
        genMobs(cur)

def genMobs(n):
    '''Randomly generates n mobs in board
    n should <= number of empty spaces in current Board'''
    empty = []
    for i in range(size):
        for j in range(size):
            if(Board[i][j]=="0"):
                empty.append((i+1, j+1))
    import random
    for i in range(n):
        i = random.choice([1,2,3])
        if i==1:
            Skull(*empty.pop(random.randint(0, len(empty)-1)))
        elif i==2:
            Slime(*empty.pop(random.randint(0, len(empty)-1)))
        elif i==3:
            Pig(*empty.pop(random.randint(0, len(empty)-1)))
        #print("Generating 1 Skull of type", i)

class Player:
    def __init__(self, x, y):
        self.pos = (x, y)
        self.symbol = "P"
        self.setpos(x, y)
        self.alive = True
    
    def setpos(self, x, y):
        
        if x-1 not in range(size) or y-1 not in range(size):
            pass
            #print("Error:", self, "hit wall")                  # makes sure no out of bound movement
            
        elif Board[x-1][y-1] in mobsymbols:
            for m in mobs:
                if m.pos==(x, y):
                    #print("Killing", m)
                    m.kill()
                    break
            for i in mobs:
                i.AutoMove()
            
        elif Board[x-1][y-1] != "0" and Board[x-1][y-1] != "F":
            pass
            #print("Error:", self, "Board is occupied")                # is not "0" -> board is occupied
            #print("Board[x-1][y-1] = ", Board[x-1][y-1])

        else:
            if Board[self.pos[0]-1][self.pos[1]-1]==self.symbol: # set previously occupied block to be empty
                Board[self.pos[0]-1][self.pos[1]-1] = "0"
            Board[x-1][y-1] = self.symbol                        # set block to be occupied by player
            self.pos = (x, y)                                    # update position later 
            for i in mobs:                                       # Skull movement
                i.AutoMove()
            
            #print("Position", *self.pos)              # remove later
    
    def Move(self, move):

        if move=="up":
            self.setpos(self.pos[0]-1, self.pos[1])
        elif move=="left":
            self.setpos(self.pos[0], self.pos[1]-1)
        elif move=="down":
            self.setpos(self.pos[0]+1, self.pos[1])
        elif move=="right":
            self.setpos(self.pos[0], self.pos[1]+1)
    
    def kill(self):
        #print("Game Over!") # 改成pygame裡顯示
        self.alive = False
        Board[self.pos[0]-1][self.pos[1]-1] = "X" 
    
mobs = [] # list that contains all mobs

class Skull(Player):
    # worth 400 points
    def __init__(self, x, y):
        self.pos = (x, y)
        self.symbol = "A"
        self.setpos(x, y)
        self.worth = 400
        mobs.append(self)
        
    def setpos(self, x, y):
        
        if x-1 not in range(size) or y-1 not in range(size):
            pass
            #print("Error:", self, "hit wall")                  # makes sure no out of bound movement
            
        elif Board[x-1][y-1] == "P":
            global P
            P.kill()
            
        elif Board[x-1][y-1] != "0":                          # is not "0" -> board is occupied
            pass
            # move around obstacle
            
        else:
            if Board[self.pos[0]-1][self.pos[1]-1]==self.symbol: # set previously occupied block to be empty
                Board[self.pos[0]-1][self.pos[1]-1] = "0"
                
            Board[x-1][y-1] = self.symbol                        # set block to be occupied by player
            self.pos = (x, y)                                    # update position later 
            
            #print("Position", *self.pos)              # remove later

    def AutoMove(self):
        #available_movements
        dis = [1000]*4
        try:
            if Board[self.pos[0]-2][self.pos[1]-1]  == "0" or Board[self.pos[0]-2][self.pos[1]-1]  == "P":
                dis[0] = (self.pos[0] - P.pos[0] - 1)**2 + (self.pos[1] - P.pos[1])**2
        except:
            pass
        try:
            if self.pos[1] == 1:
            	dis[1] = 10000
            else:	
            	if Board[self.pos[0]-1][self.pos[1]-2]  == "0" or Board[self.pos[0]-1][self.pos[1]-2]  == "P":
                	dis[1] = (self.pos[0] - P.pos[0])**2 + (self.pos[1] - P.pos[1] - 1)**2
        except:
            pass
        try:
            if Board[self.pos[0]-1][self.pos[1]]  == "0" or Board[self.pos[0]-1][self.pos[1]]  == "P":
                dis[2] = (self.pos[0] - P.pos[0])**2 + (self.pos[1] - P.pos[1] + 1)**2
        except:
            pass
        try:
            if Board[self.pos[0]][self.pos[1]-1]  == "0" or Board[self.pos[0]][self.pos[1]-1]  == "P":
                dis[3] = (self.pos[0] - P.pos[0] + 1)**2 + (self.pos[1] - P.pos[1])**2
        except:
            pass
            
        if min(dis) == dis[0] :
            self.Move("up")
        elif min(dis) == dis[1]:
            self.Move("left")
        elif min(dis) == dis[2]:
            self.Move("right")
        elif min(dis) == dis[3]:
            self.Move("down")
    
    def kill(self):
        Board[self.pos[0]-1][self.pos[1]-1] = "0"
        del mobs[mobs.index(self)]
        global score
        score += self.worth
        
class Slime(Skull):
    '''
    主角每動兩次之後，這隻怪物才會動一次
    worth 100 points
    '''
    def __init__(self,x,y):
        self.n = 0
        self.pos = (x, y)
        self.symbol = "K"
        self.setpos(x, y)
        self.worth = 100
        mobs.append(self)
        
    def AutoMove(self):
        #available_movements
        if self.n == 1:
            self.n = 0
            self.symbol = "B"
            dis = [1000]*4
            try:
                if Board[self.pos[0]-2][self.pos[1]-1]  == "0" or Board[self.pos[0]-2][self.pos[1]-1]  == "P":
                    dis[0] = (self.pos[0] - P.pos[0] - 1)**2 + (self.pos[1] - P.pos[1])**2
            except:
                pass
            try:
                if Board[self.pos[0]-1][self.pos[1]-2]  == "0" or Board[self.pos[0]-1][self.pos[1]-2]  == "P":
                    dis[1] = (self.pos[0] - P.pos[0])**2 + (self.pos[1] - P.pos[1] - 1)**2
            except:
                pass
            try:
                if Board[self.pos[0]-1][self.pos[1]]  == "0" or Board[self.pos[0]-1][self.pos[1]]  == "P":
                    dis[2] = (self.pos[0] - P.pos[0])**2 + (self.pos[1] - P.pos[1] + 1)**2
            except:
                pass
            try:
                if Board[self.pos[0]][self.pos[1]-1]  == "0" or Board[self.pos[0]][self.pos[1]-1]  == "P":
                    dis[3] = (self.pos[0] - P.pos[0] + 1)**2 + (self.pos[1] - P.pos[1])**2
            except:
                pass

            Board[self.pos[0]-1][self.pos[1]-1] = self.symbol
            if min(dis) == dis[0]:
                self.Move("up")
            elif min(dis) == dis[1]:
                self.Move("left")
            elif min(dis) == dis[2]:
                self.Move("right")
            elif min(dis) == dis[3]:
                self.Move("down")
        else:
            self.n = 1
            self.symbol = 'K'
            Board[self.pos[0]-1][self.pos[1]-1] = self.symbol

class Pig(Skull):
    '''
    這隻怪物會花一步轉彎
    開口方向就是前進方向
    worth 200 points
    '''
    def __init__(self,x,y,d = 0):
        self.dir_sign = ['W','3','E','M']
        self.pos = (x, y)
        self.symbol = self.dir_sign[d]
        self.setpos(x, y)
        self.worth = 200
        mobs.append(self)
        self.lastdir = d
        self.nowdir = 0
    def AutoMove(self):
        #available_movements
        dis = [1000]*4
        try:
            if Board[self.pos[0]-2][self.pos[1]-1]  == "0" or Board[self.pos[0]-2][self.pos[1]-1]  == "P":
                dis[0] = (self.pos[0] - P.pos[0] - 1)**2 + (self.pos[1] - P.pos[1])**2
        except:
            pass
        try:
            if Board[self.pos[0]-1][self.pos[1]-2]  == "0" or Board[self.pos[0]-1][self.pos[1]-2]  == "P":
                dis[1] = (self.pos[0] - P.pos[0])**2 + (self.pos[1] - P.pos[1] - 1)**2
        except:
            pass
        try:
            if Board[self.pos[0]-1][self.pos[1]]  == "0" or Board[self.pos[0]-1][self.pos[1]]  == "P":
                dis[2] = (self.pos[0] - P.pos[0])**2 + (self.pos[1] - P.pos[1] + 1)**2
        except:
            pass
        try:
            if Board[self.pos[0]][self.pos[1]-1]  == "0" or Board[self.pos[0]][self.pos[1]-1]  == "P":
                dis[3] = (self.pos[0] - P.pos[0] + 1)**2 + (self.pos[1] - P.pos[1])**2
        except:
            pass
        
            
        if min(dis) == dis[0]:
            self.nowdir = 0
            self.symbol = self.dir_sign[0]
            Board[self.pos[0]-1][self.pos[1]-1] = self.symbol 
            if self.nowdir == self.lastdir:
                self.Move("up")
            else:
                self.lastdir = self.nowdir
        elif min(dis) == dis[1]:
            self.nowdir = 1
            self.symbol = self.dir_sign[1]
            Board[self.pos[0]-1][self.pos[1]-1] = self.symbol
            if self.nowdir == self.lastdir:
                self.Move("left")
            else:
                self.lastdir = self.nowdir
        elif min(dis) == dis[2]:
            self.nowdir = 2
            self.symbol = self.dir_sign[2]
            Board[self.pos[0]-1][self.pos[1]-1] = self.symbol
            if self.nowdir == self.lastdir:
                self.Move("right")
            else:
                self.lastdir = self.nowdir
        elif min(dis) == dis[3]:
            self.nowdir = 3
            self.symbol = self.dir_sign[3]
            Board[self.pos[0]-1][self.pos[1]-1] = self.symbol
            if self.nowdir == self.lastdir:
                self.Move("down")
            else:
                self.lastdir = self.nowdir

class Octopus(Skull):
    '''
    這隻只會漫無目的橫著走
    遇到障礙就會走另一邊
    '''
    def __init__(self,x,y,d='left'):
        self.pos = (x, y)
        self.symbol = "D"
        self.setpos(x, y)
        self.worth = 150
        mobs.append(self)
        self.dir = d
    def AutoMove(self):
        if self.dir == 'left':
            try:
                if self.pos[1] == 1:
                    self.Move('right')
                    self.dir = 'right'
                elif Board[self.pos[0]-1][self.pos[1]-2]  == "0" or Board[self.pos[0]-1][self.pos[1]-2]  == "P":
                    self.Move('left')
                else:
                    self.Move('right')
                    self.dir = 'right'
            except:
                self.Move('right')
                self.dir = 'right'
        elif self.dir == 'right':
            try:
                if Board[self.pos[0]-1][self.pos[1]]  == "0" or Board[self.pos[0]-1][self.pos[1]]  == "P":
                    self.Move('right')
                else:
                    self.Move('left')
                    self.dir = 'left'
            except:
                self.Move('left')
                self.dir = 'left'

class Stone(Skull):
    '''
    毫無反應
    就是個欠打的廢物
    '''
    def __init__(self,x,y):
        self.pos = (x, y)
        self.symbol = "N"
        self.worth = -50
        self.setpos(x, y)
        mobs.append(self)
    def AutoMove(self):
        pass

class Wall(Stone):
    '''
    障礙物
    打不死 推不動
    '''
    def __init__(self,x,y):
        self.pos = (x, y)
        self.symbol = "S"
        self.setpos(x, y)

def terminate():
    pygame.quit()
    sys.exit()

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key

def showStartScreen():
    while True:
        start = pygame.image.load("start.PNG")
        start = pygame.transform.scale(start, (MAPWIDTH, MAPHEIGHT))
        DISPLAYSURF.blit(start, (0, 0,size*TILESIZE,size*TILESIZE))

        Surf1 = pygame.font.Font('freesansbold.ttf', 12).render('We want A+', True, WHITE)
        Rect1 = Surf1.get_rect()
        Rect1.topleft = (MAPWIDTH -80, 15)
        DISPLAYSURF.blit(Surf1, Rect1)

        
        pressKeySurf = pygame.font.Font('freesansbold.ttf', 18).render('Press any key to play.', True, WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (MAPWIDTH - 200, MAPHEIGHT - 30)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
        if checkForKeyPress():
            return 0
        pygame.display.update()

def showGameOverScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 40)
    Surf1 = titleFont.render('Final Score: '+str(score), True, WHITE, RED)
    Surf2 = titleFont.render('You Died!', True, WHITE, RED)

    while True:

        Rect1 = Surf1.get_rect()
        Rect1.center = (MAPWIDTH / 2, 2*MAPHEIGHT / 5)
        DISPLAYSURF.blit(Surf1, Rect1)

        Rect2 = Surf2.get_rect()
        Rect1.center = (MAPWIDTH / 2, 3*MAPHEIGHT / 5)
        DISPLAYSURF.blit(Surf2, Rect1)

        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        global endless
        pressKeySurf = BASICFONT.render('Press any key to restart level.', True, WHITE, RED) if endless==False else BASICFONT.render('Press any key to restart game.', True, WHITE, RED)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (MAPWIDTH - 265, MAPHEIGHT - 30)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
        if checkForKeyPress():
            return 0
        pygame.display.update()

def showLevelScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 40)
    Surf1 = titleFont.render('You Win!', True, WHITE, RED) if cur!=len(Level)-1 else titleFont.render("You Beat All Our Levels!", True, WHITE, RED)
    Surf2 = titleFont.render("Level "+str(cur+2)+" Next", True, WHITE, RED) if cur!=len(Level)-1 else titleFont.render("Enjoy Endless Mode!", True, WHITE, RED)
    degrees1 = 0
    while True:
        Rect1 = Surf1.get_rect()
        Rect1.center = (MAPWIDTH / 3, 2*MAPHEIGHT / 5) if cur!=len(Level)-1 else (MAPWIDTH / 2, 2*MAPHEIGHT / 5)
        DISPLAYSURF.blit(Surf1, Rect1)

        Rect2 = Surf2.get_rect()
        Rect1.center = (MAPWIDTH / 3, 3*MAPHEIGHT / 5) if cur!=len(Level)-1 else (MAPWIDTH / 2, 3*MAPHEIGHT / 5)
        DISPLAYSURF.blit(Surf2, Rect1)

        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

        pressKeySurf = BASICFONT.render('Press any key to continue.', True, WHITE, RED)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (MAPWIDTH - 240, MAPHEIGHT - 30)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
        if checkForKeyPress():
            return 0
        pygame.display.update()

def showInstructions():
    while True:
        Instructions = pygame.image.load("Instructions.PNG")
        Instructions = pygame.transform.scale(Instructions, (MAPWIDTH, MAPHEIGHT))
        DISPLAYSURF.blit(Instructions, (0, 0, MAPWIDTH, MAPHEIGHT))

        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pressKeySurf = BASICFONT.render('Press any key to play.', True, WHITE)
        pressKeyRect = pressKeySurf.get_rect()
        pressKeyRect.topleft = (MAPWIDTH - 200, MAPHEIGHT - 30)
        DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
        if checkForKeyPress():
            return 0
        pygame.display.update()


Restart()
try:
    showStartScreen()
    showInstructions()
    while True:
        if endless and len(mobs)==0:
            cur+=1
            genMobs(cur)

        if endless==False:
            if P.pos == final:
                showLevelScreen()
                #print("You Win!")
                #print("Score:", score)
                cur += 1
                prev_score = score
                Restart()
                    # 改成跳到下一關
        
        if P.alive == False:
            #print("You Died!")
            showGameOverScreen()
            score = 0
            if endless:
                cur = 0
                endless = False
                score = 0
                Restart()
            elif endless==False:
                Restart()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_t:
                terminate()
            if event.key == pygame.K_r:
                prev_score = score
                Restart()
            if event.key == pygame.K_UP: 
                P.Move("up")
                #PrintBoard(Board)
            if event.key == pygame.K_DOWN: 
                P.Move("down")
                #PrintBoard(Board)
            if event.key == pygame.K_LEFT: 
                P.Move("left")
                #PrintBoard(Board)
            if event.key == pygame.K_RIGHT:
                P.Move("right")
                #PrintBoard(Board)
            event.key = pygame.K_d
        
        for row in range(size):
            for column in range(size):
                DISPLAYSURF.blit( colours['0'], (column*TILESIZE,row*TILESIZE ,TILESIZE,TILESIZE))
        for row in range(size):
            for column in range(size):
                if Board[row][column] != '0':
                    if Board[row][column] == 'P':
                        DISPLAYSURF.blit( colours['P'], (column*TILESIZE - 3 , row*TILESIZE -27  ,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'M' or Board[row][column] =='W' or Board[row][column] =='E' or Board[row][column] =='3':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE , row*TILESIZE -27,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'A':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE, row*TILESIZE -35,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'B':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE-3, row*TILESIZE-27,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'D':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE-3, row*TILESIZE-27,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'S':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE,row*TILESIZE-24,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'F':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'N':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE, row*TILESIZE-19,TILESIZE,TILESIZE))
                    elif Board[row][column] == 'K':
                        DISPLAYSURF.blit( colours[Board[row][column]], (column*TILESIZE-3, row*TILESIZE-27,TILESIZE,TILESIZE))
        pygame.display.update()
except (KeyboardInterrupt):
    #print(endless)
    terminate()
