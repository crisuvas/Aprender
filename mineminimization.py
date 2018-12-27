from pulp import *
mineA = LpVariable("mineA", 0)
mineB = LpVariable("mineB", 0)

mineAHigh = 1
mineAMid = 2
mineALow = 4

mineBHigh = 2
mineBMid = 2
mineBLow = 2

requirementHigh = 70
requirementMid = 130
requirementLow = 150

costMineA = 500
costMineB = 750

problem = LpProblem("problem", LpMinimize)
problem += (mineA * mineAHigh) + (mineB * mineBHigh) >= requirementHigh
problem += (mineA * mineAMid) + (mineB * mineBMid) >= requirementMid
problem += (mineA * mineALow) + (mineB * mineBLow) >= requirementLow
problem += (mineA * costMineA) + (mineB * costMineB)

status = problem.solve()
print(LpStatus[status])
print(value(mineA))
print(value(mineB))
