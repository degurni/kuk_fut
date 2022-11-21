

from classes import Kucoin_API, Bot

bot = Bot()

symbol = 'ADAUSDTM'

# s = Kucoin_API().order(symbol, 'buy', '10', 1)

s = Kucoin_API().position(symbol)


print(s)
