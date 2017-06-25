
import numpy as np
import random

# E[sum of subset N] = average card value * N
def expected_sum(cards, N):
    return sum(cards)/(len(cards) * 1.0) * N

def random_sample(some_list, N):
    return [ some_list[i] for i in sorted(random.sample(xrange(len(some_list)), N)) ]

def remove_random(cards):
    index = random.randrange(len(cards))
    return cards.pop(index)

def random_sum(cards, N):
    return sum(random_sample(cards, N))

def select_random(cards):
    selection = random.choice(cards)
    cards.remove(selection)
    return selection

if __name__ == '__main__':
    cards = range(1, 30)

    print(random_sample(cards, 7))
    print(random_sum(cards, 7))
    print(expected_sum(cards, 7))
    
    sums = []
    for _ in range(200000):
        sums.append(random_sum(cards, 7))

    print(sum(sums)/(len(sums) * 1.0))

    print(cards)
    print(remove_random(cards))
    print(cards)
