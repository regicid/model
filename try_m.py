import sys
mu = float(sys.argv[1])
M = [.025,.075,.125,.15,.175,.225,.25]
from model import Population
import pickle
import numpy as np
for m in M:
	P = Population(mu,m=m,initial_v=0,σ=6,update_rate = .1)
	P.round(100)
	np.save(f"Results/result2_{np.round(mu,2)}_m={m}_v=0.npy",P.frequencies)
	P = Population(mu,m=m,initial_v=1,σ=6,update_rate = .1)
	P.round(100)
	np.save(f"Results/result2_{np.round(mu,2)}_m={m}_v=1.npy",P.frequencies)
