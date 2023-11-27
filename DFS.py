#DFS
import Cubing as c
actor=c.Actions()
def dfs(cube:c.Cube,goalstate):
   
    closed=set()
    fringe=[]
    actions=[]
    fringe.insert(0,(meaningfulState(cube.START_STATE),cube.MOVE_LIST+[],0))
    print(meaningfulState(cube.START_STATE))
    while(True):
        
        if  len(fringe)==0:
            print("Failure")
            return False
        node,actions,cost=fringe.pop()
        print(node)
        if CheckGS(actions,cube,goalstate)==True:
            return actions
        
        if str(node) not in closed:
            closed.add(str(node))
            
            for state in getSuccessors(node):
                fringe.insert(0,(state[0],actions+[state[1]],state[2]))
                #print(fringe)
    return actions
  

def getSuccessors(node:tuple):
    validMoves=actor.ACTIONS
    temp_Cube=c.Cube()
    for i in range(len(temp_Cube.CURRENT_STATE)):
        temp_Cube.CURRENT_STATE[i].current_position=node[i][0]
        temp_Cube.CURRENT_STATE[i].rotation=node[i][1]
    sucessors=[]
    for move in validMoves:
        next_state=actor.actOnCube(temp_Cube,move)
        cost=1
        sucessors.append((meaningfulState(next_state),move,cost))
    return sucessors

def meaningfulState(state):
    pos_rot=[]
    for block in state:
        pos_rot.append((block.current_position,block.rotation))
    return pos_rot

def CheckGS(actionlist,cube,gs):
    ttemp_Cube=c.Cube(actionlist)
    a=meaningfulState(ttemp_Cube.CURRENT_STATE)
    b=gs
    for i in range(len(a)):
        if a[i][0]==b[i][0] and a[i][1]==b[i][1]:
            return True
        else:
            return False
    

def genTermState():
    CORNER_BLOCKS=[(-1,1,1),(1,1,1),(-1,-1,1),(1,-1,1),(-1,1,-1),(1,1,-1),(-1,-1,-1),(1,-1,-1)]
    EDGE_BLOCKS=[(0,1,1),(-1,0,1),(1,0,1),(0,-1,1),(0,1,-1),(-1,0,-1),(1,0,-1),(0,-1,-1),(-1,1,0),(-1,-1,0),(1,1,0),(1,-1,0) ]
    CENTER_BLOCKS=[(0,0,1),(-1,0,0),(1,0,0),(0,1,0),(0,-1,0),(0,0,-1)]
    
    state=CORNER_BLOCKS+EDGE_BLOCKS+CENTER_BLOCKS
    pos_rot=[]
    for block in state:
        pos_rot.append((block,(0,0,0,0,0,0)))
    return pos_rot
a=genTermState()
print(a)
test=c.Cube(["F'"])

print(a)
print("Before DFS\n")
print(test.MOVE_LIST)
print(test.getDEBUGCube())
print("During DFS")
print("Solution:"+str(dfs(test,a)))
print("\nPost DFS\n")
print(test.getDEBUGCube())