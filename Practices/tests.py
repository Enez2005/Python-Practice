
def generator():
    i = 0
    while True:
        yield i
        i += 1


for i in generator():
    print(i)

