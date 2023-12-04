from collections import defaultdict

lines = open('day2.txt').read().strip().split('\n')
soma = 0
for line in lines:
    ok = True
    id_, line = line.split(':')
    for l in line.split(';'):
        for balls in l.split(','):
            n, color = balls.split()
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                ok = False
    if ok:
        soma += int(id_.split()[-1])


print(soma)
    
