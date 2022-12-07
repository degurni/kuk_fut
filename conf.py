
'''
Стратегия работает на бирже Kucoin.com
Вход в сделку по индикатору CCI, если последнее значение CCI больше  предпоследнего
и ниже нижнего предела CCI( - 100 (можно менять)) тогда LONG,
если последнее значение CCI меньше предпоследнего и выше верхнего предела CCI (100) тогда SHORT
Докупает когда цена пойдёт в не ту сторону на 0.5% (navar) и индикатор CCI сломается
Продаёт когда цена пойдёт в нужную сторону на 0.5% (navar) и индикатор CCI сломается
Продаёт по одному ордеру, если ордеров много то при продаже последнего ордера
у самого первого цена входа уменьшится на  2 % (perc_mod_price(можно менять)) и т.д пока
не станет меньше 0 и не продастся


'''

exchange = 'Kucoin.com'

# Kucoin.com
kucoin_key = ''
kucoin_secret = ''
kucoin_pasw = ''
tf = 5  # 1,5,15,30,60,120,240,480,720,1440,10080
'''
['XBTUSDTM', 'ETHUSDTM', 'BCHUSDTM', 'BSVUSDTM', 'LINKUSDTM', 'UNIUSDTM', 'YFIUSDTM', 
'EOSUSDTM', 'DOTUSDTM', 'FILUSDTM', 'ADAUSDTM', 'XRPUSDTM', 'LTCUSDTM', 'TRXUSDTM', 
'GRTUSDTM', 'SUSHIUSDTM', 'XLMUSDTM', '1INCHUSDTM', 'ZECUSDTM', 'DASHUSDTM', 
'AAVEUSDTM', 'KSMUSDTM', 'DOGEUSDTM', 'VETUSDTM', 'BNBUSDTM', 'SXPUSDTM', 'SOLUSDTM', 'IOSTUSDTM', 
'CRVUSDTM', 'ALGOUSDTM', 'AVAXUSDTM', 'FTMUSDTM', 'MATICUSDTM', 'THETAUSDTM', 'ATOMUSDTM', 'CHZUSDTM', 
'ENJUSDTM', 'MANAUSDTM', 'DENTUSDTM', 'OCEANUSDTM', 'BATUSDTM', 'XEMUSDTM', 'QTUMUSDTM', 'XTZUSDTM', 
'SNXUSDTM', 'NEOUSDTM', 'ONTUSDTM', 'XMRUSDTM', 'COMPUSDTM', 'ETCUSDTM', 'WAVESUSDTM', 'BANDUSDTM', 
'MKRUSDTM', 'RVNUSDTM', 'DGBUSDTM', 'MIRUSDTM', 'SHIBUSDTM', 'ICPUSDTM', 'DYDXUSDTM', 'AXSUSDTM', 
'HBARUSDTM', 'EGLDUSDTM', 'ALICEUSDTM', 'YGGUSDTM', 'NEARUSDTM', 'SANDUSDTM', 'C98USDTM', 'ONEUSDTM', 
'VRAUSDTM', 'GALAUSDTM', 'TLMUSDTM', 'CHRUSDTM', 'LRCUSDTM', 'FLOWUSDTM', 'RNDRUSDTM', 'IOTXUSDTM', 
'CROUSDTM', 'WAXPUSDTM', 'PEOPLEUSDTM', 'OMGUSDTM', 'LINAUSDTM', 'IMXUSDTM', 'NFTUSDTM', 'CELRUSDTM', 
'ENSUSDTM', 'CELOUSDTM', 'CTSIUSDTM', 'SLPUSDTM', 'ARPAUSDTM', 'KNCUSDTM', 'SOSUSDTM', 'API3USDTM', 
'ROSEUSDTM', 'AGLDUSDTM', 'APEUSDTM', 'JASMYUSDTM', 'ZILUSDTM', 'GMTUSDTM', 'RUNEUSDTM', 'NYMUSDTM', 
'LOOKSUSDTM', 'AUDIOUSDTM', 'KDAUSDTM', 'KAVAUSDTM', 'BALUSDTM', 'GALUSDTM', 'LUNAUSDTM', 'LUNCUSDTM', 
'OPUSDTM', 'XCNUSDTM', 'UNFIUSDTM', 'LITUSDTM', 'DUSKUSDTM', 'STORJUSDTM', 'ANCUSDTM', 'RSRUSDTM', 
'JSTUSDTM', 'OGNUSDTM', 'TRBUSDTM', 'PERPUSDTM', 'KLAYUSDTM', 'ANKRUSDTM', 'LDOUSDTM', 'WOOUSDTM', 
'RENUSDTM', 'CVCUSDTM', 'INJUSDTM', 'APTUSDTM', 'MASKUSDTM', 'REEFUSDTM']
'''
whait_list = ['ADAUSDTM', 'DASHUSDTM', 'XEMUSDTM', 'SOLUSDTM', 'CHZUSDTM', 'DYDXUSDTM', 'LINKUSDTM',
              'DOTUSDTM', 'SUSHIUSDTM']

size_usdt = 0.5
lever = 20  # % плечо

# Количество одновременных позиций
max_poz = 3
navar = 0.5  # %
perc_mod_price = 2  # 2%

# Настройка индикатора CCI
predel_cci = 100

debug = 'debug'
# пауза между циклами бота
sleep = 20  # секунд
sl = 1


# {'orderId': '637c95a448071900011cae43'}