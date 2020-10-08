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
    wel=Text(Point(5,9),"Welcome to Syracuse University!")#OTXT
    wel.draw(win)
    wel.setTextColor("orange")
    wel.setSize(28)
    wel.setStyle("bold")
    Otto=drawOtto(5,5)
    Otto.draw(win)
    #Calling function makeButton(), returns a boolean tracking mouse position
    otbutton= makeButton(6,4,6.2,3.8,win)#IMS
    while otbutton!= True:
        clickOn=Text(Point(5,1),"click on Otto to continue")
        clickOn.draw(win)
        otbutton= makeButton(6,4,6.2,3.8,win)#FNC
        clickOn.undraw()
    alist=[Otto,wel]#LOOD
    #calling the function clearWin is a for loop that deletes every object in the list
    clearWin(alist)#FNC
    
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
    #button that submits the typed username into the program when clicked
    submit=Text(Point(7.2,7),'submit')
    submit.setSize(14)
    submit.draw(win)
    thelabel=Text(Point(6,7.5),'Insert your username here:')
    thelabel.draw(win)
    button=makeButton(8.3,7.7,7.2,6.8,win)#FNC
    username=userbox.getText()#Getting the typed username
    while button!=True or username=='':#IMS   if the button is not clicked or nothing is written
        sorry= Text(Point(5,5),'make sure to type in your username and click inside the submit box.')
        sorry.setSize(18)
        sorry.draw(win)
        button=makeButton(7.7,6.7,7.1,6.9,win)#FNC
        username=userbox.getText()#Getting the typed username
        sorry.undraw()
    alist= [thelabel,clicker,submit,userbox,Otto]#LOOD
    #clearing the window
    clearWin(alist)
    return username

#uses the username gathered in the last function to say hello to the player
#creates a plot for the game, telling the story of the game
#'gives instructions'
#uses a 'button'
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
    #this is a function made specifically for the location of the Otto picture in this window
    Ottobutton(button2,win)
    #no tracker here
    start=Text(Point(5,1.5),'CLICK ANYWHERE TO START!!!!')
    start.setSize(28)
    start.draw(win)
    win.getMouse()
    alist=[Otto,thestory,thestory1,thestory2,start]#LOOD
    #clearing the window
    clearWin(alist)#FNC
    
#Uses the set location for Otto, and calls the makeButton() function
def Ottobutton(button,win):
    while button!= True:
        text= Text(Point(3,1),'click inside Otto to continue')#OTXT
        text.draw(win)
        #here we call the make Button function inside the function
        button=makeButton(4,2,4.2,1.8,win)#FNC
        text.undraw()

#This function will track where the click was made, and compare it to the bounds
#bx=big x sx=small x by= big y sy= small y
#returns a boolean
def makeButton(bx,sx,by,sy,win):
    click=win.getMouse()#IMS
    cx=click.getX()
    cy=click.getY()
    if cx>=sx and cx<=bx and cy>=sy and cy<=by:
        return True
    else:
        return False
#This function is different than makeButton because it allows for several buttons to be made in the same window, as the value for the mouseclick comes from outside the function.   
def makeButtons(click,bx,sx,by,sy,win):
    cx=click.getX()
    cy=click.getY()
    if cx>=sx and cx<=bx and cy>=sy and cy<=by:
        return True
    else:
        return False
    
#This function will track every object in the list and delete it from the window. It will know also if the object in the list is another list, and delete every object in the other list.   
def clearWin(alist):
    for item in alist:
        if type(item)==list:
            for thing in item:
                thing.undraw()
        else:
            item.undraw()
            
#Function that has the image file of Otto and just draws it.   
def drawOtto(x,y):
    Otto=Image(Point(x,y),'Otto.png')
    return(Otto)

#main game  
def FlappyOtto(win,n,newList):#n is the player level
    lev= Text(Point(9,9),"Level: "+str(n))
    lev.setSize(30)
    lev.setTextColor('orange')
    lev.draw(win)
    miniOtto=Image(Point(0.7,5),'tinyOtto.png')
    boundaries=Rectangle(Point(0.3,4.5),Point(1.2,5.5))#otto's right x position is always 1.2
    boundaries.setOutline(color_rgb(135,195,255))
    flappy=[boundaries,miniOtto]
    difficulty=Difficulty(n)#CLOD
    for item in flappy:
        item.draw(win)
    level=difficulty.getLevel()#USES CLASS TO GET THE DISTANCE BETWEEN THE PIPES
    cranes,obstacles,cdome=drawObstacles(win,level)#FNC draws all the pipes and cranes, returns lists of obstacles
    direction=difficulty.getSpeed()#USES CLASS TO FIND HOW FAST THE IMAGE WILL MOVE UP AND DOWN WITH EVERY CLICK
    instructions=Text(Point(5,5),"use Up and Down arrow keys to move Otto Up and Down.")#game instructions
    instructions.setSize(20)
    instructions.draw(win)
    win.getKey()
    instructions.undraw()
    everything=[lev,cdome,flappy,cranes,obstacles]
    crash=False #setting default parameter to False
    while crash!=True:#while loop that knows when to stop the game. while moveItems() returns False, the game keeps going
        ndirection=setDirection(win,direction)
        crash=moveItems(flappy,obstacles,ndirection,cdome,cranes,win)#FNC returns either False, True or winner
        if crash=='winner':#if the function returns winner, the window goes to the func "youWon()"
            clearWin(everything)
            newn=youWon(win,n,newList)#FNC returns the new value of n (n+1), because the player can move on to the next level. 
            return(newn)
    clearWin(everything)
    newn=youLost(win,n,newList)#FNC if the function returns True, it goes to the window 'you lost', returns the same value of n, still set to the variable newn
    return(newn)#function returns newn which is the level the player left off at.


def drawObstacles(win,level):#draws the obstacles at the separation given by the class Difficulty at a random height. 
    x=4
    cranes=[]
    obstacles=[]
    for i in range(15):#Draws 15 sets of obstacles= 30 pipes total including upper and lower. 
        y=randrange(1,6)#RND
        lobstacle=Rectangle(Point(x,0),Point(x+1,y))#lower pipes 
        uobstacle=Rectangle(Point(x,10),Point(x+1,y+2))#upper pipes
        lcrane=Image(Point(x+.5,y//2),'crane.png')#crane image lower
        ucrane=Image(Point(x+.5,(12+y)/2),'crane.png')#crane image upper
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
    dome=Circle(Point(x+3,5),1)#draws a circle around the dome photo
    dome.setOutline(color_rgb(135,195,255))
    dome.draw(win)
    cdome=Image(Point(x+3,5),'dome.png')#draws the photo of the dome
    cranes.append(cdome)
    cranes.append(dome)
    cdome.draw(win)
    
    return cranes,obstacles,cdome

    
    
def moveItems(flappy,obstacles,ndirection,cdome,cranes,win):#moves all the obstacles at the same time
        for item in flappy:
            item.move(0,ndirection)#tracking the position of the Otto image and its boundaries. Moving Otto up or down with value given by setDirection()
        position=flappy[0]
        birdsmally,birdbigy=Bump(position)#FNC calls Bump which returns the small y and big y values of flappy at all times
        x=0
        for item in obstacles:
            item.move(-0.4,0)#always moving all the obstacles at a rate of -0.4
            upperright=item.getP2()#getting the upper right position of every item in obstacles
            obsbx=upperright.getX()#getting the x upper right position for every item 
            obsby=upperright.getY()#getting the y upper right position
            lowerleft=item.getP1()#getting the lower left position 
            obssx=lowerleft.getX()#lower left x
            obssy=lowerleft.getY()#lower left y
            if obsbx<=2.2 and obsbx>=1.2:#if the obstacles is at the upper right x position between 2.2 and 1.2
                if obssy==10:#if the small y is 10, meaning all upper pipes
                    if birdbigy>=obsby:#if the bird's upper right position y is bigger than the upper obstacle's lower left y position, there has been a crash i the top
                        print('top crash')
                        return True                        
                if obssy==0:# if the small y is 0, meaning all the lower pipes
                    if birdsmally<=obsby:#if the bird's lower left position is smaller than the lower pipe's upper right position there has been a crash
                        print('bumped into the bottom')
                        return True
        for item in cranes:
            item.move(-0.4,0)
            if cranes[-1].getP2().getX()>=1.2 and cranes[-1].getP2().getX()<=2.2:#if the lst object of the list cranes (a circle around the dome image) reaches the position between 1.2 and 2.2 (where the Otto image is)
                return('winner')#there has been a winner, can proceed to next level
            
#this function appears only if the moveItems() function returns "True"
def youLost(win,n,newList):
    win.setBackground('red')
    youbump= Text(Point(5,7),'oops...you crashed into Walt the Crane\n\nYOU LOST')#OTXT
    youbump.setSize(24)
    recent= Rectangle(Point(2,4),Point(4.2,4.4))
    recent.setFill('white')
    rtext=Text(Point(3.1,4.2),"SHOW RECENT PLAYERS")#button that shows the previous recent player list
    exits= Rectangle(Point(3.5,3),Point(6.5,3.4))
    exits.setFill('white')
    etext=Text(Point(5,3.2),"EXIT GAME")#button to exit the game
    newgame= Rectangle(Point(6,4),Point(8.2,4.4))
    newgame.setFill('white')
    ntext=Text(Point(7.1,4.2),'NEW GAME')#button to start a new game in the same level
    items=[youbump,recent,exits,newgame,rtext,etext,ntext]
    for item in items:
        item.draw(win)
    winButtons(win,n,newList,items)# FNC gets all the buttons working
    return n
#this function appears only if the moveItems() function returns "winner" 
def youWon(win,n,newList):
    if n==5:#if the player has already reached the last level, the function will always return false
        n=4
    n+=1#otherwise the function will return the previous n plus 1
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
    winButtons(win,n,newList,items)#gets all the buttons working
    return n
        
def winButtons(win,n,newList,items):#gets all the buttons in the youWon() and youLost() functions working 
    click=win.getMouse()#tracks position of clicker IMS
    eclick=makeButtons(click,6.5,3.5,3.4,3,win)#calls function makeButtons, return a Boolean
    nclick=makeButtons(click,8.2,6,4.4,4,win)
    reclick=makeButtons(click,4.2,2,4.4,4,win)
    while not(eclick or nclick or reclick): #can click anywhere as many times as you want, doesnt do anything unless you click inside a button
            click=win.getMouse()#gets the position again
            eclick=makeButtons(click,6.5,3.5,3.4,3,win)#looking for boolean
            nclick=makeButtons(click,8.2,6,4.4,4,win)
            reclick=makeButtons(click,4.2,2,4.4,4,win)
    if reclick==True:#if the button for recent players is clicked, the recent players are displayed
            objects=DisplayRPlayers(win,newList)
            items.append(objects)
            while not(eclick or nclick): #nothing happens unless another button is clicked
                click=win.getMouse()
                eclick=makeButtons(click,6.5,3.5,3.4,3,win)
                nclick=makeButtons(click,8.2,6,4.4,4,win)       
    if eclick==True:#exits the game
            win.close()
    elif nclick==True:#starts a new game with tha value "n" given by the previous game
            clearWin(items)
            win.setBackground(color_rgb(135,195,255))
            n=FlappyOtto(win,n,newList)
   
def Bump(position):#gets the position for an object used for the bird. Breaks it down to the lower left and upper right y values
    lowerleft=position.getP1()
    upperright=position.getP2()
    sy=lowerleft.getY()
    bx=upperright.getX()
    by=upperright.getY() 
    return(sy,by)
        
    
    
class Difficulty:#CLOD
    def __init__(self,level,dir=1):
        self.level=level
        self.dir=dir
        
    def getLevel(self):#depending on the "level" given by the Flappy Otto function it sets the distance between the pipes
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
    
    def getSpeed(self):#depending on the level given, it returns the speed at which the Otto image moves up or down with every arrow key press. 
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
        
def setDirection(win,direction):#changes the direction of OTTO, deppending on which arrow key is pressed. 
    key= win.checkKey()
    if key=='Down' and direction>0:#if the key pressed is down, and the direction is positive, then set direction to negative
        direction=direction*-1
    elif key=='Down' and direction<0:#if the key pressed is down and the direction is negative, then keep negative
        direction=direction
    elif key=='Up' and direction<0:#if the key pressed is up and the direction is negative, then set to positive
        direction=direction*-1
    elif key=='Up' and direction>0:#if the key is up and the direction is positive, keep positive
        direction=direction
    else:
        direction=direction*0#OTHERWISE DONT MOVE
    return direction
           
def playerLevel(username,recentPlayers,outfile):#gets the level of each player from the list gotten from the infile or sets level to 1
    newList=[]
    for item in recentPlayers:#takes away all empty characters and puts all values in a new List "cleanup"
        r=item.strip()
        newList.append(r)
    for item in newList:#still cleaning up empty characters
        if item=='':
            newList.remove(item)
    if newList!=[]:#if the list is not empty
        i=0
        while i<len(newList) and newList[i]!=username:
            i+=1
        if i>=len(newList):
            i=len(newList)-1
        if newList[i]==username:#if a value in the new list is equal to the value of the entered username
            user=str(newList.pop(i))
            lev=int(newList.pop(i))
            return(lev,newList)#return that user's previous level
        else:
            return(1,newList)#if the list is not empty and the username is not in the list

    else:#if the list is empty
        return(1,newList)#just return 1
    
def printToFile(outfile,newList,username,newn):#prints the new username and the level at which they left off when they finish to the outfile
    newList.insert(0,newn)
    newList.insert(0,username)
    for item in newList:
        print(item,file=outfile)#OFL

def DisplayRPlayers(win,newList):#makes a tiny box at the top of the window displaying the recent players.
    z=9.5
    objects=[]
    for item in newList:
        z+=-.2
    playerbox=Rectangle(Point(6,z),Point(9,9.7))
    objects.append(playerbox)
    playerbox.setFill('white')
    playerbox.draw(win)
    y=9.5
    for i in range(0,len(newList),2):
        player=Text(Point(7,y),newList[i])
        level=Text(Point(8,y),"Level: "+newList[i+1])
        objects.append(player)
        objects.append(level)
        player.draw(win)
        level.draw(win)
        y+=-.2
    return objects #return a list of the objects drawn with this function, so that they can be deleted later.
    

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
    #This function prints text and other obj to the window, and uses a 'button'
    Welcome(win)#FNC
    #This function prints obj to the window, gets the username from an EntryBox and uses 'button' returns the username
    username=Username(win)#FNC
    storyLine(win,username)#FNC
    win.setBackground(color_rgb(135,195,255))#recheck color later
    outfile=open("recentPlayers.txt",'w')#OFL
    n,newList=playerLevel(username,recentPlayers,outfile)#FNC
    newn=FlappyOtto(win,n,newList)#FNC
    printToFile(outfile,newList,username,newn)#FNC
    outfile.close()
main()#END OF MAIN
