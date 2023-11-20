class ColoredSquares:
    def __init__(self, color, isOnCorrectSide=True):
        self.isOnCorrectSide=isOnCorrectSide
        self.color=color

class Block:
    def __init__(self,coloredSquares:[],global_position:(),type):
        self.coloredSquares=coloredSquares
        self.gp=global_position
        self.current_position=[x for x in global_position]
        self.rotation = [0,0,0]
        self.type=type
        self.has_moved=False

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
    FACE_POSITION={F:0, L:1, R:2, U:3, D:4, B:5}
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
        
        if scramble != None:
            #scramble cube
        else:
            #scramble cube according to insctructions

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
                    CLOCKWISE_RIGHT:[Cube.F,Cube.R, Cube.U,Cube.D, Cube.B],
                    CLOCKWISE_BACK:[Cube.R,Cube.U, Cube.L,Cube.D, Cube.B],
                    CLOCKWISE_UP:[Cube.F,Cube.R, Cube.U,Cube.L, Cube.B],
                    CLOCKWISE_DOWN:[Cube.F,Cube.R, Cube.L,Cube.D, Cube.B],
                    CLOCKWISE_LEFT:[Cube.F,Cube.U, Cube.L,Cube.D, Cube.B],
                    COUNTER_CLOCKWISE_FRONT:[Cube.F,Cube.R, Cube.U,Cube.L, Cube.D],
                    COUNTER_CLOCKWISE_RIGHT:[Cube.F,Cube.R, Cube.U,Cube.D, Cube.B],
                    COUNTER_CLOCKWISE_BACK:[Cube.R,Cube.U, Cube.L,Cube.D, Cube.B],
                    COUNTER_CLOCKWISE_UP:[Cube.F,Cube.R, Cube.U,Cube.L, Cube.B],
                    COUNTER_CLOCKWISE_DOWN:[Cube.F,Cube.R, Cube.L,Cube.D, Cube.B],
                    COUNTER_CLOCKWISE_LEFT:[Cube.F,Cube.U, Cube.L,Cube.D, Cube.B]}
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

    ACTIONS_DICT={Turns.CLOCKWISE_FRONT:(0,0,90),
                  Turns.CLOCKWISE_RIGHT:(90,0,0),
                  Turns.CLOCKWISE_BACK:(0,0,-90),
                  Turns.CLOCKWISE_UP:(0,90,0),
                  Turns.CLOCKWISE_DOWN:(0,90,0),
                  Turns.CLOCKWISE_LEFT:(-90,0,0),
                  Turns.COUNTER_CLOCKWISE_FRONT:(0,0,-90),
                  Turns.COUNTER_CLOCKWISE_RIGHT:(-90,0,0),
                  Turns.COUNTER_CLOCKWISE_BACK:(0,0,90),
                  Turns.COUNTER_CLOCKWISE_UP:(0,-90,0),
                  Turns.COUNTER_CLOCKWISE_DOWN:(0,-90,0),
                  Turns.COUNTER_CLOCKWISE_LEFT:(90,0,0)
                }

    def getPossibleMoves(self,gamestate):
        poss_Moves=self.ACTIONS
        lastmove=gamestate.MoveList[-1]
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
    
    def getSuccessorStates(self,cube:Cube, actions)->[]:
        #compute actions on cube
        #return each new cube state
    def actOnCube(self, cube:Cube, action)->[]:
        #return new state
        box=cube
        if action==Turns.CLOCKWISE_FRONT:
            affected_faces=Turns.AFFECTED_FACES.get(Turns.CLOCKWISE_FRONT)
            for face in affected_faces:
               #update position and rotation
               ind=Cube.FACE_POSITION.get(face)
               for block in box.CURRENT_STATE:
                   if block.coloredSquares[ind]!=0 and block.has_moved==False:
                        block_pos_x=block.current_position[0]
                        block_pos_y=block.current_position[1]
                        block_pos_z=block.current_position[2]
                        if block.type=="corner":
                            if block_pos_x == block_pos_y:
                                block.current_position[1]=-block_pos_y
                                block.rotation[0]=block.rotation[0]+self.ACTIONS_DICT.get(action)[0]
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                            else:
                                block.current_position[0]=-block_pos_x
                                block.rotation[0]=block.rotation[0]+self.ACTIONS_DICT.get(action)[0]
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                        elif block.type=="edge":
                            if block_pos_x!=0:
                                block.current_position[0]=0
                                block.current_position[1]=-block_pos_x
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                            else:
                                block.current_position[1]=0
                                block.current_position[0]=block_pos_y
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                        for square in block.coloredSquares:
                            if square !=0:
                                if box.CURRENT_STATE==box.GOAL_STATE:
                                    square.isOnCorrectSide=True
                                else:
                                    square.isOnCorrectSide=False
                        block.has_moved=True
            for block in box.CURRENT_STATE:
                block.has_moved=False
        elif action==Turns.COUNTER_CLOCKWISE_FRONT:
            affected_faces=Turns.AFFECTED_FACES.get(Turns.CLOCKWISE_FRONT)
            for face in affected_faces:
               #update position and rotation
               ind=Cube.FACE_POSITION.get(face)
               for block in box.CURRENT_STATE:
                   if block.coloredSquares[ind]!=0 and block.has_moved==False:
                        block_pos_x=block.current_position[0]
                        block_pos_y=block.current_position[1]
                        block_pos_z=block.current_position[2]
                        if block.type=="corner":
                            if block_pos_x != block_pos_y:
                                block.current_position[1]=-block_pos_y
                                block.rotation[0]=block.rotation[0]+self.ACTIONS_DICT.get(action)[0]
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                            else:
                                block.current_position[0]=-block_pos_x
                                block.rotation[0]=block.rotation[0]+self.ACTIONS_DICT.get(action)[0]
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                        elif block.type=="edge":
                            if block_pos_x!=0:
                                block.current_position[0]=0
                                block.current_position[1]=block_pos_x
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                            else:
                                block.current_position[1]=0
                                block.current_position[0]=-block_pos_y
                                block.rotation[1]=block.rotation[1]+self.ACTIONS_DICT.get(action)[1]
                                block.rotation[2]=block.rotation[2]+self.ACTIONS_DICT.get(action)[2]
                        for square in block.coloredSquares:
                            if square !=0:
                                if box.CURRENT_STATE==box.GOAL_STATE:
                                    square.isOnCorrectSide=True
                                else:
                                    square.isOnCorrectSide=False
                        block.has_moved=True
            for block in box.CURRENT_STATE:
                block.has_moved=False
            






                    
class Cubing:
    #manages gamestate