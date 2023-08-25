#Multiplicar Matrices
print("Introduce la primera matriz")
a = [int(input()),int(input()),int(input()),int(input())]
print("Introduce la segunda matriz")
b = [int(input()),int(input()),int(input()),int(input())]

result = [a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3]]
print(result)
result = [a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]]
print(result)


