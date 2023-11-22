import random
import fileinput
class ColoredSquares:
    def __init__(self, color, isOnCorrectSide=True):
        self.isOnCorrectSide=isOnCorrectSide
        self.isInCorrectPosition=True
        self.color=color
        self.hasMoved=False
    def __str__(self):
        text="Color: {0}. CorrectSide/Position: {1}/{2}. "
        return text.format(self.color[0],self.isOnCorrectSide,self.isInCorrectPosition)

class Block:
    def __init__(self,coloredSquares:[],global_position:(),type):
        self.coloredSquares=coloredSquares
        self.gp=global_position
        self.current_position=[x for x in global_position]
        self.rotation = [0,0,0,0,0,0]
        self.type=type
        self.has_moved=False
    
    def getColoredSquares(self):
        text=""
        for square in self.coloredSquares:
            text=text+str(square)+","
        return text
    def __str__(self):
        text="Type: {0}. Current Global Position: {1}. Colored Squares {2}. Rotation: {3}."
        t1=text.format(self.type,self.current_position,self.getColoredSquares(),self.rotation)
        return t1

class Cube:
    F="Front"
    R="Right"
    L="Left"
    U="Up"
    D="Down"
    B="Back"
    COLORS={F:"GREEN",
            L:"ORANGE",
            R:"RED",
            U:"WHITE",
            D:"YELLOW",
            B:"BLUE"}
    #need to finish
    FACE_POSITION={"F":0, "L":1, "R":2, "U":3, "D":4, "B":5}
    CORNER_BLOCKS=[Block([ColoredSquares(COLORS.get(F)),ColoredSquares(COLORS.get(L)),0,ColoredSquares(COLORS.get(U)),0,0],(-1,1,1),"corner"),Block([ColoredSquares(COLORS.get(F)),0,ColoredSquares(COLORS.get(R)),ColoredSquares(COLORS.get(U)),0,0],(1,1,1),"corner"),
                    Block([ColoredSquares(COLORS.get(F)),ColoredSquares(COLORS.get(L)),0,0,ColoredSquares(COLORS.get(D)),0],(-1,-1,1),"corner"),Block([ColoredSquares(COLORS.get(F)),0,ColoredSquares(COLORS.get(R)),0,ColoredSquares(COLORS.get(D)),0],(1,-1,1),"corner"),
                    
                    Block([0,ColoredSquares(COLORS.get(L)),0,ColoredSquares(COLORS.get(U)),0,ColoredSquares(COLORS.get(B))],(-1,1,-1),"corner"),Block([0,0,ColoredSquares(COLORS.get(R)),ColoredSquares(COLORS.get(U)),0,ColoredSquares(COLORS.get(B))],(1,1,-1),"corner"),
                    Block([0,ColoredSquares(COLORS.get(L)),0,0,ColoredSquares(COLORS.get(D)),ColoredSquares(COLORS.get(B))],(-1,-1,-1),"corner"),Block([0,0,ColoredSquares(COLORS.get(R)),0,ColoredSquares(COLORS.get(D)),ColoredSquares(COLORS.get(B))],(1,-1,-1),"corner")
                    ]
    EDGE_BLOCKS=[Block([ColoredSquares(COLORS.get(F)),0,0,ColoredSquares(COLORS.get(U)),0,0],(0,1,1),"edge"),Block([ColoredSquares(COLORS.get(F)),ColoredSquares(COLORS.get(L)),0,0,0,0],(-1,0,1),"edge"),
                 Block([ColoredSquares(COLORS.get(F)),0,ColoredSquares(COLORS.get(R)),0,0,0],(1,0,1),"edge"),Block([ColoredSquares(COLORS.get(F)),0,0,0,ColoredSquares(COLORS.get(D)),0],(0,-1,1),"edge"),
                 
                 Block([0,0,0,ColoredSquares(COLORS.get(U)),0,ColoredSquares(COLORS.get(B))],(0,1,-1),"edge"),Block([0,ColoredSquares(COLORS.get(L)),0,0,0,ColoredSquares(COLORS.get(B))],(-1,0,-1),"edge"),
                 Block([0,0,ColoredSquares(COLORS.get(R)),0,0,ColoredSquares(COLORS.get(B))],(1,0,-1),"edge"),Block([0,0,0,0,ColoredSquares(COLORS.get(D)),ColoredSquares(COLORS.get(B))],(0,-1,-1),"edge"),
                 
                 Block([0,ColoredSquares(COLORS.get(L)),0,ColoredSquares(COLORS.get(U)),0,0],(-1,1,0),"edge"),Block([0,ColoredSquares(COLORS.get(L)),0,0,ColoredSquares(COLORS.get(D)),0],(-1,-1,0),"edge"),
                 Block([0,0,ColoredSquares(COLORS.get(R)),ColoredSquares(COLORS.get(U)),0,0],(1,1,0),"edge"),Block([0,0,ColoredSquares(COLORS.get(R)),0,ColoredSquares(COLORS.get(D)),0],(1,-1,0),"edge")
                 ]
    CENTER_BLOCKS=[Block([ColoredSquares(COLORS.get(F)),0,0,0,0,0],(0,0,1),"center"),Block([0,ColoredSquares(COLORS.get(L)),0,0,0,0],(-1,0,0),"center"),Block([0,0,ColoredSquares(COLORS.get(R)),0,0,0],(1,0,0),"center"),
                   Block([0,0,0,ColoredSquares(COLORS.get(U)),0,0],(0,1,0),"center"),Block([0,0,0,0,ColoredSquares(COLORS.get(D)),0],(0,-1,0),"center"),Block([0,0,0,0,0,ColoredSquares(COLORS.get(B))],(0,0,-1),"center")]
    
    
    def __init__(self,scramble=None):

        self.START_STATE=self.CORNER_BLOCKS+self.EDGE_BLOCKS+self.CENTER_BLOCKS
        self.GOAL_STATE=self.START_STATE
        self.CURRENT_STATE=self.START_STATE
        self.MOVE_LIST=[]
        
        if scramble != None:
            action=Actions()
            if isinstance(scramble,int)==True:
                #if given int randomly sramble
                for i in range(scramble):
                    act=Actions.ACTIONS[random.randint(0,len(Actions.ACTIONS)-1)]
                    ns=action.actOnCube(self,act)
                    self.CURRENT_STATE=ns
                    self.MOVE_LIST.append(act)
            elif isinstance(scramble,list)==True:
                for act in scramble:
                    ns=action.actOnCube(self,act)
                    self.CURRENT_STATE=ns
                    self.MOVE_LIST.append(act)
            elif isinstance(scramble,str):
               for line in fileinput.input(files=scramble):
                   for act in line:
                       ns=action.actOnCube(self,act)
                       self.CURRENT_STATE=ns
                       self.MOVE_LIST.append(act)

    def isInTerminalState(self)->bool:
        for block in self.CURRENT_STATE:
            for square in block.coloredSquares:
                if square!=0:
                    if square.isInCorrectPosition!=True:
                        return False
        return True
    
    def getDEBUGState(self):
        text=""
        for block in self.CURRENT_STATE:
            text=text+str(block)+"\n"
        return text
    
    def getDEBUGCube(self):
        line1="         B[-1, -1, -1] B[0, -1, -1] B[1, -1, -1]         \n"
        line2="         B[-1, 0, -1] B[0, 0, -1] B[1, 0, -1]         \n"
        line3="         B[-1, 1, -1] B[0, 1, -1] B[1, 1, -1]         \n\n\n"
        line4="L[-1, -1, -1] L[-1, 0, -1] L[-1, 1, -1]    U[-1, 1, -1] U[0, 1, -1] U[1, 1, -1]    R[1, 1, -1] R[1, 0, -1] R[1, -1, -1]\n"
        line5="L[-1, -1, 0] L[-1, 0, 0] L[-1, 1, 0]    U[-1, 1, 0] U[0, 1, 0] U[1, 1, 0]    R[1, 1, 0] R[1, 0, 0] R[1, -1, 0]\n"
        line6="L[-1, -1, 1] L[-1, 0, 1] L[-1, 1, 1]    U[-1, 1, 1] U[0, 1, 1] U[1, 1, 1]    R[1, 1, 1] R[1, 0, 1] R[1, -1, 1]\n\n\n"
        line7="         F[-1, 1, 1] F[0, 1, 1] F[1, 1, 1]      \n"
        line8="         F[-1, 0, 1] F[0, 0, 1] F[1, 0, 1]      \n"
        line9="         F[-1, -1, 1] F[0, -1, 1] F[1, -1, 1]      \n\n\n"
        line10="         D[-1, -1, -1] D[0, -1, -1] D[1, -1, -1]      \n"
        line11="         D[-1, -1, 0] D[0, -1, 0] D[1, -1, 0]      \n"
        line12="         D[-1, -1, 1] D[0, -1, 1] D[1, -1, 1]      \n\n\n"

        template=line1+line2+line3+line4+line5+line6+line7+line8+line9+line10+line11+line12
        for block in self.CURRENT_STATE:
            for i in range(len(block.coloredSquares)):
                if block.coloredSquares[i]!=0:
                    #find where the square goes and pplace the first letter of color there
                    #side+block coor
                    for key,val in self.FACE_POSITION.items():
                        if val==i:
                            side=key
                    rt=side+str(block.current_position)
                    #print(rt)
                    template=template.replace(rt,block.coloredSquares[i].color[0])
        return template


class Turns:
    CLOCKWISE_FRONT="F"
    CLOCKWISE_RIGHT='R'
    CLOCKWISE_BACK="B"
    CLOCKWISE_UP="U"
    CLOCKWISE_DOWN="D"
    CLOCKWISE_LEFT="L"
    COUNTER_CLOCKWISE_FRONT="F'"
    COUNTER_CLOCKWISE_RIGHT="R'"
    COUNTER_CLOCKWISE_BACK="B'"
    COUNTER_CLOCKWISE_UP="U'"
    COUNTER_CLOCKWISE_DOWN="D'"
    COUNTER_CLOCKWISE_LEFT="L'"
    AFFECTED_FACES={CLOCKWISE_FRONT:[Cube.F,Cube.R, Cube.U,Cube.L, Cube.D],
                    CLOCKWISE_RIGHT:[Cube.F,Cube.B,Cube.R, Cube.U,Cube.D],
                    CLOCKWISE_BACK:[Cube.B,Cube.R,Cube.U, Cube.L,Cube.D],
                    CLOCKWISE_UP:[Cube.F,Cube.B,Cube.R, Cube.U,Cube.L],
                    CLOCKWISE_DOWN:[Cube.F,Cube.B,Cube.R, Cube.L,Cube.D],
                    CLOCKWISE_LEFT:[Cube.F,Cube.B,Cube.U, Cube.L,Cube.D],
                    COUNTER_CLOCKWISE_FRONT:[Cube.F,Cube.R, Cube.U,Cube.L, Cube.D],
                    COUNTER_CLOCKWISE_RIGHT:[Cube.F,Cube.B,Cube.R, Cube.U,Cube.D],
                    COUNTER_CLOCKWISE_BACK:[Cube.B,Cube.R,Cube.U, Cube.L,Cube.D],
                    COUNTER_CLOCKWISE_UP:[Cube.F,Cube.B,Cube.R, Cube.U,Cube.L],
                    COUNTER_CLOCKWISE_DOWN:[Cube.F,Cube.B,Cube.R, Cube.L,Cube.D],
                    COUNTER_CLOCKWISE_LEFT:[Cube.F,Cube.B,Cube.U, Cube.L,Cube.D]}
class Actions:
    "controls actions"
    ACTIONS=[Turns.CLOCKWISE_FRONT,
    Turns.CLOCKWISE_RIGHT,
    Turns.CLOCKWISE_BACK,
    Turns.CLOCKWISE_UP,
    Turns.CLOCKWISE_DOWN,
    Turns.CLOCKWISE_LEFT,
    Turns.COUNTER_CLOCKWISE_FRONT,
    Turns.COUNTER_CLOCKWISE_RIGHT,
    Turns.COUNTER_CLOCKWISE_BACK,
    Turns.COUNTER_CLOCKWISE_UP,
    Turns.COUNTER_CLOCKWISE_DOWN,
    Turns.COUNTER_CLOCKWISE_LEFT]

    ACTIONS_DICT={Turns.CLOCKWISE_FRONT:(0,0,0,0,90,0),
                  Turns.CLOCKWISE_RIGHT:(90,0,0,0,0,0),
                  Turns.CLOCKWISE_BACK:(0,0,0,0,0,90),
                  Turns.CLOCKWISE_UP:(0,0,90,0,0,0),
                  Turns.CLOCKWISE_DOWN:(0,0,0,90,0,0),
                  Turns.CLOCKWISE_LEFT:(0,90,0,0,0,0),
                  Turns.COUNTER_CLOCKWISE_FRONT:(0,0,0,0,-90,0),
                  Turns.COUNTER_CLOCKWISE_RIGHT:(-90,0,0,0,0,0),
                  Turns.COUNTER_CLOCKWISE_BACK:(0,0,0,0,0,-90),
                  Turns.COUNTER_CLOCKWISE_UP:(0,0,-90,0,0,0),
                  Turns.COUNTER_CLOCKWISE_DOWN:(0,0,0,-90,0,0),
                  Turns.COUNTER_CLOCKWISE_LEFT:(0,-90,0,0,0,0)
                }

    def getPossibleMoves(self,cube:Cube):
        poss_Moves=self.ACTIONS
        lastmove=cube.MOVE_LIST[-1]
        if lastmove==Turns.CLOCKWISE_FRONT:
            poss_Moves.remove(Turns.COUNTER_CLOCKWISE_FRONT)
        elif lastmove==Turns.CLOCKWISE_RIGHT:
            poss_Moves.remove(Turns.COUNTER_CLOCKWISE_RIGHT)
        elif lastmove==Turns.CLOCKWISE_BACK:
            poss_Moves.remove(Turns.COUNTER_CLOCKWISE_BACK)
        elif lastmove==Turns.CLOCKWISE_UP:
            poss_Moves.remove(Turns.COUNTER_CLOCKWISE_UP)
        elif lastmove==Turns.CLOCKWISE_DOWN:
            poss_Moves.remove(Turns.COUNTER_CLOCKWISE_DOWN)
        elif lastmove==Turns.CLOCKWISE_LEFT:
            poss_Moves.remove(Turns.COUNTER_CLOCKWISE_LEFT)
        elif lastmove==Turns.COUNTER_CLOCKWISE_FRONT:
            poss_Moves.remove(Turns.CLOCKWISE_FRONT)
        elif lastmove==Turns.COUNTER_CLOCKWISE_RIGHT:
            poss_Moves.remove(Turns.CLOCKWISE_RIGHT)
        elif lastmove==Turns.COUNTER_CLOCKWISE_BACK:
            poss_Moves.remove(Turns.CLOCKWISE_BACK)
        elif lastmove==Turns.COUNTER_CLOCKWISE_UP:
            poss_Moves.remove(Turns.CLOCKWISE_UP)
        elif lastmove==Turns.COUNTER_CLOCKWISE_DOWN:
            poss_Moves.remove(Turns.CLOCKWISE_DOWN)
        elif lastmove==Turns.COUNTER_CLOCKWISE_LEFT:
            poss_Moves.remove(Turns.CLOCKWISE_LEFT)
        return poss_Moves
    
    def updateRoatation(self, block:Block, action):
        rotation=block.rotation
     
        rotation[0]+=Actions.ACTIONS_DICT.get(action)[0]
        rotation[1]+=Actions.ACTIONS_DICT.get(action)[1]
        rotation[2]+=Actions.ACTIONS_DICT.get(action)[2]
        rotation[3]+=Actions.ACTIONS_DICT.get(action)[3]
        rotation[4]+=Actions.ACTIONS_DICT.get(action)[4]
        rotation[5]+=Actions.ACTIONS_DICT.get(action)[5]
        
        for i in range(len(rotation)):
            if rotation[i]==360 or rotation[i]==-360:
                rotation[i]=0
        #move colored squares
        #FACE_POSITION={F:0, L:1, R:2, U:3, D:4, B:5}
        #Rotation_ind={"R","L","U","D","F","B"}
        squares=block.coloredSquares
        lx_axis_rot=["D",0,0,"F","B","U"]
        rx_axis_rot=["U",0,0,"B","F","D"]
        y_axis_rot=["L","B","F",0,0,"R"]
        z_axis_rot=[0,"U","D","R","L",0]
        neg_lx_axis_rot=["U",0,0,"B","F","D"]
        neg_rx_axis_rot=["D",0,0,"F","B","U"]
        neg_y_axis_rot=["R","F","B",0,0,"L"]
        neg_z_axis_rot=[0,"D","U","L","R",0]
        changed_ind=[]
        isNeg=False
        for i in range(len(Actions.ACTIONS_DICT.get(action))):
            if Actions.ACTIONS_DICT.get(action)[i]!=0:
                changed_ind.append(i)
        
        if Actions.ACTIONS_DICT.get(action)[changed_ind[0]]<0:
            isNeg=True
        temp_block=[0,0,0,0,0,0]
        if isNeg==False:
            if changed_ind[0] <2:
                #if right face moved
                if changed_ind[0]==0:
                    for i in range(len(squares)):
                        if squares[i]!=0 and rx_axis_rot[i]!=0 and squares[i].hasMoved==False:
                            #hold any values current in the needed location
                            if squares[Cube.FACE_POSITION.get(rx_axis_rot[i])]!=0:
                                temp_block[Cube.FACE_POSITION.get(rx_axis_rot[i])]=squares[Cube.FACE_POSITION.get(rx_axis_rot[i])]
                                squares[Cube.FACE_POSITION.get(rx_axis_rot[i])].hasMoved=True
                            squares[Cube.FACE_POSITION.get(rx_axis_rot[i])]=squares[i]
                            squares[i].hasMoved=True
                            squares[i]=0
                            
                    #move held values
                    for i in range(len(temp_block)):
                        if temp_block[i]!=0:
                            squares[Cube.FACE_POSITION.get(rx_axis_rot[i])]=temp_block[i]
                elif changed_ind[0]==1:
                    #if left face moved
                    for i in range(len(squares)):
                        if squares[i]!=0 and lx_axis_rot[i]!=0 and squares[i].hasMoved==False:
                            #hold any values current in the needed location
                            if squares[Cube.FACE_POSITION.get(lx_axis_rot[i])]!=0:
                                temp_block[Cube.FACE_POSITION.get(lx_axis_rot[i])]=squares[Cube.FACE_POSITION.get(lx_axis_rot[i])]
                                squares[Cube.FACE_POSITION.get(lx_axis_rot[i])].hasMoved=True
                            squares[Cube.FACE_POSITION.get(lx_axis_rot[i])]=squares[i]
                            squares[i].hasMoved=True
                            squares[i]=0
                            
                    #move held values
                    for i in range(len(temp_block)):
                        if temp_block[i]!=0:
                            squares[Cube.FACE_POSITION.get(lx_axis_rot[i])]=temp_block[i]
            #y axis rotation
            elif changed_ind[0]>1 and changed_ind[0]<4:
                for i in range(len(squares)):
                    if squares[i]!=0 and y_axis_rot[i]!=0 and squares[i].hasMoved==False:
                        #hold any values current in the needed location
                        if squares[Cube.FACE_POSITION.get(y_axis_rot[i])]!=0:
                            temp_block[Cube.FACE_POSITION.get(y_axis_rot[i])]=squares[Cube.FACE_POSITION.get(y_axis_rot[i])]
                            squares[Cube.FACE_POSITION.get(y_axis_rot[i])].hasMoved=True
                        squares[Cube.FACE_POSITION.get(y_axis_rot[i])]=squares[i]
                        squares[i].hasMoved=True
                        squares[i]=0
                        
                #move held values
                for i in range(len(temp_block)):
                    if temp_block[i]!=0:
                        squares[Cube.FACE_POSITION.get(y_axis_rot[i])]=temp_block[i]
            #z rotation
            else:
                for i in range(len(squares)):
                    if squares[i]!=0 and z_axis_rot[i]!=0 and squares[i].hasMoved==False:
                        #hold any values current in the needed location
                        
                        if squares[Cube.FACE_POSITION.get(z_axis_rot[i])]!=0:
                            temp_block[Cube.FACE_POSITION.get(z_axis_rot[i])]=squares[Cube.FACE_POSITION.get(z_axis_rot[i])]
                            squares[Cube.FACE_POSITION.get(z_axis_rot[i])].hasMoved=True
                        squares[Cube.FACE_POSITION.get(z_axis_rot[i])]=squares[i]
                        squares[i].hasMoved=True
                        squares[i]=0
                        
                    #move held values
                for i in range(len(temp_block)):
                    if temp_block[i]!=0:
                        squares[Cube.FACE_POSITION.get(z_axis_rot[i])]=temp_block[i]
        else:
            if changed_ind[0] <2:
                #if right face moved
                if changed_ind[0]==0:
                    for i in range(len(squares)):
                        if squares[i]!=0 and neg_rx_axis_rot[i]!=0 and squares[i].hasMoved==False:
                            #hold any values current in the needed location
                            if squares[Cube.FACE_POSITION.get(neg_rx_axis_rot[i])]!=0:
                                temp_block[Cube.FACE_POSITION.get(neg_rx_axis_rot[i])]=squares[Cube.FACE_POSITION.get(neg_rx_axis_rot[i])]
                                squares[Cube.FACE_POSITION.get(neg_rx_axis_rot[i])].hasMoved=True
                            squares[Cube.FACE_POSITION.get(neg_rx_axis_rot[i])]=squares[i]
                            squares[i].hasMoved=True
                            squares[i]=0
                            
                    #move held values
                    for i in range(len(temp_block)):
                        if temp_block[i]!=0:
                            squares[Cube.FACE_POSITION.get(neg_rx_axis_rot[i])]=temp_block[i]
                elif changed_ind[0]==1:
                    #if left face moved
                    for i in range(len(squares)):
                        if squares[i]!=0 and neg_lx_axis_rot[i]!=0 and squares[i].hasMoved==False:
                            #hold any values current in the needed location
                            if squares[Cube.FACE_POSITION.get(neg_lx_axis_rot[i])]!=0:
                                temp_block[Cube.FACE_POSITION.get(neg_lx_axis_rot[i])]=squares[Cube.FACE_POSITION.get(neg_lx_axis_rot[i])]
                                squares[Cube.FACE_POSITION.get(neg_lx_axis_rot[i])].hasMoved=True
                            squares[Cube.FACE_POSITION.get(neg_lx_axis_rot[i])]=squares[i]
                            squares[i].hasMoved=True
                            squares[i]=0
                            
                    #move held values
                    for i in range(len(temp_block)):
                        if temp_block[i]!=0:
                            squares[Cube.FACE_POSITION.get(neg_lx_axis_rot[i])]=temp_block[i]
            #y axis rotation
            elif changed_ind[0]>1 and changed_ind[0]<4:
                for i in range(len(squares)):
                    if squares[i]!=0 and neg_y_axis_rot[i]!=0 and squares[i].hasMoved==False:
                        #hold any values current in the needed location
                        if squares[Cube.FACE_POSITION.get(neg_y_axis_rot[i])]!=0:
                            temp_block[Cube.FACE_POSITION.get(neg_y_axis_rot[i])]=squares[Cube.FACE_POSITION.get(neg_y_axis_rot[i])]
                            squares[Cube.FACE_POSITION.get(neg_y_axis_rot[i])].hasMoved=True
                        squares[Cube.FACE_POSITION.get(neg_y_axis_rot[i])]=squares[i]
                        squares[i].hasMoved=True
                        squares[i]=0
                        
                #move held values
                for i in range(len(temp_block)):
                    if temp_block[i]!=0:
                        squares[Cube.FACE_POSITION.get(neg_y_axis_rot[i])]=temp_block[i]
            #z rotation
            else:
                for i in range(len(squares)):
                    if squares[i]!=0 and z_axis_rot[i]!=0 and squares[i].hasMoved==False:
                        #hold any values current in the needed location
                        
                        if squares[Cube.FACE_POSITION.get(neg_z_axis_rot[i])]!=0:
                            temp_block[Cube.FACE_POSITION.get(neg_z_axis_rot[i])]=squares[Cube.FACE_POSITION.get(neg_z_axis_rot[i])]
                            squares[Cube.FACE_POSITION.get(neg_z_axis_rot[i])].hasMoved=True
                        squares[Cube.FACE_POSITION.get(neg_z_axis_rot[i])]=squares[i]
                        squares[i].hasMoved=True
                        squares[i]=0
                        
                    #move held values
                for i in range(len(temp_block)):
                    if temp_block[i]!=0:
                        squares[Cube.FACE_POSITION.get(neg_z_axis_rot[i])]=temp_block[i]
        #zero out colored squares
        for square in block.coloredSquares:
            if square!=0:
                #check if squares are in the right position
                if block.current_position==list(block.gp) and block.rotation==[0,0,0,0,0,0]:
                    square.isInCorrectPosition=True
                    square.isOnCorrectSide=True
                else:
                    square.isInCorrectPosition=False
                    if square.hasMoved==True:
                        square.isOnCorrectSide=False
                square.hasMoved=False
        return rotation,squares


        #return each new cube state
    def actOnCube(self, cube:Cube, action)->[]:
        #return new state
        box=cube
        if action==Turns.CLOCKWISE_FRONT:
            for block in box.CURRENT_STATE:
                #every block on the front face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_z==1:
                    if block.type=="corner":
                        if block_pos_x==block_pos_y:
                            block.current_position[1]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[0]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block.type=="edge":
                        if block_pos_x==0:
                            block.current_position[0]=block_pos_y
                            block.current_position[1]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[1]=-block_pos_x
                            block.current_position[0]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.COUNTER_CLOCKWISE_FRONT:
            for block in box.CURRENT_STATE:
                #every block on the front face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_z==1:
                    if block.type=="corner":
                        if block_pos_x!=block_pos_y:
                            block.current_position[1]=block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[0]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block.type=="edge":
                        if block_pos_x==0:
                            block.current_position[0]=-block_pos_y
                            block.current_position[1]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[1]=block_pos_x
                            block.current_position[0]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.CLOCKWISE_BACK:
            for block in box.CURRENT_STATE:
                #every block on the back face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_z==-1:
                    if block.type=="corner":
                        if block_pos_x==block_pos_y:
                            block.current_position[1]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[0]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block.type=="edge":
                        if block_pos_x==0:
                            block.current_position[0]=block_pos_y
                            block.current_position[1]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[1]=-block_pos_x
                            block.current_position[0]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.COUNTER_CLOCKWISE_BACK:
            for block in box.CURRENT_STATE:
                #every block on the back face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_z==-1:
                    if block.type=="corner":
                        if block_pos_x!=block_pos_y:
                            block.current_position[1]=block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[0]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block.type=="edge":
                        if block_pos_x==0:
                            block.current_position[0]=-block_pos_y
                            block.current_position[1]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        else:
                            block.current_position[1]=block_pos_x
                            block.current_position[0]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.CLOCKWISE_RIGHT:
            for block in box.CURRENT_STATE:
                #every block on the right face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_x==1:
                    #front/right blocks
                    if block_pos_z==1:
                        if block.type == "corner":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=-block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/right pieces
                    elif block_pos_z==-1:
                        if block.type == "corner":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=-block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #right side
                    elif block_pos_z==0:
                        if block.type=="edge":
                           block.current_position[0]=1
                           block.current_position[1]=0
                           block.current_position[2]=-block_pos_y
                           block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.COUNTER_CLOCKWISE_RIGHT:
            for block in box.CURRENT_STATE:
                #every block on the right face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_x==1:
                    #front/right blocks
                    if block_pos_z==1:
                        if block.type == "corner":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/right pieces
                    elif block_pos_z==-1:
                        if block.type == "corner":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #right side
                    elif block_pos_z==0:
                        if block.type=="edge":
                           block.current_position[0]=1
                           block.current_position[1]=0
                           block.current_position[2]=block_pos_y
                           block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.CLOCKWISE_LEFT:
            for block in box.CURRENT_STATE:
                #every block on the left face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_x==-1:
                    #front/left blocks
                    if block_pos_z==1:
                        if block.type == "corner":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/left pieces
                    elif block_pos_z==-1:
                        if block.type == "corner":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #left side
                    elif block_pos_z==0:
                        if block.type=="edge":
                           block.current_position[0]=-1
                           block.current_position[1]=0
                           block.current_position[2]=block_pos_y
                           block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.COUNTER_CLOCKWISE_LEFT:
            for block in box.CURRENT_STATE:
                #every block on the left face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_x==-1:
                    #front/left blocks
                    if block_pos_z==1:
                        if block.type == "corner":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=-block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/left pieces
                    elif block_pos_z==-1:
                        if block.type == "corner":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=-block_pos_y
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #left side
                    elif block_pos_z==0:
                        if block.type=="edge":
                           block.current_position[0]=-1
                           block.current_position[1]=0
                           block.current_position[2]=-block_pos_y
                           block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action == Turns.CLOCKWISE_UP:
            for block in box.CURRENT_STATE:
                #every block on the up face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_y==1:
                    #front/up
                    if block_pos_z==1:
                        if block.type=="corner":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/up
                    elif block_pos_z==-1:
                        if block.type=="corner":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block_pos_z==0:
                        #right/up
                        if block_pos_x==1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=1
                                block.current_position[2]=1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        #left/up
                        elif block_pos_x==-1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=1
                                block.current_position[2]=-1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.COUNTER_CLOCKWISE_UP:
             for block in box.CURRENT_STATE:
                #every block on the up face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_y==1:
                    #front/up
                    if block_pos_z==1:
                        if block.type=="corner":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/up
                    elif block_pos_z==-1:
                        if block.type=="corner":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block_pos_z==0:
                        #right/up
                        if block_pos_x==1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=1
                                block.current_position[2]=-1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        #left/up
                        elif block_pos_x==-1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=1
                                block.current_position[2]=1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action == Turns.CLOCKWISE_DOWN:
            for block in box.CURRENT_STATE:
                #every block on the down face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_y==-1:
                    #front/down
                    if block_pos_z==1:
                        if block.type=="corner":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/down
                    elif block_pos_z==-1:
                        if block.type=="corner":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block_pos_z==0:
                        #right/down
                        if block_pos_x==1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=-1
                                block.current_position[2]=1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        #left/down
                        elif block_pos_x==-1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=-1
                                block.current_position[2]=-1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        elif action==Turns.COUNTER_CLOCKWISE_DOWN:
             for block in box.CURRENT_STATE:
                #every block on the down face
                block_pos_x=block.current_position[0]
                block_pos_y=block.current_position[1]
                block_pos_z=block.current_position[2]
                if block_pos_y==-1:
                    #front/down
                    if block_pos_z==1:
                        if block.type=="corner":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    #back/down
                    elif block_pos_z==-1:
                        if block.type=="corner":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=-block_pos_x
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        elif block.type=="edge":
                            block.current_position[0]=-1
                            block.current_position[1]=-1
                            block.current_position[2]=0
                            block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                    elif block_pos_z==0:
                        #right/down
                        if block_pos_x==1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=-1
                                block.current_position[2]=-1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
                        #left/down
                        elif block_pos_x==-1:
                            if block.type=="edge":
                                block.current_position[0]=0
                                block.current_position[1]=-1
                                block.current_position[2]=1
                                block.rotation,block.coloredSquares=self.updateRoatation(block, action)
        return box.CURRENT_STATE
                    
    def getSuccessorStates(self,cube:Cube, actions:[])->[]:
            #compute actions on cube
            states=[]
            for action in actions:
                states.append(self.actOnCube(cube,action))
            return states

#testing stuff
#rc=Cube(["D"])
#action=Actions()
#ns=action.actOnCube(rc,"U'")
#rc.CURRENT_STATE=ns
#print(rc.getDEBUGCube())
#ns=action.actOnCube(rc,"F")
#rc.CURRENT_STATE=ns
#ns=action.actOnCube(rc,"F")
#rc.CURRENT_STATE=ns
#ns=action.actOnCube(rc,"F")
#rc.CURRENT_STATE=ns
#print(rc.getDEBUGState())
#print("\n"+rc.getDEBUGCube())
#print(rc.MOVE_LIST)
#print("\n"+str(rc.isInTerminalState()))   
#print(rc.getDEBUGCube())
#ns=action.actOnCube(rc,"U'")
#rc.CURRENT_STATE=ns
#print(rc.getDEBUGState())
#print("\n"+rc.getDEBUGCube())
#print("\n"+str(rc.isInTerminalState()))            
#class Cubing:
  #  #manages gamestate