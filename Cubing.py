class ColoredSquares:
    def __init__(self, position:(), color, isOnCorrectSide=True):
        self.position=position
        self.isOnCorrectSide=isOnCorrectSide
        self.color=color

class Block:
    def __init__(self,coloredSquares:[],sides:[]):
        self.coloredSquares=coloredSquares
        self.sides=sides
        if  len(coloredSquares)==1:
            self.type="center"
        elif len(coloredSquares)==2:
            self.type="edge"
        elif len(coloredSquares)==3:
            self.type="corner"

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
    SOLVED_FACES={F:[Block([ColoredSquares((L,0,2),COLORS.get(L)),ColoredSquares((U,2,0),COLORS.get(U)),ColoredSquares((F,0,0),COLORS.get(F))],sides=[L,U,F]),
              Block([ColoredSquares((U,2,1),COLORS.get(U)),ColoredSquares((F,0,1),COLORS.get(F))],sides=[U,F]),
              Block([ColoredSquares((F,0,2),COLORS.get(F)),ColoredSquares((U,2,2),COLORS.get(U)),ColoredSquares((R,0,0),COLORS.get(R))],sides=[L,U,R]),
              Block([ColoredSquares((L,1,2),COLORS.get(L)),ColoredSquares((F,1,0),COLORS.get(F))],sides=[L,F]),
              Block([ColoredSquares((F,1,1),COLORS.get(F))],sides=[F]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((R,1,0),COLORS.get(R))],sides=[F,R]),
              Block([ColoredSquares((L,2,2),COLORS.get(L)),ColoredSquares((D,0,0),COLORS.get(D)),ColoredSquares((F,2,0),COLORS.get(F))],sides=[L,D,F]),
              Block([ColoredSquares((F,2,1),COLORS.get(F)),ColoredSquares((D,0,1),COLORS.get(D))],sides=[F,D]),
              Block([ColoredSquares((F,2,2),COLORS.get(F)),ColoredSquares((D,0,2),COLORS.get(D)),ColoredSquares((R,2,0),COLORS.get(R))],sides=[F,D,R])],
           R:[Block([ColoredSquares((F,0,2),COLORS.get(F)),ColoredSquares((U,2,2),COLORS.get(U)),ColoredSquares((R,0,0),COLORS.get(R))],sides=[F,U,R]),
              Block([ColoredSquares((U,1,2),COLORS.get(U)),ColoredSquares((R,0,1),COLORS.get(R))],sides=[U,R]),
              Block([ColoredSquares((R,0,2),COLORS.get(R)),ColoredSquares((U,0,2),COLORS.get(U)),ColoredSquares((B,0,0),COLORS.get(B))],sides=[R,U,B]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((F,1,0),COLORS.get(F))],sides=[L,F]),
              Block([ColoredSquares((F,1,1),COLORS.get(F))],sides=[F]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((R,1,0),COLORS.get(R))],sides=[F,R]),
              Block([ColoredSquares((L,2,2),COLORS.get(L)),ColoredSquares((D,0,0),COLORS.get(D)),ColoredSquares((F,2,0),COLORS.get(F))],sides=[L,D,F]),
              Block([ColoredSquares((F,2,1),COLORS.get(F)),ColoredSquares((D,0,1),COLORS.get(D))],sides=[F,D]),
              Block([ColoredSquares((F,2,2),COLORS.get(F)),ColoredSquares((D,0,2),COLORS.get(D)),ColoredSquares((R,2,0),COLORS.get(R))],sides=[F,D,R])],
           L:[Block([ColoredSquares((L,0,2),COLORS.get(L)),ColoredSquares((U,2,0),COLORS.get(U)),ColoredSquares((F,0,0),COLORS.get(F))],sides=[L,U,F]),
              Block([ColoredSquares((U,2,1),COLORS.get(U)),ColoredSquares((F,0,1),COLORS.get(F))],sides=[U,F]),
              Block([ColoredSquares((F,0,2),COLORS.get(F)),ColoredSquares((U,2,2),COLORS.get(U)),ColoredSquares((R,0,0),COLORS.get(R))],sides=[L,U,R]),
              Block([ColoredSquares((L,1,2),COLORS.get(L)),ColoredSquares((F,1,0),COLORS.get(F))],sides=[L,F]),
              Block([ColoredSquares((F,1,1),COLORS.get(F))],sides=[F]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((R,1,0),COLORS.get(R))],sides=[F,R]),
              Block([ColoredSquares((L,2,2),COLORS.get(L)),ColoredSquares((D,0,0),COLORS.get(D)),ColoredSquares((F,2,0),COLORS.get(F))],sides=[L,D,F]),
              Block([ColoredSquares((F,2,1),COLORS.get(F)),ColoredSquares((D,0,1),COLORS.get(D))],sides=[F,D]),
              Block([ColoredSquares((F,2,2),COLORS.get(F)),ColoredSquares((D,0,2),COLORS.get(D)),ColoredSquares((R,2,0),COLORS.get(R))],sides=[F,D,R])],
           U:[Block([ColoredSquares((L,0,2),COLORS.get(L)),ColoredSquares((U,2,0),COLORS.get(U)),ColoredSquares((F,0,0),COLORS.get(F))],sides=[L,U,F]),
              Block([ColoredSquares((U,2,1),COLORS.get(U)),ColoredSquares((F,0,1),COLORS.get(F))],sides=[U,F]),
              Block([ColoredSquares((F,0,2),COLORS.get(F)),ColoredSquares((U,2,2),COLORS.get(U)),ColoredSquares((R,0,0),COLORS.get(R))],sides=[L,U,R]),
              Block([ColoredSquares((L,1,2),COLORS.get(L)),ColoredSquares((F,1,0),COLORS.get(F))],sides=[L,F]),
              Block([ColoredSquares((F,1,1),COLORS.get(F))],sides=[F]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((R,1,0),COLORS.get(R))],sides=[F,R]),
              Block([ColoredSquares((L,2,2),COLORS.get(L)),ColoredSquares((D,0,0),COLORS.get(D)),ColoredSquares((F,2,0),COLORS.get(F))],sides=[L,D,F]),
              Block([ColoredSquares((F,2,1),COLORS.get(F)),ColoredSquares((D,0,1),COLORS.get(D))],sides=[F,D]),
              Block([ColoredSquares((F,2,2),COLORS.get(F)),ColoredSquares((D,0,2),COLORS.get(D)),ColoredSquares((R,2,0),COLORS.get(R))],sides=[F,D,R])],
           D:[Block([ColoredSquares((L,0,2),COLORS.get(L)),ColoredSquares((U,2,0),COLORS.get(U)),ColoredSquares((F,0,0),COLORS.get(F))],sides=[L,U,F]),
              Block([ColoredSquares((U,2,1),COLORS.get(U)),ColoredSquares((F,0,1),COLORS.get(F))],sides=[U,F]),
              Block([ColoredSquares((F,0,2),COLORS.get(F)),ColoredSquares((U,2,2),COLORS.get(U)),ColoredSquares((R,0,0),COLORS.get(R))],sides=[L,U,R]),
              Block([ColoredSquares((L,1,2),COLORS.get(L)),ColoredSquares((F,1,0),COLORS.get(F))],sides=[L,F]),
              Block([ColoredSquares((F,1,1),COLORS.get(F))],sides=[F]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((R,1,0),COLORS.get(R))],sides=[F,R]),
              Block([ColoredSquares((L,2,2),COLORS.get(L)),ColoredSquares((D,0,0),COLORS.get(D)),ColoredSquares((F,2,0),COLORS.get(F))],sides=[L,D,F]),
              Block([ColoredSquares((F,2,1),COLORS.get(F)),ColoredSquares((D,0,1),COLORS.get(D))],sides=[F,D]),
              Block([ColoredSquares((F,2,2),COLORS.get(F)),ColoredSquares((D,0,2),COLORS.get(D)),ColoredSquares((R,2,0),COLORS.get(R))],sides=[F,D,R])],
           B:[Block([ColoredSquares((L,0,2),COLORS.get(L)),ColoredSquares((U,2,0),COLORS.get(U)),ColoredSquares((F,0,0),COLORS.get(F))],sides=[L,U,F]),
              Block([ColoredSquares((U,2,1),COLORS.get(U)),ColoredSquares((F,0,1),COLORS.get(F))],sides=[U,F]),
              Block([ColoredSquares((F,0,2),COLORS.get(F)),ColoredSquares((U,2,2),COLORS.get(U)),ColoredSquares((R,0,0),COLORS.get(R))],sides=[L,U,R]),
              Block([ColoredSquares((L,1,2),COLORS.get(L)),ColoredSquares((F,1,0),COLORS.get(F))],sides=[L,F]),
              Block([ColoredSquares((F,1,1),COLORS.get(F))],sides=[F]),
              Block([ColoredSquares((F,1,2),COLORS.get(F)),ColoredSquares((R,1,0),COLORS.get(R))],sides=[F,R]),
              Block([ColoredSquares((L,2,2),COLORS.get(L)),ColoredSquares((D,0,0),COLORS.get(D)),ColoredSquares((F,2,0),COLORS.get(F))],sides=[L,D,F]),
              Block([ColoredSquares((F,2,1),COLORS.get(F)),ColoredSquares((D,0,1),COLORS.get(D))],sides=[F,D]),
              Block([ColoredSquares((F,2,2),COLORS.get(F)),ColoredSquares((D,0,2),COLORS.get(D)),ColoredSquares((R,2,0),COLORS.get(R))],sides=[F,D,R])]}
    

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
    
    def getSuccessorStates(self,gamestate):
        #compute actions on cube
        #return each new cube state
class Cubing:
    #manages gamestate