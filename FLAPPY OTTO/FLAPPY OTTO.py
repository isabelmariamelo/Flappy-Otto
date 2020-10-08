#Flappy Otto
#FlappyOtto.py
#name: ISABEL MELO
#Nickname: Liz
#Lab section: M5
#SU Login name: immelo

#opens the window, click to move to next window
#makebutton function done
#imports Otto
#function clearWin done
#username window done
#got Class Difficulty working!
#movement working
#otto moves up and down
#pipes move to the left
#winner  loser identifiable
#levels identifiable
#buttons to exit game, next level, new game done
#recent players done

from graphics import *
from random import randrange
    
def Welcome(win):#builds the first window of the program (Welcome screen)
    wel=Text(Point(5,9),"Welcome to Syracuse University!")
    wel.draw(win)
    wel.setTextColor("orange")
    wel.setSize(28)
    wel.setStyle("bold")
    Otto=drawOtto(5,5)
    Otto.draw(win)
    otbutton= makeButton(6,4,6.2,3.8,win)
    while otbutton!= True:
        clickOn=Text(Point(5,1),"click on Otto to continue")
        clickOn.draw(win)
        otbutton= makeButton(6,4,6.2,3.8,win)
        clickOn.undraw()
    alist=[Otto,wel]
    clearWin(alist)
    
#uses interactive input to get the username of the user. Uses entry box and 
def Username(win):
    #getting the username for the user
    Otto=drawOtto(3,3)
    Otto.draw(win)
    userbox=Entry(Point(5.5,7),15)#IEB
    userbox.draw(win)
    clicker= Rectangle(Point(6.7,6.8),Point(7.7,7.2))
    clicker.setFill('red')
    clicker.draw(win)
    #button that submits the typed username into the program
    submit=Text(Point(7.2,7),'submit')
    submit.setSize(14)
    submit.draw(win)
    thelabel=Text(Point(6,7.5),'Insert your username here:')
    thelabel.draw(win)
    button=makeButton(8.3,7.7,7.2,6.8,win)
    username=userbox.getText()
    while button!=True or username=='':#IMS
        sorry= Text(Point(5,5),'make sure to type in your username and click inside the submit box.')
        sorry.setSize(18)
        sorry.draw(win)
        button=makeButton(7.7,6.7,7.1,6.9,win)
        username=userbox.getText()
        sorry.undraw()
    alist= [thelabel,clicker,submit,userbox,Otto]
    clearWin(alist)
    return username

def storyLine(win,username):
    Otto=drawOtto(3,3)
    Otto.draw(win)
    story= "Hello, "+username.upper()+" it is your lucky day!\nYou get to play Otto in tonight's game"
    thestory= Text(Point(6,9),story)
    thestory.setSize(24)
    thestory.draw(win)
    button=makeButton(4,2,4.2,1.8,win)
    Ottobutton(button,win)
    thestory1=Text(Point(6,7), "Go put on your costume and get to the Dome\n ASAP!")
    thestory1.setSize(24)
    thestory1.draw(win)
    button1=makeButton(4,2,4.2,1.8,win)
    Ottobutton(button1,win)
    thestory2=Text(Point(6,5),"...AND make sure not to crash into walt the crane!")
    thestory2.setSize(24)
    thestory2.draw(win)
    button2=makeButton(4,2,4.2,1.8,win)
    Ottobutton(button2,win)
    start=Text(Point(5,1.5),'CLICK ANYWHERE TO START!!!!')
    start.setSize(28)
    start.draw(win)
    win.getMouse()
    alist=[Otto,thestory,thestory1,thestory2,start]
    clearWin(alist)
    

def Ottobutton(button,win):
    while button!= True:
        text= Text(Point(3,1),'click inside Otto to continue')
        text.draw(win)
        button=makeButton(4,2,4.2,1.8,win)
        text.undraw()
        
def makeButton(bx,sx,by,sy,win):
    click=win.getMouse()
    cx=click.getX()
    cy=click.getY()
    if cx>=sx and cx<=bx and cy>=sy and cy<=by:
        return True
    else:
        return False
    
def makeButtons(click,bx,sx,by,sy,win):
    cx=click.getX()
    cy=click.getY()
    if cx>=sx and cx<=bx and cy>=sy and cy<=by:
        return True
    else:
        return False
    
def clearWin(alist):
    for item in alist:
        if type(item)==list:
            for thing in item:
                thing.undraw()
        else:
            item.undraw()
    
def drawOtto(x,y):
    Otto=Image(Point(x,y),'Otto.png')
    return(Otto)
    
def FlappyOtto(win,n,newList):
    lev= Text(Point(9,9),str(n))
    lev.setSize(30)
    lev.setTextColor('orange')
    lev.draw(win)
    miniOtto=Image(Point(0.7,5),'tinyOtto.png')
    boundaries=Rectangle(Point(0.3,4.5),Point(1.2,5.5))#otto's right x position is always 1.2
    boundaries.setOutline(color_rgb(135,195,255))
    flappy=[boundaries,miniOtto]
    difficulty=Difficulty(n)
    for item in flappy:
        item.draw(win)
    level=difficulty.getLevel()
    cranes,obstacles,cdome=drawObstacles(win,level)
    direction=difficulty.getSpeed()
    instructions=Text(Point(5,5),"use Up and Down arrow keys to move Otto Up and Down.")
    instructions.setSize(20)
    instructions.draw(win)
    win.getKey()
    instructions.undraw()
    everything=[lev,cdome,flappy,cranes,obstacles]
    crash=False
    while crash!=True:
        ndirection=setDirection(win,direction)
        crash=moveItems(flappy,obstacles,ndirection,cdome,cranes,win)
        if crash=='winner':
            clearWin(everything)
            newn=youWon(win,n,newList)
            return(newn)
    clearWin(everything)
    newn=youLost(win,n,newList)
    return(newn)

def drawObstacles(win,level):
    x=4
    cranes=[]
    obstacles=[]
    for i in range(25):
        y=randrange(1,6)
        lobstacle=Rectangle(Point(x,0),Point(x+1,y))
        uobstacle=Rectangle(Point(x,10),Point(x+1,y+2))
        lcrane=Image(Point(x+.5,y//2),'crane.png')
        ucrane=Image(Point(x+.5,(12+y)/2),'crane.png')
        cranes.append(lcrane)
        cranes.append(ucrane)
        obstacles.append(lobstacle)
        obstacles.append(uobstacle)
        lobstacle.setFill('green')
        uobstacle.setFill('green')
        lobstacle.draw(win)
        uobstacle.draw(win)
        lcrane.draw(win)
        ucrane.draw(win)
        x+=level
    dome=Circle(Point(x+3,5),1)
    dome.setOutline(color_rgb(135,195,255))
    dome.draw(win)
    cdome=Image(Point(x+3,5),'dome.png')
    cranes.append(cdome)
    cranes.append(dome)
    cdome.draw(win)
    
    return cranes,obstacles,cdome

    
    
def moveItems(flappy,obstacles,ndirection,cdome,cranes,win):
        for item in flappy:
            item.move(0,ndirection)
        position=flappy[0]
        birdsmally,birdbigy=Bump(position)
        x=0
        for item in obstacles:
            item.move(-0.5,0)
            upperright=item.getP2()
            obsbx=upperright.getX()
            obsby=upperright.getY()
            lowerleft=item.getP1()
            obssx=lowerleft.getX()
            obssy=lowerleft.getY()
            if obsbx<=2.2 and obsbx>=1.2:
                if obssy==10:
                    if birdbigy>=obsby:
                        print('top crash')
                        print(birdbigy)
                        print(obssy)
                        return True                        
                if obssy==0:
                    if birdsmally<=obsby:
                        print('bumped into the bottom')
                        print(birdsmally)
                        print(obsby)
                        return True
        for item in cranes:
            item.move(-0.5,0)
            if cranes[-1].getP2().getX()>=1.2 and cranes[-1].getP2().getX()<=2.2:
                return('winner')
            
def youLost(win,n,newList):
    win.setBackground('red')
    youbump= Text(Point(5,7),'oops...you crashed into Walt the Crane\n\nYOU LOST')
    youbump.setSize(24)
    recent= Rectangle(Point(2,4),Point(4.2,4.4))
    recent.setFill('white')
    rtext=Text(Point(3.1,4.2),"SHOW RECENT PLAYERS")
    exits= Rectangle(Point(3.5,3),Point(6.5,3.4))
    exits.setFill('white')
    etext=Text(Point(5,3.2),"EXIT GAME")
    newgame= Rectangle(Point(6,4),Point(8.2,4.4))
    newgame.setFill('white')
    ntext=Text(Point(7.1,4.2),'NEW GAME')
    items=[youbump,recent,exits,newgame,rtext,etext,ntext]
    for item in items:
        item.draw(win)
    winButtons(win,n,newList,items)
    return n

def youWon(win,n,newList):
    if n==5:
        n=4
    n+=1
    win.setBackground('green')
    youbump= Text(Point(5,7),'YAY YOU MADE IT IN TIME')
    youbump.setSize(24)
    recent= Rectangle(Point(2,4),Point(4.2,4.4))
    recent.setFill('white')
    rtext=Text(Point(3.1,4.2),"SHOW RECENT PLAYERS")
    exits= Rectangle(Point(3.5,3),Point(6.5,3.4))
    exits.setFill('white')
    etext=Text(Point(5,3.2),"EXIT GAME")
    newgame= Rectangle(Point(6,4),Point(8.2,4.4))
    newgame.setFill('white')
    ntext=Text(Point(7.1,4.2),'PROCEED TO NEXT LEVEL')
    items=[youbump,recent,exits,newgame,rtext,etext,ntext]
    for item in items:
        item.draw(win)
    winButtons(win,n,newList,items)
    return n
        
def winButtons(win,n,newList,items):
    click=win.getMouse()
    eclick=makeButtons(click,6.5,3.5,3.4,3,win)
    nclick=makeButtons(click,8.2,6,4.4,4,win)
    reclick=makeButtons(click,4.2,2,4.4,4,win)
    while not(eclick or nclick or reclick): 
            click=win.getMouse()
            eclick=makeButtons(click,6.5,3.5,3.4,3,win)
            nclick=makeButtons(click,8.2,6,4.4,4,win)
            reclick=makeButtons(click,4.2,2,4.4,4,win)
    if reclick==True:
            objects=DisplayRPlayers(win,newList)
            items.append(objects)
            while not(eclick or nclick): 
                click=win.getMouse()
                eclick=makeButtons(click,6.5,3.5,3.4,3,win)
                nclick=makeButtons(click,8.2,6,4.4,4,win)       
    if eclick==True:
            win.close()
    elif nclick==True:
            clearWin(items)
            win.setBackground(color_rgb(135,195,255))
            n=FlappyOtto(win,n,newList)
   
def Bump(position):
    lowerleft=position.getP1()
    upperright=position.getP2()
    sy=lowerleft.getY()
    bx=upperright.getX()
    by=upperright.getY() 
    return(sy,by)
        
    
    
class Difficulty:
    def __init__(self,level,dir=1):
        self.level=level
        self.dir=dir
        
    def getLevel(self):
        if self.level==1:
            self.level=6
        elif self.level==2:
            self.level=5          
        elif self.level==3:
            self.level=4         
        elif self.level==4:
            self.level=3
        elif self.level==5:
            self.level=2.7
        return self.level
    
    def getSpeed(self):
        if self.level==1:
            self.dir=1
        elif self.level==2:
            self.dir=1.1
        elif self.level==3:
            self.dir=1.2
        elif self.level==4:
            self.dir==1.3
        elif self.level==5:
            self.dir==1.4
        return self.dir
        
def setDirection(win,direction):
    key= win.checkKey()
    if key=='Down' and direction>0:
        direction=direction*-1
    elif key=='Down' and direction<0:
        direction=direction*1
    elif key=='Up' and direction<0:
        direction=direction*-1
    elif key=='Up' and direction>0:
        direction=direction*1
    else:
        direction=direction*0
    return direction
           
def playerLevel(username,recentPlayers,outfile):
    newList=[]
    for item in recentPlayers:
        r=item.strip()
        newList.append(r)
    for item in newList:
        if item=='':
            newList.pop(item)
    if newList!=[]:
        i=0
        while i<=len(newList):
            if newList[i]==username:
                return(int(newList[i+1]),newList)
            else:
                return(1,newList)
            i+=1
    else:
        return(1,newList)
    
def printToFile(outfile,newList,username,newn):
    newList.insert(0,newn)
    newList.insert(0,username)
    for item in newList:
        print(item,file=outfile)

def DisplayRPlayers(win,newList):
    y=9.5
    objects=[]
    for item in newList:
        player=Text(Point(7,y),item)
        objects.append(player)
        player.draw(win)
        y+=-.2
    return objects
    

def main():#MAINNNNNNNN
    #Opening the window
    win= GraphWin("Flappy Otto",700,700)#GW
    #reading from recent players input file and exporting it to a List
    infile=open('recentPlayers.txt','r')
    recentPlayers=infile.readlines()#IFL
    #closing the recent players input file
    infile.close()
    win.setCoords(0,0,10,10)
    win.setBackground('white')
    #This function makes 
    Welcome(win)
    username=Username(win)
    storyLine(win,username)
    win.setBackground(color_rgb(135,195,255))#recheck color later
    outfile=open("recentPlayers.txt",'w')
    n,newList=playerLevel(username,recentPlayers,outfile)
    newn=FlappyOtto(win,n,newList)
    printToFile(outfile,newList,username,newn)
    outfile.close()
main()
