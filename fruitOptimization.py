from pulp import *

a = LpVariable("a", 0)
b = LpVariable("b", 0)

aOrange = 1
aApple = 2
aBanana = 1

bOrange = 2
bApple = 1
bBanana = 1

aEarn = 1200
bEarn = 1400

orange = 800
apple = 800
banana = 500

problem = LpProblem("problem", LpMaximize)
problem += (a * aOrange) + (b * bOrange) <= orange
problem += (a * aApple) + (b * bApple) <= apple
problem += (a * aBanana) + (b * bBanana) <= banana
problem += (a * aEarn) + (b * bEarn)
status = problem.solve()

print(LpStatus[status])
print(value(a))
print(value(b))
print("The earn is %s" % (value(a) * aEarn + value(b) * bEarn))
