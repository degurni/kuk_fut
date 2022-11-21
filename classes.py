
import conf
import keys
import os
import pandas as pd
import pandas_ta as ta
from kucoin_futures.client import User, Trade, Market




class Gate_API:

    def __init__(self):
        print('Gate.io')


class Kucoin_API:

    def __init__(self):
        self.tf = conf.tf
        if os.path.isfile('keys.py'):
            self.key = keys.kucoin_key
            self.secret = keys.kucoin_secret
            self.pasw = keys.kucoin_pasw
        else:
            self.key = conf.kucoin_key
            self.secret = conf.kucoin_secret
            self.pasw = keys.kucoin_pasw
        self.client = Trade(key=self.key, secret=self.secret, passphrase=self.pasw)
        self.market = Market(key=self.key, secret=self.secret, passphrase=self.pasw)
        self.trade = Trade(key=self.key, secret=self.secret, passphrase=self.pasw)


        self.market = Market()

    def list_contracts(self):
        '''

        :return:
        {'symbol': 'XBTUSDTM',
        'rootSymbol': 'USDT',
        'type': 'FFWCSX',
        'firstOpenDate': 1585555200000,
        'expireDate': None,
        'settleDate': None,
        'baseCurrency': 'XBT',
        'quoteCurrency': 'USDT',
        'settleCurrency': 'USDT',
        'maxOrderQty': 1000000,
        'maxPrice': 1000000.0,
        'lotSize': 1,
        'tickSize': 1.0,
        'indexPriceTickSize': 0.01,
        'multiplier': 0.001,
        'initialMargin': 0.01,
        'maintainMargin': 0.005,
        'maxRiskLimit': 250000,
        'minRiskLimit': 250000,
        'riskStep': 125000,
        'makerFeeRate': 0.0002,
        'takerFeeRate': 0.0006,
        'takerFixFee': 0.0,
        'makerFixFee': 0.0,
        'settlementFee': None,
        'isDeleverage': True,
        'isQuanto': True,
        'isInverse': False,
        'markMethod': 'FairPrice',
        'fairMethod': 'FundingRate',
        'fundingBaseSymbol': '.XBTINT8H',
        'fundingQuoteSymbol': '.USDTINT8H',
        'fundingRateSymbol': '.XBTUSDTMFPI8H',
        'indexSymbol': '.KXBTUSDT',
        'settlementSymbol': '',
        'status': 'Open',
        'fundingFeeRate': 0.0001,
        'predictedFundingFeeRate': 0.0001,
        'openInterest': '23663291',
        'turnoverOf24h': 831796556.2098064,
        'volumeOf24h': 51453.478,
        'markPrice': 15975.76,
        'indexPrice': 15975.55,
        'lastTradePrice': 15982.0,
        'nextFundingRateTime': 3679792,
        'maxLeverage': 100,
        'sourceExchanges': ['huobi', 'Okex', 'Binance', 'Kucoin', 'Poloniex', 'Hitbtc'],
        'premiumsSymbol1M': '.XBTUSDTMPI',
        'premiumsSymbol8H': '.XBTUSDTMPI8H',
        'fundingBaseSymbol1M': '.XBTINT',
        'fundingQuoteSymbol1M': '.USDTINT',
        'lowPrice': 15883,
        'highPrice': 16639,
        'priceChgPct': -0.0354,
        'priceChg': -588}
        '''
        f = self.market.get_contracts_list()
        list = []
        for i in f:
            list.append(i['symbol'])
        return list

    def klines(self, symbol):
        '''
        [1668999300000,    - время        - Time
        0.30422,           - открытия     - Open
        0.30422,           - наибольшая   - High
        0.30273,           - наименьшая   - Low
        0.30386,           - закрытие     - Close
        8727]              - объём торгов - Volume
        :param symbol:
        :return:
        '''
        return self.market.get_kline_data(symbol=symbol, granularity=self.tf)

    def order(self, symbol, side, lever, size):
        f = self.trade.create_market_order(symbol=symbol, side=side, lever=lever, size=size)
        return f

    def position(self, symbol):
        '''

        :param symbol:
        :return:
        {'id': '637bef26ac0c180001958347',
        'symbol': 'ADAUSDTM',
        'autoDeposit': False,
        'maintMarginReq': 0.025,
        'riskLimit': 100000,
        'realLeverage': 7.94,
        'crossMode': False,
        'delevPercentage': 0.89,
        'openingTimestamp': 1669066534398,
        'currentTimestamp': 1669068367514,
        'currentQty': 1,
        'currentCost': 3.0382,                      Текущее значение позиции
        'currentComm': 0.00182292,
        'unrealisedCost': 3.0382,                   Нереализованная стоимость
        'realisedGrossCost': 0.0,
        'realisedCost': 0.00182292,
        'isOpen': True,
        'markPrice': 0.30172,
        'markValue': 3.0172,
        'posCost': 3.0382,
        'posCross': 0.09994,
        'posInit': 0.30382,
        'posComm': 0.00206521,
        'posLoss': 0.0,
        'posMargin': 0.40582521,
        'posMaint': 0.07832403,
        'maintMargin': 0.38482521,
        'realisedGrossPnl': 0.0,
        'realisedPnl': -0.00182292,
        'unrealisedPnl': -0.021,
        'unrealisedPnlPcnt': -0.0069,
        'unrealisedRoePcnt': -0.0691,
        'avgEntryPrice': 0.30382,
        'liquidationPrice': 0.27107,
        'bankruptPrice': 0.26344,
        'settleCurrency': 'USDT',
        'maintainMargin': 0.025,
        riskLimitLevel': 1}

        '''
        return self.trade.get_position_details(symbol=symbol)




if conf.exchange == 'Kucoin.com':
    api = Kucoin_API()
elif conf.exchange == 'Gate.io':
    api = Gate_API()

class Bot:
    def __init__(self):
        pass

    def list_contracts(self):
        return api.list_contracts()

    def klines(self, symbol):
        return api.klines(symbol=symbol)

    def create_df(self, symbol):
        data = Bot().klines(symbol=symbol)
        tm, close, high, low, opn, vol = [], [], [], [], [], []
        if conf.exchange == 'Kucoin.com':
            for i in data:
                tm.append(int(i[0]))
                close.append(float(i[4]))
                high.append(float(i[2]))
                low.append(float(i[3]))
                opn.append(float(i[1]))
                vol.append(float(i[5]))
        df = pd.DataFrame({'Time': tm,
                           'Close': close,
                           'High': high,
                           'Low': low,
                           'Open': opn,
                           'Volume': vol})
        df['Time'] = pd.to_datetime(df.Time, unit='ms')
        df.set_index('Time', inplace=True)
        # df = df[df.High != df.Low]  # удаляем свечи без движения
        # добавляем индикатор CCI
        df = Indicater().cci_1(df=df)
        # df.to_csv('dat.csv')  # записываем датафрейм в файл
        return df

class Indicater:

    def __init__(self):
        pass

    def cci_1(self, df):
        df['CCI'] = ta.cci(df.High, df.Low, df.Close, length=20)
        return df

