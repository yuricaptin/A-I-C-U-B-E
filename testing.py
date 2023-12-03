import BFS
import DFS
import ReflexRubiks as Reflex
import time
import Cubing
import func_timeout as ft


def LATester(scramble_length,num_times):
   
    for i in range(num_times):
        print("Round: {0}\n".format(i+1))
        #gen cube
        cube=Cubing.Cube(scramble_length)
        print("Starting Cube: {0}".format(cube.MOVE_LIST))
        #BFS
        if(scramble_length<3):
            try:
                print("BFS")
                start=time.perf_counter()
                a=ft.func_timeout(600,BFS.bfs, args=(cube, cube.GOAL_STATE))
                end=time.perf_counter()
                print("num moves: {0}\nTotal time: {1}\n\n".format(len(a),end-start))
            except ft.FunctionTimedOut:
                print("BFS Exceeded 10 Minutes\n")
            try:
                print("Reflex")
                start=time.perf_counter()
                a=ft.func_timeout(600,Reflex.REFLEX_SOL, args=(cube, cube.GOAL_STATE))
                end=time.perf_counter()
                print("num moves: {0}\nTotal time: {1}\n\n".format(len(a),end-start))
            except ft.FunctionTimedOut:
                print("Reflex Exceeded 10 Minutes\n")
        try:
            print("DFS")
            start=time.perf_counter()
            a=ft.func_timeout(600,DFS.dfs, args=(cube, cube.GOAL_STATE))
            end=time.perf_counter()
            print("num moves: {0}\nTotal time: {1}\n\n".format(len(a),end-start))
        except ft.FunctionTimedOut:
            print("DFS Exceeded 10 Minutes\n")

for i in range(3,11):
    print("Scramble Length: {0}".format(i))
    LATester(i,10)