from collections import defaultdict

lines = open('day41.txt').read().strip().split('\n')

games = 0
cards_dict = defaultdict(int)

for card, line in enumerate(lines):
    cards_dict[card] += 1
    points = 0
    iter = 0
    w_numbers = line.split(':')[1].split('|')[0].split()
    m_numbers = line.split(':')[1].split('|')[1].split()
    val = len(set(w_numbers) & set(m_numbers)) # one way to do it

    for i in w_numbers: # other way to do it
        if i in m_numbers:
            iter += 1
            if iter == 1:
                points = 1
            else:
                points *= 2

    for j in range(iter):
        cards_dict[card + 1 + j] += cards_dict[card]

    games += points
    print('='*80)

print(cards_dict)
print(games)
print(sum(cards_dict.values()))
