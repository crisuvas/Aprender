def value_less_40():
    i = 0
    x = 55
    while i <= 25:
        x -= 3
        if x <= 39:
            print("X values less than 40")
            break
        i += 1
        print(x)


def range_greater():
    a = b = c = 0
    for i in range(0, 7):
        a += 1
        if a >= b:
            b = a + 1
        if b >= c:
            c = b + 1
        print("a = %s, b = %s, c= %s" % (a, b, c))


def division_values():
    i = 0
    a = 32405
    b = 200
    while i <= 100:
        c = a / b
        i += 1
        b -= 1
        print("%s. The division is %s" % (i, c))


division_values()