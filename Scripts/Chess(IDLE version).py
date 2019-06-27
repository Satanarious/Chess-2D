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

#Board Assignment(Global declaration)
a=[["BR","BN","BB","BQ","BK","BB","BN","BR"], #Row H
   ["BP","BP","BP","BP","BP","BP","BP","BP"], #Row G
   ["  ","  ","  ","  ","  ","  ","  ","  "], #Row F
   ["  ","  ","  ","  ","  ","  ","  ","  "], #Row E
   ["  ","  ","  ","  ","  ","  ","  ","  "], #Row D
   ["  ","  ","  ","  ","  ","  ","  ","  "], #Row C
   ["WP","WP","WP","WP","WP","WP","WP","WP"], #Row B
   ["WR","WN","WB","WQ","WK","WB","WN","WR"]] #Row A
#Col--1----2---3----4----5----6-----7----8--
checkwho=[]                          #Indice of pieces that check the King(Global declaration)
castle={'W':[0,0,0],'B':[0,0,0]}     #Flags for castling(Global declaration)
kill_list={'W':[],'B':[]}             #Killed pieces(Global declaration)
def borw(a):                         #Letting user known of the colour selected randomly
    if(a=='B'):
        return("Black")
    else:
        return("White")
def chance(ch) :                     #Comprehending black or white turn
    if(ch%2 is not 0):
        return('W')
    else:
        return('B')
def plnum(ch):                       #Player number
    if(chance(ch)==p1):
        return("Player 1:")
    else:
        return("Player 2:")
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
        kr,kc=myking(one)
        for i in range(len(bl)):
            if(a[(8-ord(bl[i][0])+64)][(int(bl[i][1])-1)][0]==p1):
                bl[i]=0
        bl=list(filter(lambda a: a != 0, bl))
        return(bl)
def promotion(piece,r,c):
    if(r==72 or r==65):
        print("You are Eligible for a 'Pawn Promotion' Choose 'Promoted piece':")
        print("1)Queen\n2)Knight\n3)Bishop\n4)Rook")
        while(1):
            try:
                a[8-r+64][c-1]={1:piece[0]+"Q",2:piece[0]+"N",3:piece[0]+"B",4:piece[0]+"R"}[int(input("Enter:"))]
                if(a[8-r+64][c-1][1]=='Q'):
                    print("\t\t\t\t!!!!Queening Performed!!!!\n")
                else:
                    print("\t\t\t!!!!!!!!!Underpromotion Performed!!!!!!!!\n")
                break
            except:
                continue
def ind(two,pawn):                       #Indices of opponent pieces except pawns
    b=[]
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j][0]==two and a[i][j][1]!='P' and pawn==False):
                b.append((i,j))
            elif(a[i][j][0]==two and pawn==True):
                b.append((i,j))
    return(b)
def myking(one):                    #Position of the king
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j]==one+'K'):
                return(i,j)
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
    return(True)
def castle_check(dc):               #Setting flags for castling
    if(a[(8-dc[2]+64)][dc[3]-1]=='WR' and dc[0]==65 and dc[1]==1):
        castle['W'][0]=1
    elif(a[(8-dc[2]+64)][dc[3]-1]=='WR' and dc[0]==65 and dc[1]==8):
        castle['W'][1]=1
    elif(a[(8-dc[2]+64)][dc[3]-1]=='BR' and dc[0]==72 and dc[1]==1):
        castle['B'][0]=1
    elif(a[(8-dc[2]+64)][dc[3]-1]=='BR' and dc[0]==75 and dc[1]==8):
        castle['B'][1]=1
    elif(a[(8-dc[2]+64)][dc[3]-1]=='WK' and dc[0]==65 and dc[1]==5):
        castle['W'][2]=1
    elif(a[(8-dc[2]+64)][dc[3]-1]=='BK' and dc[0]==72 and dc[1]==5):
        castle['B'][2]=1
def castling(one,two,side):         #Castling
    if not(side>0 and side<3):      #Check for input
        print("\n\t\t\t\t!!!!Unknown Input!!!!\n")
        return(False)
    if(castle[one][2]==1):          #Check for King flag
        print("\n!!!!Castling cannot be done, The king has moved!!!!\n")
        return(False)
    kr,kc=myking(one)
    if(chcheck(one,two)):           #Checking if the King is checked
        print("\n!!!!Castling cannot be done, The King is under check!!!!\n")
        return(False)
    else:
        if(castle[one][side-1]==1): #Check for Rook Flag
            print("\n!!!!Castling cannot be done, The Rook has moved!!!!\n")
            return(False)
        else:
            if(side==1):            #Queenside Castling
                if not(a[kr][kc-4]==one+'R'):
                    print("\n!!!!Castling cannot be done, The Rook has been taken out!!!!\n")
                    return(False)
                if(a[kr][kc-1]==a[kr][kc-2]==a[kr][kc-3]=="  "):
                    a[kr][kc-1]=one+'K'
                    a[kr][kc]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc-1]="  "
                        print("\n!!!!Castling cannot be done, The King moves through a checked block!!!!\n")
                        return(False)
                    a[kr][kc-2]=one+'K'
                    a[kr][kc-1]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc-2]="  "
                        print("\n!!!!Castling cannot be done, The King will be checked after it!!!!\n")
                        return(False)
                    else:
                        if(len(ind(one,True))==1):
                            sixteen+=1
                        a[kr][kc-1]=one+'R'
                        a[kr][kc-4]="  "
                        castle[one][2]=1
                        return(True)
                else:
                    print("\n!!!!Castling is being blocked by pieces in between Rook and King!!!!\n")
                    return(False)
            else:                   #Kingside Castling
                if not(a[kr][kc+3]==one+'R'):
                    print("\n!!!!Castling cannot be done, The Rook has been taken out!!!!\n")
                    return(False)
                if(a[kr][kc+1]==a[kr][kc+2]=="  "):
                    a[kr][kc+1]=one+'K'
                    a[kr][kc]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc+1]="  "
                        print("\n!!!!Castling cannot be done, The King moves through a checked block!!!!\n")
                        return(False)
                    a[kr][kc+2]=one+'K'
                    a[kr][kc+1]="  "
                    if(chcheck(one,two)):
                        a[kr][kc]=one+'K'
                        a[kr][kc+2]="  "
                        print("\n!!!!Castling cannot be done, The King will be checked after it!!!!\n")
                        return(False)
                    else:
                        if(len(ind(one,True))==1):
                            sixteen+=1
                        a[kr][kc+1]=one+'R'
                        a[kr][kc+3]="  "
                        castle[one][2]=1
                        return(True)
                else:
                    print("\n!!!!Castling is being blocked by pieces in between Rook and King!!!!\n")
                    return(False)
def decode(mov):                     #Decoding player move syntax
    try:
        if(mov.lower()=="castle"):
            return("castle")
        elif(mov.lower()=="board"):
            return("board")
        elif(mov.lower()=="moves"):
            return("moves")
    except:
        return("!!Invalid Syntax or Out of bounds move!!")
    try:
        r1,c1,r2,c2=ord(mov[0].upper()),int(mov[1]),ord(mov[6].upper()),int(mov[7])
        if(r1>=65 and r1<=72 and r2>=65 and r2<=72 and c1>=1 and c1<=8 and c2>=1 and c2<=8 and mov[2]==" " and mov[5]==" " and mov[3].lower()=='t' and mov[4].lower()=='o'):
            return([r1,c1,r2,c2])
        else:
            return("!!Invalid Syntax or Out of bounds move!!")
    except:
        return("!!Invalid Syntax or Out of bounds move!!")
def moves(mov):                      #Assessment of error
    if(decode(mov)[0]=='!'):
       print(decode(mov))
       return(0)
    else:
        return(decode(mov))
ws =u'\u2000\u2000'
ws1=u'\u2000'
def boardprint(a):                   #Board Printing
    b=7
    st={'  ':ws,'WK':'\u2654','WQ':'\u2655','WR':'\u2656','WB':'\u2657','WN':'\u2658','WP':'\u2659','BK':'\u265A','BQ':'\u265B','BR':'\u265C','BB':'\u265D','BN':'\u265E','BP':'\u265F'}
    print("\t\t\t\t    ****Chess Board****\n")
    for i in a:
        print("\t\t\t(",chr(65+b),")  ",end="",sep="")
        b-=1
        for j in i:
            print("[",st[j],"]",end="",sep="")
        if(b==4):
            print("\tBlack(Taken out(s)):",end="")
        elif(b==3):
            print("\t",end="")
            for j in kill_list['B']:            #Black taken out Pieces
                print(st[j],end="")
        elif(b==1):
            print("\tWhite(Taken out(s)):",end="")
        elif(b==0):
            print("\t",end="")
            for j in kill_list['W']:            #White taken out Pieces
                print(st[j],end="")
        print()
    print("\n\t\t\t     ",end="",sep="")
    for i in range(8):
        print("(",i+1,")",ws1,end="",sep="")
    print()
#############################################################################################################################################################################################
#                                                                                       MAIN PROGRAM                                                                                        #
#############################################################################################################################################################################################
print()
print("                          ██████╗██╗  ██╗███████╗███████╗███████╗")
print("                         ██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝")
print("                         ██║     ███████║█████╗  ███████╗███████╗")
print("                         ██║     ██╔══██║██╔══╝  ╚════██║╚════██║")
print("                         ╚██████╗██║  ██║███████╗███████║███████║")
print("                          ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝")
print()
boardprint(a)
print("\n\n\t\t\t     ",end="",sep="")
print("^^^^Welcome to Chess-2D^^^^")
ch=["B","W"]
import random as r
p1=r.choice(ch)                       #Random assignment of Black or White on player 1
p2=[i for i in ch if i  is not p1]
p2=p2[0]                              #Assignment of Black or White on player 2
print("Player 1 is ",borw(p1))
print("Player 2 is ",borw(p2),)
print("Note: Colour selection is based on a random selection technique")
print("Syntax: row(initial)column(initial) to row(final)column(final)")
print("Ex:B2 to D2,Rows lie from A to H  and columns lie from 1 to 8")
print("Type:\n1)Board (To print the Chessboard)\n2)Castle (To perform Castling)\n3)Moves (To know possible moves of a piece)")
ch=1                                  #First/starting chance assignment
print("\n")
one,two='W','B'
sixteen=0                             #Sixteen Chance Mate counter
while(1):                             #Looping chances
    dc=0                              #Deciphered Move
    while(dc==0):
        if(chcheck(one,two)):
            if(chcheckmate(one,two)):
                    print("\n\t\t\t\t!!!!Checkmate!!!!")
                    print("\t\t\t",plnum(ch-1)[:-1],"((",borw(two),"))"," wins")
                    import sys
                    sys.exit(0)
            else:
                print("\n\t\t\t\t!!!!Check!!!!")
        elif(stalemate(one,two)):
            print("\n\t\t\t\t!!!!Stalemate!!!!")
            print("\t\t\tThe match has ended in a draw ")
            import sys
            sys.exit(0)
        turn="Turn-->>("+borw(one)+")"+str(plnum(ch))       #Letting the player know of his/her chance
        move=input(turn)
        dc=moves(move)
        if(dc=="castle"):                                   #Keyword for Castling options
            print("You have opted for Castling:")
            print("1)Queenside Castling\n2)Kingside Castling")
            try:
                if(castling(one,two,int(input("Enter your choice:")))==False):
                    dc=0
            except:
                print("!!!!Invalid Input!!!!")
                dc=0
        elif(dc=="moves"):                                  #Keyword to check possible moves of a piece
            pos=input("Enter the piece's current position:")
            try:
                if(len(pos)>2 or a[8-ord(pos[0].upper())+64][int(pos[1])-1][0]==two):
                    print("!!!!Invalid Block!!!!")
                    dc=0
                    continue
            except:
                print("!!!!Invalid Block!!!!")
                dc=0
                continue
            try:
                print("Possible moves are: ",blocks(a,a[8-ord(pos[0].upper())+64][int(pos[1])-1],one,two,ord(pos[0].upper())-64,int(pos[1])))
                dc=0
            except:
                print("!!!!Invalid Block!!!!")
                dc=0
        elif(dc=="board"):                                  #Keyword to print board
            boardprint(a)
            dc=0
        elif(dc==0):
            continue
        elif(a[(8-dc[0]+64)][dc[1]-1][0]==two):             #If player tries to move opponent's piece
            print("!!Invalid Move!!\n!!That's the opponents piece mi amigo!!")
            dc=0
        elif(a[(8-dc[0]+64)][dc[1]-1]=="  "):
            print("!!Invalid Move!!\n!!Empty as your brain!!")
            dc=0
        elif(chr(dc[2])+str(dc[3]) in blocks(a,a[(8-dc[0]+64)][dc[1]-1],one,two,dc[0]-64,dc[1]) and a[(8-dc[2]+64)][(dc[3]-1)]!=two+'K'):
            temp=a[(8-dc[2]+64)][dc[3]-1]
            a[(8-dc[2]+64)][dc[3]-1]=a[(8-dc[0]+64)][dc[1]-1]
            a[(8-dc[0]+64)][dc[1]-1]="  "
            sixteen+=1
            if(chcheck(one,two)):                           #Check for check on the king
                print("!!Invalid Move!!You are under CHECK!!")
                a[(8-dc[0]+64)][dc[1]-1]=a[(8-dc[2]+64)][dc[3]-1]
                a[(8-dc[2]+64)][dc[3]-1]=temp
                dc=0
                sixteen-=1
                continue
            elif(a[(8-dc[2]+64)][dc[3]-1][1]=='P'):
                promotion(a[(8-dc[2]+64)][dc[3]-1],dc[2],dc[3])     #Pawn Promotion
            if(temp is not "  "):
                kill_list[two].append(temp)
            castle_check(dc)                                        #Check for Rook or king moves(Reference for Castling)
        else:
            print("!!Invalid move!!")
            dc=0
        if(len(ind(one,True))==1):
            if(len(ind(two,True))==1):
                print("The game has resulted in a draw.")
                sys.exit(0)
            if(sixteen==17):
                print("The game has resulted in a draw.Due to incompletion of sixteen chance mate")
                sys.exit(0)
    ch+=1
    one,two=two,one
    boardprint(a)
