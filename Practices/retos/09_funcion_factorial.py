print("Introduce el numero que deseas sacar el factorial")

y = int(input())
x = y

for cantidad in range(y-1):

    x = x * (y - (cantidad +1))

print(x)

