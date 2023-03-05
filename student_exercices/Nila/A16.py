# a
def a():
    antwort = int(input("ein zahl eigeben"))
    for value in range(0, antwort + 1):
        if value % 2 == 0:
            print(value)


a()


# b
def b(x):
    return list(range(1, x + 1))


print(b(5))
