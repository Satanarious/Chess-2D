#############################################################################################################################################################################################
#                                                                                                                                                                                           #
#                                                                         ██████╗██╗  ██╗███████╗███████╗███████╗                                                                           #
#                                                                        ██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝                                                                           #
#                                                                        ██║     ███████║█████╗  ███████╗███████╗                                                                           #
#                                                                        ██║     ██╔══██║██╔══╝  ╚════██║╚════██║                                                                           #
#                                                                        ╚██████╗██║  ██║███████╗███████║███████║                                                                           #
#                                                                         ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝                                                                           #
#                                                                                                                -By Satyam                                                                 #
#############################################################################################################################################################################################
from tkinter import *
from tkinter import messagebox
import pygame
import sys
checkwho=[]                          #Indices of pieces that check the King(Global declaration)
castle={'W':[0,0,0],'B':[0,0,0]}     #Flags for castling(Global declaration)
kill_list={'W':[],'B':[]}             #Killed pieces(Global declaration)
class Promote(object):
    def __init__(self, one,title, message):
        self.base = Toplevel()
        self.base.title(title)
        self.label1 =Label(self.base, text=message)
        self.label1.grid(row=0,column=0,columnspan=4)
        self.button1 =Button(self.base, command=self.queen)
        self.photo1=PhotoImage(file=stack[one+'Q'])
        self.button1.config(image=self.photo1,width="85",height="85")
        self.button1.grid(row=1,column=0,padx=5,)
        self.button2 =Button(self.base,  command=self.rook)
        self.photo2=PhotoImage(file=stack[one+'R'])
        self.button2.config(image=self.photo2,width="85",height="85")
        self.button2.grid(row=1,column=1,padx=5)
        self.button3 =Button(self.base,command=self.knight)
        self.photo3=PhotoImage(file=stack[one+'N'])
        self.button3.config(image=self.photo3,width="85",height="85")
        self.button3.grid(row=1,column=2,padx=5)
        self.button4 =Button(self.base,  command=self.bishop)
        self.photo4=PhotoImage(file=stack[one+'B'])
        self.button4.config(image=self.photo4,width="85",height="85")
        self.button4.grid(row=1,column=3,padx=5)
        self.label2 =Label(self.base, text="Note: Closing this pop-up will promote Pawn to Queen(Default)")
        self.label2.grid(row=2,column=0,columnspan=4)
        self.base.geometry('405x160+540+340')
        self.base.resizable(False, False)
        self.base.protocol("WM_DELETE_WINDOW",self.queen)
    def rook(self):
        a[coord[0]][coord[1]]=one+'R'
        self.base.destroy()
    def queen(self):
        a[coord[0]][coord[1]]=one+'Q'
        self.base.destroy()
    def knight(self):
        a[coord[0]][coord[1]]=one+'N'
        self.base.destroy()
    def bishop(self):
        a[coord[0]][coord[1]]=one+'B'
        self.base.destroy()
    def destroy(self):
        self.base.wait_window()
        self.base.destroy()
def myking(one):                    #Position of the king
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j]==one+'K'):
                return(i,j)
def ind(two,pawn):                       #Indices of opponent pieces except pawns
    b=[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j][0]==two and a[i][j][1]!='P' and pawn==False):
                b.append((i,j))
            elif(a[i][j][0]==two and pawn==True):
                b.append((i,j))
    return(b)
def castle_check(coord,dc):               #Setting flags for castling
    if(a[coord[0]][coord[1]]=='WR' and dc[0]==7 and coord[1]==0):
        castle['W'][0]=1
    elif(a[coord[0]][coord[1]]=='WR' and dc[0]==7 and dc[1]==7):
        castle['W'][1]=1
    elif(a[coord[0]][coord[1]]=='BR' and dc[0]==0 and dc[1]==0):
        castle['B'][0]=1
    elif(a[coord[0]][coord[1]]=='BR' and dc[0]==0 and dc[1]==7):
        castle['B'][1]=1
    elif(a[coord[0]][coord[1]]=='WK' and dc[0]==7 and dc[1]==4):
        castle['W'][2]=1
    elif(a[coord[0]][coord[1]]=='BK' and dc[0]==0 and dc[1]==4):
        castle['B'][2]=1
def blocks(a,p,p1,p2,r1,c1):         #Move Palete assignment
    bl=[]
    def rook(r1,c1):                 #Rook move palete fxn
        bl=[]
        r,c=r1,c1
        while(r<8):
            r+=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        r=r1
        while(r>1):
            r-=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        r=r1
        while(c<8):
            c+=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        c=c1
        while(c>1):
            c-=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        return(bl)
    def bishop(r1,c1):                #Bishop move palete fxn
        bl=[]
        r,c=r1,c1
        while(r<8 and c<8):
            r+=1
            c+=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        r,c=r1,c1
        while(r>1 and c>1):
            r-=1
            c-=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        r,c=r1,c1
        while(r<8 and c>1):
            r+=1
            c-=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        r,c=r1,c1
        while(r>1 and c<8):
            r-=1
            c+=1
            if(a[8-r][c-1][0]==p2):
                bl.append(chr(r+64)+str(c))
                break
            elif(a[8-r][c-1][0]==p1):
                break
            else:
                bl.append(chr(r+64)+str(c))
        return(bl)
    if(p=="BR" or p=="WR"):          #Rook move palete
        return(rook(r1,c1))
    elif(p=="BN" or p=="WN"):        #Knight move palete
        if(c1-1<9):
            bl.append(chr(r1+2+64)+str(c1-1))
            bl.append(chr(r1-2+64)+str(c1-1))
        if(c1+1<9):
            bl.append(chr(r1+2+64)+str(c1+1))
            bl.append(chr(r1-2+64)+str(c1+1))
        if(c1-2<9):
            bl.append(chr(r1-1+64)+str(c1-2))
            bl.append(chr(r1+1+64)+str(c1-2))
        if(c1+2<9):
            bl.append(chr(r1-1+64)+str(c1+2))
            bl.append(chr(r1+1+64)+str(c1+2))
        for i in range(len(bl)):
            try:
                if not(ord(bl[i][0])>64 and ord(bl[i][0])<73 and int(bl[i][1])>0 and int(bl[i][1])<9):      #Removing unwanted blocks from palete
                    bl[i]=0
            except ValueError:
                bl[i]=0
        bl=list(filter(lambda a: a != 0, bl))
        for i in range(len(bl)):
            if(a[8-(ord(bl[i][0])-64)][(int(bl[i][1])-1)][0]==p1):
                bl[i]=0
        bl=list(filter(lambda a: a != 0, bl))
        return(bl)
    elif(p=="BB" or p=="WB"):        #Bishop move palete
        return(bishop(r1,c1))
    elif(p=="WP"):                   #White Pawn move palete
        if (r1+65)==67:
            if(a[8-r1-1][c1-1][0]!=p2 and a[8-r1-1][c1-1][0]!=p1):
                bl.append(chr(r1+64+1)+str(c1))
                if(a[8-r1-2][c1-1][0]!=p2 and a[8-r1-2][c1-1][0]!=p1):
                    bl.append(chr(r1+64+2)+str(c1))
            try:
                if(a[8-r1-1][c1+1-1][0]==p2):
                    bl.append(chr(r1+64+1)+str(c1+1))
            except:
                pass
            try:
                if(a[8-r1-1][c1-1-1][0]==p2):
                    bl.append(chr(r1+64+1)+str(c1-1))
            except:
                pass
        elif (r1+65)<73:
            if(a[8-r1-1][c1-1][0]!=p2 and a[8-r1-1][c1-1][0]!=p1):
                bl.append(chr(r1+64+1)+str(c1))
            try:
                if(a[8-r1-1][c1+1-1][0]==p2):
                    bl.append(chr(r1+64+1)+str(c1+1))
            except:
                pass
            try:
                if(a[8-r1-1][c1-1-1][0]==p2):
                    bl.append(chr(r1+64+1)+str(c1-1))
            except:
                pass
        return(bl)
    elif(p=="BP"):                   #Black Pawn move palete
        if(r1+65==72):
            if(a[8-r1+1][c1-1][0]!=p2 and a[8-r1+1][c1-1][0]!=p1):
                bl.append(chr(r1+64-1)+str(c1))
                if(a[8-r1+2][c1-1][0]!=p2 and a[8-r1+2][c1-1][0]!=p1):
                    bl.append(chr(r1+64-2)+str(c1))
            try:
                if(a[8-r1+1][c1-1-1][0]==p2):
                    bl.append(chr(r1+64-1)+str(c1-1))
            except:
                pass
            try:
                if(a[8-r1+1][c1+1-1][0]==p2):
                    bl.append(chr(r1+64-1)+str(c1+1))
            except:
                pass
        elif (r1+65)>65:
            if(a[8-r1+1][c1-1][0]!=p2 and a[8-r1+1][c1-1][0]!=p1):
                bl.append(chr(r1+64-1)+str(c1))
            try:
                if(a[8-r1+1][c1-1-1][0]==p2):
                    bl.append(chr(r1+64-1)+str(c1-1))
            except:
                pass
            try:
                if(a[8-r1+1][c1+1-1][0]==p2):
                    bl.append(chr(r1+64-1)+str(c1+1))
            except:
                pass
        return(bl)
    elif(p=="BQ" or p=="WQ"):        #Queen move palete
        return(bishop(r1,c1)+rook(r1,c1))
    elif(p=="BK" or p=="WK"):        #King move palete
        bl.append(chr(r1+64+1)+str(c1))
        bl.append(chr(r1+64-1)+str(c1))
        bl.append(chr(r1+64-1)+str(c1-1))
        bl.append(chr(r1+64)+str(c1-1))
        bl.append(chr(r1+64+1)+str(c1-1))
        bl.append(chr(r1+64-1)+str(c1+1))
        bl.append(chr(r1+64)+str(c1+1))
        bl.append(chr(r1+64+1)+str(c1+1))
        for i in range(len(bl)):
            try:
                if not(ord(bl[i][0])>64 and ord(bl[i][0])<73 and int(bl[i][1])>0 and int(bl[i][1])<9):    #Removing unwanted blocks from palete
                    bl[i]=0
            except ValueError:
                bl[i]=0
        bl=list(filter(lambda a: a != 0, bl))
        coord=block_find(pos)
        kr,kc=myking(one)
        for i in range(len(bl)):
            if(a[(8-ord(bl[i][0])+64)][(int(bl[i][1])-1)][0]==p1):
                bl[i]=0
        bl=list(filter(lambda a: a != 0, bl))
        return(bl)
def king_moves(one,two):            #Check if King's blocks are all checked
    kr,kc=myking(one)
    count=0
    kingpath=blocks(a,one+'K',one,two,8-kr,kc+1)
    for i in kingpath:
        temp=a[(8-ord(i[0])+64)][int(i[1])-1]
        a[(8-ord(i[0])+64)][int(i[1])-1]=one+'K'
        a[kr][kc]="  "
        if(chcheck(one,two)):
            count+=1
        a[kr][kc]=one+'K'
        a[(8-ord(i[0])+64)][int(i[1])-1]=temp
    if not(count==len(kingpath)):
        return(False)
    else:
        return(True)
def plnum(ch):                       #Player number
    if(chance(ch)==p1):
        return("Player 1:")
    else:
        return("Player 2:")
def borw(a):                         #Letting user known of the colour selected randomly
    if(a=='B'):
        return("Black")
    else:
        return("White")
def chance(ch) :                     #Comprehending black or white turn
    if(ch%2 != 0):
        return('W')
    else:
        return('B')
def stalemate(one,two):             #Check for Stalemate
    for i in ind(one,True):
        if not(a[(i[0])][(i[1])]==one+'K'):
            if(blocks(a,a[(i[0])][(i[1])],one,two,8-i[0],i[1]+1)==[]):
                continue
            else:
                return(False)
        else:
            if(king_moves(one,two)==False):
                return(False)
def chcheck(one,two):               #Check for if King is checked
        global checkwho
        checkwho=[]
        kr,kc=myking(one)
        if(one=='W'):
            try:
                if(a[kr-1][kc-1]==two+'P'):
                    checkwho.append((kr-1,kc-1))
                if(a[kr-1][kc+1]==two+'P'):
                    checkwho.append((kr-1,kc+1))
            except:
                pass
        elif(one=='B'):
            try:
                if(a[kr+1][kc-1]==two+'P'):
                    checkwho.append((kr+1,kc-1))
                if(a[kr+1][kc+1]==two+'P'):
                    checkwho.append((kr+1,kc+1))
            except:
                pass
        for i in ind(two,False):
            if(chr(8-kr+64)+str(kc+1) in blocks(a,a[(i[0])][i[1]],two,one,8-i[0],i[1]+1)):
                checkwho.append(i)
        if(checkwho==[]):
            return(False)
        else:
            return(True)
def chcheckmate(one,two):           #Check for Checkmate
    kr,kc=myking(one)
    if(king_moves(one,two)==False): #Count for places king can move and still get checked-----(MOVE)
        return(False)
    for i in checkwho:              #Check if blocking the check or taking out the checking piece is possible
        for j in ind(one,True):
            if(chr(8-i[0]+64)+str(i[1]+1) in blocks(a,a[(j[0])][j[1]],one,two,8-j[0],j[1]+1)):      #Check if the piece responsible for check can be taken out-----(KILL)
                temp=a[(i[0])][(i[1])]
                a[(i[0])][(i[1])]=a[(j[0])][(j[1])]
                a[(j[0])][(j[1])]="  "
                if(chcheck(one,two)):
                    a[(j[0])][(j[1])]=a[(i[0])][(i[1])]
                    a[(i[0])][(i[1])]=temp
                    pass
                else:
                    a[(j[0])][(j[1])]=a[(i[0])][(i[1])]
                    a[(i[0])][(i[1])]=temp
                    return(False)
            blockchk=blocks(a,a[(i[0])][i[1]],two,one,8-i[0],i[1]+1)
            try:
                blockchk.remove(chr(8-kr+64)+str(kc+1))
            except:
                pass
            for k in blockchk:                                                                      #Check if the check can be blocked-----(BLOCK)
                if(k in blocks(a,a[(j[0])][j[1]],one,two,8-j[0],j[1]+1)):
                    a[(8-ord(k[0])+64)][int(k[1])-1]=a[(j[0])][(j[1])]
                    a[(j[0])][(j[1])]="  "
                    if(chcheck(one,two)):
                        a[(j[0])][(j[1])]=a[(8-ord(k[0])+64)][int(k[1])-1]
                        a[(8-ord(k[0])+64)][int(k[1])-1]="  "
                        pass
                    else:
                        a[(j[0])][(j[1])]=a[(8-ord(k[0])+64)][int(k[1])-1]
                        a[(8-ord(k[0])+64)][int(k[1])-1]="  "
                        return(False)
    return(True)
def block_find(coord):          #Find the block in array as defined by any mouse click on the chess board
    if(coord==None):
        return None
    for i in chess_block['X']:
        if(coord[0]>chess_block['X'][i][0] and coord[0]<chess_block['X'][i][1] and coord[1]>chess_block['Y'][i][0] and coord[1]<chess_block['Y'][i][1]):
            return(i)
    return(None)
def board_print():              #Prints the board
    screen.fill(white)          #Fill the screen with white colour
    count = 0
    font =pygame.font.Font("Assets/unispace bd.ttf", 72)
    text = font.render('      Chess', True, (255,0,0), white)           #Chess text print
    textRect = text.get_rect()
    screen.blit(text,textRect)
    textRect.center = (500,10)
    pygame.draw.rect(screen, black,[80,80,640,640],5)                   #Main Chess border draw
    b=7
    font =pygame.font.Font("Assets/unispace bd.ttf",55)
    for i in range(8):                                                  
        text = font.render(chr(65+b), True, (255,0,0), white)           #Row alphabets print
        screen.blit(text,(10,80*(i+1)))
        text = font.render(str(i+1), True, (255,0,0), white)            #Column numbers print
        screen.blit(text,(((i+1)*80)+20,725))
        for j in range(8):                                              #Black and white block draw
            if count % 2 == 0:
                color=white
            else:
                color=black
            pygame.draw.rect(screen,color,[size*(j+1),size*(i+1),size,size])    
            count +=1
        count-=1
        b-=1
    for i in range(8):                                                  #Chess pieces' images arrangement draw
        for j in range(8):
            if(a[i][j]!="  "):
                screen.blit(pygame.image.load(stack[(a[i][j])]),position[(i,j)])
def castle_screen():
    pygame.draw.rect(screen,[211,211,211],[1220,295,230,100])
    pygame.draw.rect(screen,black,[1220,295,230,100],2)
    font =pygame.font.Font("Assets/unispace bd.ttf", 30)
    text = font.render('Castling', True, (0,0,0), white)
    screen.blit(text,(1260,255))
    screen.blit(pygame.image.load(stack['BQ']),(1230,295))
    screen.blit(pygame.image.load(stack['WQ']),(1260,293))
    screen.blit(pygame.image.load(stack['BK']),(1330,295))
    screen.blit(pygame.image.load(stack['WK']),(1360,293))
    font =pygame.font.Font("Assets/unispace bd.ttf", 20)
    text = font.render('Queenside', True, (0,0,0), [211,211,211])
    screen.blit(text,(1225,370))
    text = font.render('Kingside', True, (0,0,0), [211,211,211])
    screen.blit(text,(1350,370))
def castling(one,two,side):         #Castling
    global sixteen
    if(castle[one][2]==1):          #Check for King flag
        Tk().wm_withdraw() #to hide the main window
        msg="Castling cannot be done, The king has moved"
        messagebox.showerror('Error',msg)
        return(False)
    kr,kc=myking(one)
    if(chcheck(one,two)):           #Checking if the King is checked
        Tk().wm_withdraw() #to hide the main window
        msg="Castling cannot be done, The King is under check"
        messagebox.showerror('Error',msg)
        return(False)
    else:
        if(castle[one][side-1]==1): #Check for Rook Flag
            Tk().wm_withdraw() #to hide the main window
            msg="Castling cannot be done, The Rook has moved"
            messagebox.showerror('Error',msg)
            return(False)
        else:
            if(side==1):            #Queenside Castling
                if not(a[kr][kc-4]==one+'R'):
                    Tk().wm_withdraw() #to hide the main window
                    msg="Castling cannot be done, The Rook has been taken out"
                    messagebox.showerror('Error',msg)
                    return(False)
                if(a[kr][kc-1]==a[kr][kc-2]==a[kr][kc-3]=="  "):
                    a[kr][kc-1]=one+'K'
                    a[kr][kc]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc-1]="  "
                        Tk().wm_withdraw() #to hide the main window
                        msg="Castling cannot be done, The King moves through a checked block"
                        messagebox.showerror('Error',msg)
                        return(False)
                    a[kr][kc-2]=one+'K'
                    a[kr][kc-1]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc-2]="  "
                        Tk().wm_withdraw() #to hide the main window
                        msg="Castling cannot be done, The King will be checked after it"
                        messagebox.showerror('Error',msg)
                        return(False)
                    else:
                        if(len(ind(one,True))==1):
                            sixteen+=1
                        a[kr][kc-1]=one+'R'
                        a[kr][kc-4]="  "
                        castle[one][2]=1
                        castle_sound.play()
                        return(True)
                else:
                    Tk().wm_withdraw() #to hide the main window
                    msg="Castling is being blocked by pieces in between Rook and King"
                    messagebox.showerror('Error',msg)
                    return(False)
            else:                   #Kingside Castling
                if not(a[kr][kc+3]==one+'R'):
                    Tk().wm_withdraw() #to hide the main window
                    msg="Castling cannot be done, The Rook has been taken out"
                    messagebox.showerror('Error',msg)
                    return(False)
                if(a[kr][kc+1]==a[kr][kc+2]=="  "):
                    a[kr][kc+1]=one+'K'
                    a[kr][kc]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc+1]="  "
                        Tk().wm_withdraw() #to hide the main window
                        msg="Castling cannot be done, The King moves through a checked block"
                        messagebox.showerror('Error',msg)
                        return(False)
                    a[kr][kc+2]=one+'K'
                    a[kr][kc+1]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc+2]="  "
                        Tk().wm_withdraw() #to hide the main window
                        msg="Castling cannot be done, The King will be checked after it"
                        messagebox.showerror('Error',msg)
                        return(False)
                    else:
                        if(len(ind(one,True))==1):
                            sixteen+=1
                        a[kr][kc+1]=one+'R'
                        a[kr][kc+3]="  "
                        castle[one][2]=1
                        castle_sound.play()
                        return(True)
                else:
                    Tk().wm_withdraw() #to hide the main window
                    msg="Castling is being blocked by pieces in between Rook and King"
                    messagebox.showerror('Error',msg)
                    return(False)
def kill_stack():
    font =pygame.font.Font("Assets/unispace bd.ttf", 30)
    text = font.render('Black Taken Out(s)', True, (0,0,0), white)
    screen.blit(text,(1000,30))
    screen.blit(shelf,(780,135))
    screen.blit(shelf,(780,225))
    text = font.render('White Taken Out(s)', True, (0,0,0), white)
    screen.blit(text,(1000,400))
    screen.blit(shelf,(780,505))
    screen.blit(shelf,(780,595))
    x,y=790,80
    for i in kill_list['B']:
        screen.blit(pygame.image.load(stack[i]),(x,y))
        x+=80
        if(x>1509):
            y+=90
            x=790
    x,y=790,450
    for i in kill_list['W']:
        screen.blit(pygame.image.load(stack[i]),(x,y))
        x+=80
        if(x>1509):
            y+=90
            x=790
def forwards(one,two,coord):                                                #Displays blocks the selected chess piece could move
    global selected
    selected=None
    if(coord==None):
        return None
    if(a[coord[0]][coord[1]]=="  "):
        return None
    else:
        for i in blocks(a,a[coord[0]][coord[1]],one,two,8-coord[0],coord[1]+1):
            x=int(i[1])*80
            y=(9-ord(i[0])+64)*80
            pygame.draw.rect(screen,[127,255,0],[x,y,80,80],5)
    selected=chr(8-coord[0]+64)+str(coord[1]+1)
def chance_indicator(one):                                  #Chance Indicator(Indicates whether its Black's or White's chance)
    font =pygame.font.Font("Assets/unispace bd.ttf", 35)
    text = font.render('Chance Indicator', True, (255,0,0), white)
    screen.blit(text,(1150,640))
    pygame.draw.rect(screen,[211,211,211],[1250,700,195,80],0)
    pygame.draw.rect(screen,[255,255,255],[1265,705,70,70],0)    
    pygame.draw.rect(screen,[0,0,0],[1345,705,70,70],0)
    font =pygame.font.Font("Assets/unispace bd.ttf", 15)
    if(one=='W'):
        pygame.draw.rect(screen,[255,0,0],[1265,705,70,70],5)
        text = font.render('White', True, (0,0,0), white)
        screen.blit(text,(1280,730))
    else:
        pygame.draw.rect(screen,[255,0,0],[1345,705,70,70],5)
        text = font.render('Black', True, (255,255,255), (0,0,0))
        screen.blit(text,(1355,730))
def if_exit():
    Tk().wm_withdraw() #to hide the main window
    answer = messagebox.askokcancel("Exit", "Would you like to exit?")
    if(answer==True):
        pygame.quit()
        sys.exit(0)
def check_indicator(ch):                                    #Check Indicator(If my king is under check)
    font =pygame.font.Font("Assets/unispace bd.ttf", 35)
    text = font.render('Check Indicator', True, (255,0,0), white)
    screen.blit(text,(770,640))
    pygame.draw.circle(screen,[250,128,114],(880,750), 40)
    pygame.draw.circle(screen,[152,251,152],(980,750), 40)
    if(ch==True):
        text = font.render('Y', True, (255,0,0),[250,128,114])
        screen.blit(text,(867,730))
        pygame.draw.circle(screen,[255,0,0],(880,750),40,5)
    else:
        text = font.render('N', True, (0,255,0),[152,251,152] )
        screen.blit(text,(967,730))
        pygame.draw.circle(screen,[0,255,0],(980,750),40,5)
#############################################################################################################################################################################################
#                                                                                       MAIN PROGRAM                                                                                        #
#############################################################################################################################################################################################                                                               #Title of the game window change to 'Chess'
pygame.init()
black = (0,0,0)                                                                                     #Black colour assignment
clock = pygame.time.Clock()
white=(255,255,255)
screen = pygame.display.set_mode((1550,801))
pygame.display.set_caption("Chess")
icon = pygame.image.load("Assets/chess.png")
pygame.display.set_icon(icon)
background=pygame.transform.scale(pygame.image.load("Assets/back.jpeg"),(1550,801))
main_back=pygame.transform.scale(pygame.image.load("Assets/main_back.jpg").convert_alpha(), [370,400])
new_game=pygame.mixer.Sound("Assets/new.wav")
main_back.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
menu_click=pygame.mixer.Sound("Assets/menu_click.wav")
while(1):
    screen.blit(background,(0,0))
    screen.blit(main_back,(600,160))
    font =pygame.font.Font("Assets/unispace bd.ttf", 70)
    text = font.render('Chess', True, white)
    screen.blit(text,(680,80))
    pos=pygame.mouse.get_pos()
    if(pos[0]>670 and pos[0]<910 and pos[1]>205 and pos[1]<250):
        font =pygame.font.Font("Assets/unispace bd.ttf", 60)
        text = font.render('New Game', True, white)
        screen.blit(text,(650,195))
    else:
        font =pygame.font.Font("Assets/unispace bd.ttf", 50)
        text = font.render('New Game', True, black)
        screen.blit(text,(670,200))
    if(pos[0]>680 and pos[0]<895 and pos[1]>285 and pos[1]<328):
        font =pygame.font.Font("Assets/unispace bd.ttf", 60)
        text = font.render('Credits', True,white)
        screen.blit(text,(660,275))
    else:
        font =pygame.font.Font("Assets/unispace bd.ttf", 50)
        text = font.render('Credits', True,black)
        screen.blit(text,(680,280))
    if(pos[0]>700 and pos[0]<820 and pos[1]>365 and pos[1]<415):
        font =pygame.font.Font("Assets/unispace bd.ttf", 60)
        text = font.render('Quit', True, white)
        screen.blit(text,(690,350))
    else:
        font =pygame.font.Font("Assets/unispace bd.ttf", 50)
        text = font.render('Quit', True, black)
        screen.blit(text,(700,360))

    pos=(0,0)
    for event in pygame.event.get():                            #User Inputs
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONUP:                  #Catching position of mouse click on input
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:                           #Cross button pressed,response
            if_exit()
        if event.type == pygame.KEYDOWN:                        #If Escape key pressed,response 
            if event.key == pygame.K_ESCAPE:
                if_exit()
        if event.type == pygame.quit:                           #Response for Quit button click
            if_exit()
    if(pos[0]>670 and pos[0]<910 and pos[1]>205 and pos[1]<250):        #Board Assignment(Global declaration)
        menu_click.play()
        a=[["BR","BN","BB","BQ","BK","BB","BN","BR"], #Row H
           ["BP","BP","BP","BP","BP","BP","BP","BP"], #Row G
           ["  ","  ","  ","  ","  ","  ","  ","  "], #Row F
           ["  ","  ","  ","  ","  ","  ","  ","  "], #Row E
           ["  ","  ","  ","  ","  ","  ","  ","  "], #Row D
           ["  ","  ","  ","  ","  ","  ","  ","  "], #Row C
           ["WP","WP","WP","WP","WP","WP","WP","WP"], #Row B
           ["WR","WN","WB","WQ","WK","WB","WN","WR"]] #Row A
        #Col--1----2---3----4----5----6-----7----8--
        new_game.play()
        break
    elif(pos[0]>700 and pos[0]<820 and pos[1]>365 and pos[1]<415):
        menu_click.play()
        if_exit()
    elif(pos[0]>680 and pos[0]<895 and pos[1]>285 and pos[1]<328):
        menu_click.play()
        Tk().wm_withdraw() #to hide the main window
        msg="Thanks to the Pygame and Python community \n\n\t\t\t\t- Satyam"
        messagebox.showinfo('Credits',msg)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
size=80
black_bishop = "Assets/black_bishop.png"        
black_king = "Assets/black_king.png"
black_knight = "Assets/black_knight.png"
black_rook = "Assets/black_rook.png"
black_pawn = "Assets/black_pawn.png"                        #Image Assignment to variables
black_queen = "Assets/black_queen.png"
white_bishop = "Assets/white_bishop.png"
white_king = "Assets/white_king.png"
white_knight = "Assets/white_knight.png"
white_rook = "Assets/white_rook.png"
white_pawn = "Assets/white_pawn.png"
white_queen = "Assets/white_queen.png"
shelf =pygame.transform.scale(pygame.image.load("Assets/shelf.png"), [735,30])
chess_block=dict({'X':{},'Y':{}})
x=0
for i in range(8):
    y=0
    for j in range(8):
        chess_block['Y'][(x,y)]=((i+1)*80,((i+1)*80)+80)
        chess_block['X'][(x,y)]=((y+1)*80,((y+1)*80)+80)
        y+=1
    x+=1

stack={'BR':black_rook,                                         #Image Assignment                       
       'BN':black_knight,
       'BB':black_bishop,
       'BQ':black_queen,
       'BK':black_king,
       'BP':black_pawn,
       'WR':white_rook,
       'WN':white_knight,
       'WB':white_bishop,
       'WQ':white_queen,
       'WK':white_king,
       'WP':white_pawn}
position=dict({})                                               #Assignment of Chess pieces' positon on the board
for i in range(8):
    for j in range(8):
        position[(j,i)]=(80*(i+1),80*(j+1))
pos=None                                                        #Mouse click coordinates
count=0
move_sound=pygame.mixer.Sound("Assets/move.wav")
check_sound=pygame.mixer.Sound("Assets/check.wav")
taken_sound=pygame.mixer.Sound("Assets/taken.wav")
flop_sound=pygame.mixer.Sound("Assets/flop.wav")
castle_sound=pygame.mixer.Sound("Assets/castle.wav")
ch=["B","W"]
import random as r
p1=r.choice(ch)                       #Random assignment of Black or White on player 1
p2=[i for i in ch if i != p1]
p2=p2[0]                              #Assignment of Black or White on player 2
sixteen=0                             #Sixteen Chance Mate counter
while(1):
    selected=None
    ch=False
    if(count%2==0):                                             #Chance declaration
        one,two='W','B'
    else:
        one,two='B','W'
    if(chcheck(one,two)):                                       #Check for Check on the king
            check_sound.play()
            if(chcheckmate(one,two)):                           #Check for Checkmate
                Tk().wm_withdraw() #to hide the main window
                msg=plnum(ch-1)[:-1]+" ("+borw(two)+") wins!!"
                messagebox.showinfo('Checkmate',msg)
                pygame.quit()
                sys.exit(0)
            else:
                ch=True
    elif(stalemate(one,two)):
            Tk().wm_withdraw() #to hide the main window
            msg="The match has ended in a draw"
            messagebox.showinfo('Stalemate',msg)
            pygame.quit()
            sys.exit(0)
    for event in pygame.event.get():                            #User Inputs
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONUP:                  #Catching position of mouse click on input
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:                           #Cross button pressed,response
            if_exit()
        if event.type == pygame.KEYDOWN:                        #If Escape key pressed,response 
            if event.key == pygame.K_ESCAPE:
                if_exit()
        if event.type == pygame.quit:                           #Response for Quit button click
            if_exit()
    board_print()
    coord=block_find(pos)                                       #Determination of block by mouse click
    if coord!=None:                                             #Actual work of 'forward' function 
        if(a[coord[0]][coord[1]][0]==one):
            forwards(one,two,coord)

    chance_indicator(one)
    check_indicator(ch)
    kill_stack()
    castle_screen()
    piece=0
    same=False
    if(selected!=None):
        for event in pygame.event.get():
            if event.type == pygame.VIDEORESIZE:
                surface = pygame.display.set_mode((event.w, event.h),pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONUP:                  #Catching position of mouse click on input
                pos = pygame.mouse.get_pos()
                coord=block_find(pos)
                piece=(8-ord(selected[0])+64,int(selected[1])-1)
                if(piece==coord):
                    same=True
                    break
                if(coord!=None):
                    if(chr(8-coord[0]+64)+str(coord[1]+1) in blocks(a,a[piece[0]][piece[1]],one,two,8-piece[0],piece[1]+1)):
                        temp=a[coord[0]][coord[1]]
                        a[coord[0]][coord[1]]=a[piece[0]][piece[1]]
                        a[piece[0]][piece[1]]="  "
                        count+=1
                        if(sixteen==0 and len(ind(one,True))!=1 and len(ind(two,True))==1):
                                Tk().wm_withdraw() #to hide the main window
                                msg="The game will result in a draw if you cannot complete a checkmate in the next 16 moves"
                                messagebox.showinfo('Sixteen Chance Mate',msg)
                        if(len(ind(one,True))==1):
                            sixteen+=1
                        if(chcheck(one,two)):                           #Check for check on the king
                            a[piece[0]][piece[1]]=a[coord[0]][coord[1]]
                            a[coord[0]][coord[1]]=temp
                            count-=1
                            sixteen-=1
                            flop_sound.play()
                            continue
                        else:
                            if(a[coord[0]][coord[1]][1]=='P' and (coord[0]==0 or coord[0]==7)):     #Check if Pawn promotion is possible
                                Tk().wm_withdraw() #to hide the main window
                                promote=Promote(one,'Pawn Promotion','Pawn can be promoted to:\n')
                                promote.destroy()
                            if(temp != '  '):
                                kill_list[two].append(temp)
                                taken_sound.play()
                            else:
                                move_sound.play()
                        castle_check(coord,piece)
            elif event.type == pygame.QUIT:                           #Cross button pressed,response
                if_exit()
            elif event.type == pygame.KEYDOWN:                        #If Escape key pressed,response 
                if event.key == pygame.K_ESCAPE:
                    if_exit()
            elif event.type == pygame.quit:                           #Response for Quit button click
                if_exit()
            else:
                pass
    else:
        try:
            if((pos[0]>1240 and pos[0]<1325 and pos[1]>300 and pos[1]<360)or(pos[0]>1340 and pos[0]<1425 and pos[1]>300 and pos[1]<360)):
                if(pos[0]>1240 and pos[0]<1325):
                    side=1
                else:
                    side=2
                pos=None
                is_move=castling(one,two,side)
                if(is_move==True):
                    count+=1
                continue
        except:
                pass
    if(len(ind(one,True))==1):
        if(len(ind(two,True))==1):
            Tk().wm_withdraw() #to hide the main window
            msg="The game has resulted in a draw"
            messagebox.showinfo('Draw',msg)
            pygame.quit()
            sys.exit(0)
        font =pygame.font.Font("Assets/unispace bd.ttf", 35)
        text = font.render(str(sixteen), True, (0,0,0), white)
        screen.blit(text,(1120,720))
        if(sixteen==17):
            Tk().wm_withdraw() #to hide the main window
            msg="Draw,Due to incompletion of 16 chance mate"
            messagebox.showinfo('Draw',msg)
            pygame.quit()
            sys.exit(0)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
