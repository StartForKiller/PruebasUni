print("Hello world")

file = open('prueba.txt', 'r')
lines = file.readlines()
for index in range(0, len(lines)):
    print(lines[index], end='')