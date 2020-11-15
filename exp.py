exp = []

with open('exp.txt', 'r', encoding='utf8') as fin:
    index = 0
    for line in fin.readlines():
        index += 1

        exp.append(int(line.split(' ')[1]))

print(exp)