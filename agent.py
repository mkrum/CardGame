
import utils as ut


class Player:
    def __init__(self, name, n_cards, n_players):
        self.name = name
        self.n_cards = n_cards
        self.unknown_cards = range(1, n_cards + 1)
        self.n_players = n_players
        self.positions = {}

    def take_card(self, card):
        self.unknown_cards.remove(card)
        self.card = card
        self.update_price()

    def show_card(self, card):
        self.unknown_cards.remove(card)
        self.update_price()

    def info(self, actual_price=None):
        if actual_price is not None: 
            print('{} {} {} {}'.format(self.name, self.card, self.price, self.pnl(self.price)))
        else:
            print('{} {} {} {}'.format(self.name, self.card, self.price, self.pnl(actual_price)))

    def update_price(self):
        self.price = ut.expected_sum(self.unknown_cards, (self.n_players) - 1) + self.card

    def get_spread(self):
        self.update_price()
        return Spread(self.price - 5, self.price + 5, self)

    def make_trade(self, price, quantity):
        self.positions[price] = quantity

    def pnl(self, price):
        total = 0
        for p in self.positions.keys():
            total += (price - p) * self.positions[p]
        return total

class Spread(object):

    def __init__(self, bid, ask, player):
        self.bid = bid
        self.ask = ask
        self.player = player

def PlayerFactory(N, n_cards, types=None, names=None):
    players = []
    if types is not None:
        pass 
    else:
        for n in range(N):
            if names is not None:
                players.append(Player(names[n], n_cards, N))
            else:
                players.append(Player(str(n), n_cards, N))


    return players

if __name__ == '__main__':
    SimplePlayer('test', 30, 7)
    


