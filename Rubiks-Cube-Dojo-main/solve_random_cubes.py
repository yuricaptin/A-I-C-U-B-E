import random
import time
from rubik import solve
import rubik.cube as cube
from rubik.cube import Cube
from rubik.solve import Solver
from rubik.optimize import optimize_moves

SOLVED_CUBE_STR = "OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR"
#MOVES = ["L", "R", "U", "D", "F", "B", "M", "E", "S"]
MOVES = ["L", "R", "U", "D", "F", "B"]

def random_cube():
    """
    :return: A new scrambled Cube
    """
    scramble_moves = " ".join(random.choices(MOVES, k=10))
    #print(scramble_moves)
    #scramble_moves
    #test
    file = open('Data_Files/randomActions.txt', 'r')
    read = file.readline()
    scram = ""
    for i in range(0, len(read)):
        if read[i] != "'":        
            scram += "{a} ".format(a = read[i])
        else:
            scram += "{a} {b} ".format(a = read[i-1], b = read[i-1])
    scram.strip()    
    print(scram)        
    #print(read)
    #print(output)
    a = Cube(SOLVED_CUBE_STR)
    #a.sequence(scramble_moves)
    a.sequence(scram)
    return a


def run():
    #successes = 0
    #failures = 0

    #avg_opt_moves = 0.0
    #avg_moves = 0.0
    #avg_time = 0.0
    #while True:
    
    C = random_cube()
    solver = Solver(C)

    #start = time.time()
    solver.solve()
    #duration = time.time() - start

    if C.is_solved():
        print(solver.moves)
        opt_moves = optimize_moves(solver.moves)
        #successes += 1
        #avg_moves = (avg_moves * (successes - 1) + len(solver.moves)) / float(successes)
        #avg_time = (avg_time * (successes - 1) + duration) / float(successes)
        #avg_opt_moves = (avg_opt_moves * (successes - 1) + len(opt_moves)) / float(successes)
    else:
        #failures += 1
        #print(f"Failed ({successes + failures}): {C.flat_str()}")
        print("\nFAILED\n")

    #total = successes + failures
    #if total == 1 or total % 100 == 0:
    #    pass_percentage = 100 * successes / total
    #    print(f"{total}: {successes} successes ({pass_percentage:0.3f}% passing)"
    #            f" avg_moves={avg_moves:0.3f} avg_opt_moves={avg_opt_moves:0.3f}"
    #            f" avg_time={avg_time:0.3f}s")


if __name__ == '__main__':
    solve.DEBUG = False
    run()
