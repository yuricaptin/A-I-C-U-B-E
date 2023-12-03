import Cubing as c
import math
import random
actor=c.Actions()
def REFLEX_SOL(cube:c.Cube,goalstate):
    actions=cube.MOVE_LIST
    gamestate=cube.CURRENT_STATE
    while CheckGS(actions,goalstate)==False:
        scrSucc=getScoredSuccessors(gamestate,actions)
        scores=[scrSucc[i][2]  for i in range(len(scrSucc)) ]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        actions.append(scrSucc[chosenIndex][1])
        print(actions)
        print(scrSucc[chosenIndex][2])
    return actions






def scoreState(gamestate):
    # #how many blocks in correct posistion
    # #how many blocks have correct rotation
    # #how many blocks are close
    # rp=meaningfulState(gamestate)
    # cor_posBlk=0
    # cor_rotBlk=0
    # closeBlk=0
    # for i in range(len(rp)):
    #     rot=rp[i][1]
    #     dist=rp[i][0]
    #     if gamestate[i].gp==dist and rot==[0,0,0,0,0,0]:
    #         cor_posBlk+=1
    #         cor_rotBlk+=1
    #     elif closePos(dist,gamestate[i].gp)==True and closeRot==True:
    #         closeBlk+=1
    # print(cor_posBlk)
    # print(cor_rotBlk)
    # print(closeBlk)

    # return cor_posBlk+cor_rotBlk+(3*closeBlk)
    cor_pos=0
    cor_rot=0
    both=0
    for block in gamestate:
        for square in block.coloredSquares:
            #print(square)
            if square !=0:
                if square.isOnCorrectSide==True and square.isInCorrectPosition==True:
                    cor_pos+=1
                    cor_rot+=1
                    both+=1
                elif square.isOnCorrectSide==True and square.isInCorrectPosition==False:
                    cor_rot+=1
                elif square.isOnCorrectSide==False and square.isInCorrectPosition==True:
                    cor_pos+=1

    return cor_pos+cor_rot+(3*both)

    
    

def closeRot(rot):
    flag=False
    degCt=0
    for r in rot:
        if abs(r)==90 and degCt<2:
            degCt=degCt+1
            flag=True
        elif  r==0 and degCt<2:
             flag=True
        else:
             flag=False
             break
    return flag

def closePos(pos,gp):
    ct=0
    flag=False
    for i in range(len(pos)):
        if abs(pos[i]-gp[i])==1 and ct<2:
            ct+=1
            flag=True
        else:
            flag=False
    return flag
def getScoredSuccessors(node:tuple,al):
    temp_Cube=c.Cube(al)
    validMoves=actor.ACTIONS
    sucessors=[]
    for move in validMoves:
        next_state=actor.actOnCube(temp_Cube,move)
        cost=1
        sucessors.append((next_state,move,scoreState(next_state)-cost))
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
# print("Before Reflex Sol\n")
# print(test.MOVE_LIST)
# print(test.getDEBUGCube())
# print("During Reflex Sol")
# a=REFLEX_SOL(test,test.GOAL_STATE)
# print(str(a))
# test=c.Cube(a)
# print("\nPost Reflex Sol\n")
# print(test.getDEBUGCube())