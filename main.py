
from market import CardMarket
from agent import PlayerFactory
import matplotlib.pyplot as plt

market = CardMarket(PlayerFactory(7, 30), 30)

market.get_data()
for _ in range(23):
    market.run()
    market.get_data()

market.result()

for d in market.data:
    plt.plot(range(24), d)


for p in market.players:
    print(p.positions)

plt.show()

