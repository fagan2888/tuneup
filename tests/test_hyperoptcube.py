from tuneup.objective_functions import OBJECTIVES
from tuneup.hyperoptcube import hyperopt_cube

def test_cube():
    for objective, scale in OBJECTIVES.items():
        best = hyperopt_cube(objective=objective,scale=scale,n_trials=5)
        print(best)

if __name__=="__main__":
    test_cube()