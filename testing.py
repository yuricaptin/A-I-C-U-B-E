import BFS
import DFS
import ReflexRubiks as Reflex
import time
import Cubing
from func_timeout import func_timeout, FunctionTimedOut

def LATester(scramble_length,num_times):
   
    for i in range(num_times):
        print("Round: {0}\n".format(i+1))
        #gen cube
        cube=Cubing.Cube(scramble_length)
        #BFS
        try:
            print("BFS")
            start=time.perf_counter()
            a=func_timeout(600,BFS, args=(cube, cube.GOAL_STATE))
            end=time.perf_counter()
            print("num moves: {0}\nTotal time: {1}\n\n".format(len(a),end-start))
        except FunctionTimedOut:
            print("BFS Exceeded 10 Minutes\n")
        try:
            print("Reflex")
            start=time.perf_counter()
            a=func_timeout(600,Reflex, args=(cube, cube.GOAL_STATE))
            end=time.perf_counter()
            print("num moves: {0}\nTotal time: {1}\n\n".format(len(a),end-start))
        except FunctionTimedOut:
            print("Reflex Exceeded 10 Minutes\n")
        try:
            print("DFS")
            start=time.perf_counter()
            a=func_timeout(600,DFS, args=(cube, cube.GOAL_STATE))
            end=time.perf_counter()
            print("num moves: {0}\nTotal time: {1}\n\n".format(len(a),end-start))
        except FunctionTimedOut:
            print("DFS Exceeded 10 Minutes\n")

for i in range(10):
    print("Scramble Length: {0}".format(i))
    LATester(i,10)