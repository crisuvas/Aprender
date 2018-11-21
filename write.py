def write_text(a, b, c):
    file = open("write.txt", "w")
    file.write(a)
    file.write(b)
    file.write(c)
    file.close()


write_text("Hello", "my", "Friend")


def read_text():
    file = open("write.txt", "r")
    return file.read(), file.close()


print(read_text())
