from collections import defaultdict

lines = open('day7.txt').read().strip().split('\n')

letter_map = {
    'T': 'A',
    # 'J': 'B',
    'J': '.',
    'Q': 'C',
    'K': 'D',
    'A': 'E'
}
    
def check_high_card(hand):
    if len(set(hand)) == 5: return True 
    return False


def check_one_pairs(hand):
    if len(set(hand)) == 4: return True 
    return False


def check_two_pairs(hand):
    value_counts = defaultdict(lambda:0)
    for v in hand:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1,2,2]: return True
    return False
    

def check_three_kind(hand):
    value_counts = defaultdict(lambda:0)
    for v in hand:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 1, 3]: return True
    return False


def check_full_house(hand):
    value_counts = defaultdict(lambda:0)
    for v in hand:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [2, 3]: return True
    return False


def check_four_kind(hand):
    value_counts = defaultdict(lambda:0)
    for v in hand:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1, 4]: return True
    return False


def check_five_kind(hand):
    if len(set(hand)) == 1: return True
    return False


def check_hand(hand):
    if check_high_card(hand):
        return 1
    if check_one_pairs(hand):
        return 2
    if check_two_pairs(hand):
        return 3
    if check_three_kind(hand):
        return 4
    if check_full_house(hand):
        return 5
    if check_four_kind(hand):
        return 6
    if check_five_kind(hand):
        return 7
    
def replacements(hand):
    if hand == '':
        return ['']
    
    # return [
    #     x + y
    #     for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
    #     for y in replacements(hand[1:])
    # ]

    result = []
    if hand[0] == 'J':
        for x in ('123456789TQKA'):
            for y in replacements(hand[1:]):
                result.append(x + y)
    else:
        for y in replacements(hand[1:]):
            result.append(hand[0] + y)

    return result


def classify(hand):
    print(hand)
    return max(map(check_hand, replacements(hand)))
    
def strength(hand):
    return (classify(hand), [letter_map.get(card, card) for card in hand])


points = 0
plays = []

for line in lines:
    hand, bid = line.split()
    # hand, bid = list(hand), int(bid)
    plays.append((hand, int(bid)))


plays.sort(key = lambda play: strength(play[0])) #it firsts sees the first element, and then goes to the alphabetical order in the second list

for rank, (hand, bid) in enumerate(plays, 1):
    points += rank * bid

print(points)