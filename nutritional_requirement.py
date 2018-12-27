from pulp import *

a = LpVariable("a", 0)
b = LpVariable("b", 0)

aProtein = 2
aCarbohydrate = 6
aFat = 1

bProtein = 1
bCarbohydrate = 1
bFat = 3

aCost = 600
bCost = 400

requirementP = 8
requirementC = 12
requirementF = 9

problem = LpProblem("problem", LpMinimize)
problem += (a * aProtein) + (b * bProtein) >= requirementP
problem += (a * aCarbohydrate) + (b * bCarbohydrate) >= requirementC
problem += (a * aFat) + (b * bFat) >= requirementF
problem += (a * aCost) + (b * bCost)
status = problem.solve()

print(LpStatus[status])
print(value(a))
print(value(b))
print("The cheapest cost is %s" % (value(a) * aCost + value(b) * bCost))
