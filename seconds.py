def seconds():
    i = j = 0
    list_sec = []
    while i <= 5:
        while j <= 9:
            x = ":" + str(i) + str(j)
            j += 1
            list_sec.append(x)
        j = 0
        i += 1
    return list_sec


y = seconds()
print(y)