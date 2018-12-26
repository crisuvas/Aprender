from pulp import *

football = LpVariable("football", 0, 400)
basketball = LpVariable("basketball", 0, 300)

materialF = 100
materialB = 125

availableMaterial = 50000

earnF = 50
earnB = 40

problem = LpProblem("problem", LpMaximize)

problem += (materialF * football) + (materialB * basketball) <= availableMaterial

problem += (football * earnF) + (basketball * earnB)

status = problem.solve()

print(LpStatus[status])
print(value(football))
print(value(basketball))
