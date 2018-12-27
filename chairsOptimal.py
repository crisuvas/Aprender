from pulp import *
s1 = LpVariable("s1", 0)
s2 = LpVariable("s2", 0)

s1WF = 1/3
s2WF = 1/2

s1MW = 1/3
s2MW = 1/6

limitWF = 100
limitMW = 80

s1Earn = 15
s2Earn = 10

problem = LpProblem("problem", LpMaximize)
problem += (s1WF * s1) + (s2WF * s2) <= limitWF
problem += (s1MW * s1) + (s2MW * s2) <= limitMW
problem += (s1 * s1Earn) + (s2 * s2Earn)

status = problem.solve()

print(LpStatus[status])
print(value(s1))
print(value(s2))
print("The best earn is %s" % (value(s1) * s1Earn + value(s2) * s2Earn))
