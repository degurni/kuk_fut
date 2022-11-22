
import conf
from datetime import datetime
import time
import sys
import os
from classes import Kucoin_API, Bot

bot = Bot()

symbol = 'ADAUSDTM'

# s = Kucoin_API().order(symbol, 'buy', '10', 1)
#
# s = Kucoin_API().position(symbol)
#
#
# print(s)


def kuc_fut():
    start_time = datetime.now()
    max_zakaz = 0
    paras = conf.whait_list
    # Проверяем наличие вспомогательных файлов
    for i in paras:
        if not os.path.isfile('stock/{}.json'.format(i)):
            bot.write_json([], i)
    kol_poz = 0
    # Проверяем количество открытых позиций
    poz_list = Kucoin_API().position_list()
    # print(poz_list)
    try:
        if poz_list['data'] != []:
            for i in poz_list:
                if i['currentQty'] != 0 and i['symbol'] in paras:
                    kol_poz += 1
                else:
                    if os.path.isfile('stock/{}.json'.format(i['symbol'])):
                        bot.write_json([], i['symbol'])
    except TypeError:
        pass





    while True:
        if kol_poz < conf.max_poz:
            for para in paras:
                if kol_poz >= conf.max_poz:
                    break
                poz = bot.position(symbol=para)  # проверяем открыта ли позиция
                time.sleep(conf.sl)
                if poz['currentQty'] == 0:
                    bot.debug('debug', '{}: Позиция ещё не открыта'.format(para))
                    df = bot.create_df(symbol=para)  # создаём датафрейм с последними свечами и сигналами индикаторов
                    if df.CCI[-2] < df.CCI[-1] < (conf.predel_cci * -1):
                        bot.debug('inform', '{}: Точка входа в LONG'.format(para))
                        # Заходим в позицию по рынку . заносим данные заказа в файл
                        t = bot.create_position(symbol=para, side='buy', lever=1, size=1)
                        time.sleep(conf.sl)
                        if t:
                            kol_poz += 1

                    if df.CCI[-2] > df.CCI[-1] > conf.predel_cci:
                        bot.debug('inform', '{}: Точка входа в SHORT'.format(para))
                        # Заходим в позицию по рынку . заносим данные заказа в файл
                        t = bot.create_position(symbol=para, side='sell', lever=1, size=1)
                        time.sleep(conf.sl)
                        if t:
                            kol_poz += 1

        if kol_poz:
            for para in paras:
                poz = bot.position(symbol=para)
                time.sleep(conf.sl)
                if poz['currentQty'] > 0:  # если уже открыта LONG-позиция
                    df = bot.create_df(symbol=para)  # создаём датафрейм с последними свечами и сигналами индикаторов
                    t = bot.check_profit_long_1(df=df, para=para)
                    if t:
                        kol_poz -= 1
                    time.sleep(conf.sl)

                if poz['currentQty'] < 0:  # если уже открыта SHORT-позиция
                    df = bot.create_df(symbol=para)  # создаём датафрейм с последними свечами и сигналами индикаторов
                    t = bot.check_profit_short_1(df=df, para=para)
                    if t:
                        kol_poz -= 1
                    time.sleep(conf.sl)






        new_time = datetime.now() - start_time
        nt = ((str(new_time)).split('.'))[0]
        print('Бот в работе - {} : MAX заказов - {}'.format(nt, max_zakaz))

        time.sleep(conf.sleep)



# try:

if __name__ == '__main__':
    kuc_fut()
# except KeyboardInterrupt:
#     bot.debug('inform', 'Работа бота завершена')
#     sys.exit(0)
# except Exception as e:
#     bot.debug('inform', 'Возникла непредвиденная ошибка - {}'.format(e))
#     time.sleep(conf.sleep)
#     bot.debug('inform', 'Перезапускаюсь...')

