x = 4
y = 0
try:
    z = x / y
except ZeroDivisionError:
    print("You cannot divide a number between zero")
except ValueError:
    print("Some value is an error")
except:
    print("The operation cannot be realized")
else:
    print("The operation was realized")
