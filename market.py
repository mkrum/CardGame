import utils as ut
from agent import Player
import Queue as Q

class MatchingEngine(object):

    def __init__(self):
        self.clear_book()

    def add_spread(self, spread):
        #bit hacky, but you get it
        self.bids.put(-1.0 * spread.bid)
        self.asks.put(spread.ask)

        try:
            self.bid_dir[spread.bid].append(spread.player)
        except KeyError:
            self.bid_dir[spread.bid] = [spread.player]

        try:
            self.ask_dir[spread.ask].append(spread.player)
        except KeyError:
            self.ask_dir[spread.ask] = [spread.player]

    def trade(self):
        top_ask = self.asks.get()
        top_bid = -1.0 * self.bids.get()
        
        while top_bid > top_ask:
            buyer = ut.select_random(self.bid_dir[top_bid])
            seller = ut.select_random(self.ask_dir[top_ask])
            price = ut.select_random([top_ask, top_bid])
            self.execute_trade(buyer, seller, price)
            
            if len(self.bid_dir[top_bid]) > 0:
                self.bids.put(-1.0 * top_bid)

            if len(self.ask_dir[top_ask]) > 0:
                self.asks.put(top_ask)

            top_ask = self.asks.get()
            top_bid = -1.0 * self.bids.get()
    
    def execute_trade(self, buyer, seller, price):
        buyer.positions[price] = 1
        seller.positions[price] = -1

    def clear_book(self):
        self.bids = Q.PriorityQueue()
        self.asks = Q.PriorityQueue()

        #bid and ask directories
        self.bid_dir = {}
        self.ask_dir = {}


class CardMarket(object):

    def __init__(self, players, n_cards):
        self.players = players
        self.n_cards = n_cards
        self.cards = range(1, n_cards + 1)
        self.data = [[] for _ in range(len(self.players)) ]
        self.draw()
        self.match = MatchingEngine()

    def run(self):
        self.match.clear_book()
        self.reveal()
        self.poll_players()
        self.match.trade()

    def poll_players(self):
        
        for p in self.players:
            self.match.add_spread(p.get_spread())

    def reveal(self):
        card = ut.remove_random(self.cards)
        for player in self.players:
            player.show_card(card)

    def draw(self):
        self.actual_price = 0

        for player in self.players:
            card = ut.remove_random(self.cards)
            self.actual_price += card
            player.take_card(card)

    def display(self):
        for player in self.players:
            player.info()

    def result(self):
        for player in self.players:
            player.info(self.actual_price)
     
    def get_data(self):
        for p in range(len(self.players)):
            self.data[p].append(self.players[p].price)
