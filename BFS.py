#BFS
import Cubing as c
actor=c.Actions()
def bfs(cube:c.Cube,goalstate):
   
    closed=set()
    fringe=[]
    actions=[]
    fringe.append((meaningfulState(cube.START_STATE),cube.MOVE_LIST+[],0))
    #print(meaningfulState(cube.START_STATE))
    while(True):
        
        if  len(fringe)==0:
            print("Failure")
            return False
        node,actions,cost=fringe.pop(0)
        #print(actions)
        if CheckGS(actions,goalstate)==True:
            return actions
        
        if str(node) not in closed:
            closed.add(str(node))
            
            for state in getSuccessors(node,actions):
                fringe.append((state[0],actions+[state[1]],state[2]))
                #print(fringe)
    return actions
  

def getSuccessors(node:tuple,al):
    temp_Cube=c.Cube(al)
    validMoves=actor.getPossibleMoves(temp_Cube)
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

def CheckGS(actionlist,gs):
    temp_Cube=c.Cube(actionlist)
    if meaningfulState(temp_Cube.CURRENT_STATE)==meaningfulState(gs):
        return True
    else:
        return False




# test=c.Cube(3)

# #print(a)
# print("Before BFS\n")
# print(test.MOVE_LIST)
# print(test.getDEBUGCube())
# print("During BFS")
# a=bfs(test,test.GOAL_STATE)
# print(str(a))
# test=c.Cube(a)
# print("\nPost BFS\n")
# print(test.getDEBUGCube())