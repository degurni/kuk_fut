import sys

import conf
import keys
import os
import pandas as pd
import pandas_ta as ta
import datetime
import json
from kucoin_futures.client import User, Trade, Market
from decimal import Decimal




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

    def contract(self, symbol):
        '''
        ???????????????? ???????????????????? ?? ?????????????? ???????????????? ????????
        :param symbol:
        :return:
        {'symbol': 'ADAUSDTM',
        'rootSymbol': 'USDT',
        'type': 'FFWCSX',
        'firstOpenDate': 1603180800000,
        'expireDate': None,
        'settleDate': None,
        'baseCurrency': 'ADA',
        'quoteCurrency': 'USDT',
        'settleCurrency': 'USDT',
        'maxOrderQty': 1000000,
        'maxPrice': 1000000.0,
        'lotSize': 1,                              ???????????????????? ?????????? ?? ??????????
        'tickSize': 1e-05,
        'indexPriceTickSize': 1e-05,
        'multiplier': 10.0,                        ??????-???? ?????????? ?? ????????
        'initialMargin': 0.05,
        'maintainMargin': 0.025,
        'maxRiskLimit': 200000,
        'minRiskLimit': 200000,
        'riskStep': 100000,
        'makerFeeRate': 0.0002,                     ???????????????? ??????????????
        'takerFeeRate': 0.0006,                     ???????????????? ??????????????
        'takerFixFee': 0.0,
        'makerFixFee': 0.0,
        'settlementFee': None,
        'isDeleverage': True,
        'isQuanto': True,
        'isInverse': False,
        'markMethod': 'FairPrice',
        'fairMethod': 'FundingRate',
        'fundingBaseSymbol': '.ADAINT8H',
        'fundingQuoteSymbol': '.USDTINT8H',
        'fundingRateSymbol': '.ADAUSDTMFPI8H',
        'indexSymbol': '.KADAUSDT',
        'settlementSymbol': '',
        'status': 'Open',
        'fundingFeeRate': 0.0001,
        'predictedFundingFeeRate': 0.0001,
        'openInterest': '9324183',                 ???????????????? ?????????????? ???? ?????????? ?? ??????????
        'turnoverOf24h': 6367496.96032071,
        'volumeOf24h': 20277500.0,
        'markPrice': 0.31036,
        'indexPrice': 0.31033,
        'lastTradePrice': 0.31027,                 ?????????????? ???????? ?? ???????????????? ????????????
        'nextFundingRateTime': 24554763,
        'maxLeverage': 20,                         ???????????????????????? ??????????
        'sourceExchanges': ['huobi', 'Okex', 'Binance', 'Kucoin', 'Bittrex'],
        'premiumsSymbol1M': '.ADAUSDTMPI',
        'premiumsSymbol8H': '.ADAUSDTMPI8H',
        'fundingBaseSymbol1M': '.ADAINT',
        'fundingQuoteSymbol1M': '.USDTINT',
        'lowPrice': 0.3072,
        'highPrice': 0.31988,
        'priceChgPct': -0.0257,
        'priceChg': -0.0082}

        '''
        return self.market.get_contract_detail(symbol=symbol)

    def klines(self, symbol):
        '''
        [1668999300000,    - ??????????        - Time
        0.30422,           - ????????????????     - Open
        0.30422,           - ????????????????????   - High
        0.30273,           - ????????????????????   - Low
        0.30386,           - ????????????????     - Close
        8727]              - ?????????? ???????????? - Volume
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
        'currentQty': 1,                            ?????????????? ???????????????????? ????????????????????
        'currentCost': 3.0382,                      ?????????????? ???????????????? ??????????????
        'currentComm': 0.00182292,
        'unrealisedCost': 3.0382,                   ?????????????????????????????? ??????????????????
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

    def position_list(self):
        '''

        :return:
        {'id': '637c556c1f7a310001486a87',
        'symbol': 'DOTUSDTM',
        'autoDeposit': False,
        'maintMarginReq': 0.01,
        'riskLimit': 200000,
        'realLeverage': 10.44,
        'crossMode': False,
        'delevPercentage': 0.91,
        'openingTimestamp': 1669092716170,
        'currentTimestamp': 1669095969969,
        'currentQty': 1,                            ?????????????? ???????????????????? ????????????????????
        'currentCost': 5.179,                       ?????????????? ???????? ??????????
        'currentComm': 0.0031074,
        'unrealisedCost': 5.179,
        'realisedGrossCost': 0.0,
        'realisedCost': 0.0031074,
        'isOpen': True,
        'markPrice': 5.157,
        'markValue': 5.157,
        'posCost': 5.179,
        'posCross': 0,
        'posInit': 0.5179,
        'posComm': 0.00341814,
        'posLoss': 0.0,
        'posMargin': 0.52131814,
        'posMaint': 0.05530136,
        'maintMargin': 0.49931814,
        'realisedGrossPnl': 0.0,
        'realisedPnl': -0.0031074,
        'unrealisedPnl': -0.022,
        'unrealisedPnlPcnt': -0.0042,
        'unrealisedRoePcnt': -0.0425,
        'avgEntryPrice': 5.179,
        'liquidationPrice': 4.713,
        'bankruptPrice': 4.661,
        'settleCurrency': 'USDT',
        'isInverse': False,
        'maintainMargin': 0.01}
        '''
        f = self.trade.get_all_position()
        return f

    def single_order(self, order_id):
        '''

        :param order_id:
        :return:
        {'id': '637c95a448071900011cae43',
        'symbol': 'DASHUSDTM',
        'type': 'market',
        'side': 'sell',
        'price': None,
        'size': 1,
        'value': '0.3467',                              ?????????????????? ????????????
        'dealValue': '0.3467',                          ?????????????????????? ???????????? ??????????????
        'dealSize': 1,
        'stp': '',
        'stop': '',
        'stopPriceType': '',
        'stopTriggered': False,
        'stopPrice': None,
        'timeInForce': 'GTC',
        'postOnly': False,
        'hidden': False,
        'iceberg': False,
        'leverage': '1',
        'forceHold': False,
        'closeOrder': False,
        'visibleSize': None,
        'clientOid': 'a3c07de36a4711eda65c2006101a3dc6',
        'remark': None,
        'tags': None,
        'isActive': False,
        'cancelExist': False,
        'createdAt': 1669109156000,
        'updatedAt': 1669109157000,
        'endAt': 1669109157000,
        'orderTime': 1669109156957247121,
        'settleCurrency': 'USDT',
        'status': 'done',
        'filledValue': '0.3467',                            ???????????????????? ?????????????????????? ??????????????
        'filledSize': 1,
        'reduceOnly': False}
        '''
        return self.trade.get_order_details(orderId=order_id)

    def inf_contract(self, symbol):
        return self.market.get_contract_detail(symbol=symbol)




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
        # df = df[df.High != df.Low]  # ?????????????? ?????????? ?????? ????????????????
        # ?????????????????? ?????????????????? CCI
        df = Indicater().cci_1(df=df)
        # df.to_csv('dat.csv')  # ???????????????????? ?????????????????? ?? ????????
        return df

    def tm(self):
        """
        :return: ???????????????????? ?????????????? ?????????? ?? ?????????????? ????:????:????
        """
        return datetime.datetime.now().strftime('%H:%M:%S')

    def debug(self, var, inf):
        """
        :param var:
        :param inf:
        :return:
        """
        time = self.tm() if var == 'debug' else None
        if conf.debug == 'inform':
            if var == 'inform':
                print(inf)
            elif var == 'debug':
                print('\033[32m {} - {} \033[0;0m'.format(time, inf))
            else:
                print('\033[31m {} \033[0;0m'.format(inf))
        if conf.debug == 'debug':
            if var == 'debug':
                print('\033[32m {} - {} \033[0;0m'.format(time, inf))
            else:
                print('\033[31m {} \033[0;0m'.format(inf))
        if conf.debug == 'error':
            if var == 'error':
                print('\033[31m {} \033[0;0m'.format(inf))

    def write_json(self, data, para):
        """
        :param data:
        :param para:
        :return:
        """
        with open('stock/{}.json'.format(para), 'w') as f:
            json.dump(data, f, indent=2)

    def read_json(self, para):
        """
        :param para:
        :return:
        """
        try:
            with open('stock/{}.json'.format(para)) as f:
                data = json.load(f)
        except FileNotFoundError:
            Bot().write_json(data=[], para=para)
        else:
            return data

    def is_file_json(self):
        '''
        ???????? ???????????????????????????????? ?????????? ??????. ???? ??????????????
        ?? ?????????????????? ?????? ???????????? ??????????????
        :return:
        '''
        kol_poz = 0
        for i in conf.whait_list:
            poz = api.position(i)
            if poz['currentQty'] == 0 and not os.path.isfile('stock/{}.json'.format(i)):
                Bot().write_json([], i)
            elif poz['currentQty'] != 0:
                data = Bot().read_json(i)
                if len(data) > 0:
                    Bot().debug('debug', '{}: ?????????????? {} ??????????????'.format(i, len(data)))
                    kol_poz += 1
                else:
                    Bot().debug('error', '{}: ?????????????? ?????????????? ???? ??????????'.format(i))
                    sys.exit(0)
        return kol_poz



    def position(self, symbol):
        return api.position(symbol=symbol)

    def create_position(self, symbol, side, lever):
        # ?????????????????????? ??????-???? ?????????? ?? ??????????
        g = api.contract(symbol=symbol)
        tick_size = str(Decimal(str(g['tickSize'])))
        size = g['lotSize']
        if g['maxLeverage'] < lever:
            lever = g['maxLeverage']
        size_lot = conf.size_usdt / g['lastTradePrice'] / g['multiplier'] * lever
        if size_lot > g['lotSize']:
            size = size_lot
        # ?????????????? ??????????
        f = api.order(symbol=symbol, side=side, lever=lever, size=size)
        # ???????????????? ???????????????????? ???? ID ????????????
        s = api.single_order(order_id=f['orderId'])
        mult_play = (api.inf_contract(symbol=symbol))['multiplier']
        inf = {'id': s['id'],
               'symbol': s['symbol'],
               'size': s['size'],
               'price': str(float(s['value']) / float(s['size'])),
               'tick_size': tick_size,
               'lever': s['leverage'],
               'multiplier': mult_play,
               'mod_price': float(s['value']) / float(s['size']),
               'mp': float(s['value']) / float(s['size']) / 100 * conf.perc_mod_price}
        data = Bot().read_json(para=s['symbol'])
        data.append(inf)
        Bot().write_json(data=data, para=s['symbol'])
        return True

    def create_order(self, symbol, side, lever, size):
        # ?????????????? ??????????
        f = api.order(symbol=symbol, side=side, lever=lever, size=size)
        # ???????????????? ???????????????????? ???? ID ????????????
        s = api.single_order(order_id=f['orderId'])
        # ???????????????? ???????????????????? ???? ???????? ?????????????? ???????? ???????????????? ????????
        data = Bot().read_json(para=s['symbol'])
        inf = {'id': s['id'],
               'symbol': s['symbol'],
               'size': s['size'],
               'price': str(float(s['value']) / float(s['size'])),
               'tick_size': data[-1]['tick_size'],
               'lever': s['leverage'],
               'multiplier': data[-1]['multiplier'],
               'mod_price': float(s['value']) / float(s['size']),
               'mp': float(s['value']) / float(s['size']) / 100 * conf.perc_mod_price}
        data.append(inf)
        Bot().write_json(data=data, para=s['symbol'])
        return inf

    def del_order(self, symbol, side, lever, size):
        p = False
        # ?????????????? ??????????
        api.order(symbol=symbol, side=side, lever=lever, size=size)
        data = Bot().read_json(para=symbol)
        data.pop(-1)
        if len(data) == 0:
            p = True
        else:
            data[0]['mod_price'] = data[0]['mod_price'] - data[0]['mp']
            if data[0]['mod_price'] <= 0:
                api.order(symbol=symbol, side=side, lever=lever, size=size)
                data.pop(0)
            if len(data) == 0:
                p = True
        Bot().write_json(data=data, para=symbol)
        return p

    def single_order(self, order_id):
        f = api.single_order(order_id=order_id)
        print(f)

    def check_profit_long_1(self, df, para):
        k = False
        data = Bot().read_json(para)
        gen_size = float(data[-1]['size'])  # ???????????????????? ???????????????????? ?? ??????????
        mult_play = data[-1]['multiplier']
        navar = 1 + (conf.navar / 100)
        mimo = 1 - (conf.navar / 100)
        navar_price = float(data[-1]['price']) * navar / mult_play
        mimo_price = float(data[-1]['price']) * mimo / mult_play
        navar_price = Decimal(navar_price)
        navar_price = navar_price.quantize(Decimal(data[-1]['tick_size']))
        mimo_price = Decimal(mimo_price)
        mimo_price = mimo_price.quantize(Decimal(data[-1]['tick_size']))
        # Bot().debug('debug', '?????????????? ???????? - {}'.format(df.Close[-1]))
        Bot().progress(para=para, orders=len(data), navar_price=navar_price, price_close=df.Close[-1],
                       mimo_price=mimo_price, side='long')
        if float(navar_price) < df.Close[-1] and df.CCI[-1] < df.CCI[-2]:
            Bot().debug('inform', '{} : ?????????????? {} ????????????????????'.format(para, gen_size))
            s = Bot().del_order(symbol=para, side='sell', lever=data[-1]['lever'], size=gen_size)
            if s:
                k = True
        elif mimo_price > df.Close[-1] and df.CCI[-1] > df.CCI[-2]:
            # print('navar - {}, mimo - {}, Close - {}'.format(navar_price, mimo_price, df.Close[-1]))
            s = Bot().create_order(symbol=para, side='buy', lever=data[-1]['lever'], size=gen_size)
            Bot().debug('inform', '{} : ?????????????????? {} ???????????????????? ???? ???????? {}'.
                        format(para, s['size'], float(s['price']) / mult_play))
        return k

    def check_profit_short_1(self, df, para):
        k = False
        data = Bot().read_json(para)
        gen_size = float(data[-1]['size'])  # ???????????????????? ???????????????????? ?? ??????????
        mult_play = data[-1]['multiplier']
        navar = 1 - (conf.navar / 100)
        mimo = 1 + (conf.navar / 100)
        navar_price = float(data[-1]['price']) * navar / mult_play
        mimo_price = float(data[-1]['price']) * mimo / mult_play
        navar_price = Decimal(navar_price)
        navar_price = navar_price.quantize(Decimal(data[-1]['tick_size']))
        mimo_price = Decimal(mimo_price)
        mimo_price = mimo_price.quantize(Decimal(data[-1]['tick_size']))
        # Bot().debug('debug', '?????????????? ???????? - {} CCI_1 - {} CCI_2 - {}'.format(df.Close[-1], df.CCI[-1], df.CCI[-2]))
        Bot().progress(para=para, orders=len(data), navar_price=navar_price, price_close=df.Close[-1],
                       mimo_price=mimo_price, side='short')
        if float(navar_price) > df.Close[-1] and df.CCI[-1] >= df.CCI[-2]:
            Bot().debug('inform', '{} : ?????????????? {} ????????????????????'.format(para, gen_size))
            s = Bot().del_order(symbol=para, side='buy', lever=data[-1]['lever'], size=gen_size)
            if s:
                k = True
        elif mimo_price < df.Close[-1] and df.CCI[-1] <= df.CCI[-2]:
            s = Bot().create_order(symbol=para, side='sell', lever=data[-1]['lever'], size=gen_size)
            Bot().debug('inform', '{} : ?????????????????? {} ???????????????????? ???? ???????? {}'.
                        format(para, s['size'], float(s['price']) / mult_play))
        return k

    def progress(self, para, orders, navar_price, price_close, mimo_price, side):
        lev = 20
        kr = '\033[31m'
        gr = '\033[32m'
        sbros = '\033[0m'
        pruf = 10
        navar_price = float(navar_price)
        mimo_price = float(mimo_price)
        z = '.'
        pr = para
        if side == 'short':
            pr = '{}{}{}{}{}'.format(sbros, kr, para, sbros, gr)
            delen = (mimo_price - navar_price) / pruf
            if price_close <= navar_price:
                lev = 0
                z = '<'
            else:
                lev = round((price_close - navar_price) / delen)
                if lev > pruf:
                    lev = pruf
                    z = '>'

        elif side == 'long':
            # print('navar - {} | mimo - {}'.format(navar_price, mimo_price))
            delen = (navar_price - mimo_price) / pruf
            if price_close >= navar_price:
                lev = 0
                z = '<'
            else:
                lev = round((navar_price - price_close) / delen)
        if lev > pruf:
            lev = pruf
            z = '>'
        prav = pruf - lev

        time = self.tm()
        print(' {}{} - {}: ?????????????? {}, {} {}{}{}{}{}{} {}{}'.format(
            gr, time, pr, orders, navar_price, kr, z * lev, gr, z * prav, sbros, gr, mimo_price, sbros))



class Indicater:

    def __init__(self):
        pass

    def cci_1(self, df):
        df['CCI'] = ta.cci(df.High, df.Low, df.Close, length=20)
        return df

