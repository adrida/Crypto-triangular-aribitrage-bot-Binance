api_key = "de largent"
api_secret = "3afak"

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from time import sleep
from sys import exit
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
import math
client = Client(api_key, api_secret)

ticks = {}
for filt in client.get_symbol_info('BTCUSDT')['filters']:
    if filt['filterType'] == 'LOT_SIZE':
        ticks['BTC'] = filt['stepSize'].find('1') - 2
        break

for filt in client.get_symbol_info('ROSEUSDT')['filters']:
    if filt['filterType'] == 'LOT_SIZE':
        ticks['ROSE'] = filt['stepSize'].find('1') - 2
        break

for filt in client.get_symbol_info('ROSEBTC')['filters']:
    if filt['filterType'] == 'LOT_SIZE':
        ticks['ROSEBTC'] = filt['stepSize'].find('1') - 2
        break

balanceBTC = client.get_asset_balance(asset='BTC')
balanceUSDT = client.get_asset_balance(asset='USDT')
balanceROSE = client.get_asset_balance(asset='ROSE')
#print("UN GAP SILVOUPLAIT")
#print("ci kwa ca -> ", ticks)
#print(math.floor(378.9995 * 10**ticks['BTC']) / float(10**ticks['BTC']))
print (balanceBTC)
print (balanceUSDT)
print (balanceROSE)
for i in range (1000):
    # Recuperation des prix
    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    # gap = (500 / (usdt_b_p * b_r_p) - 500)/500)*100)
    gap = ((((500/usdt_btc_price)/btc_rose_price*usdt_rose_price - 500)/500)*100)


    print("Un Gap silvouplé (3AFAK) = ", gap)


    if (abs(gap) > 0.32):
        # recuperation des balances

        
        if gap < 0:

            #Vars Sens 2
            #qt_Btc_Usdt = round(float(balanceUSDT["free"])/usdt_b_p) - float(10**(-5),5)
            #qt_Btc_Rose = round(float(balanceBTC["free"])/b_r_p) - float(10**(-8),8)

            balanceUSDT = client.get_asset_balance(asset='USDT')

            # Buy BTC with USDT
            client.order_limit_buy(symbol='BTCUSDT', quantity=math.floor(float(balanceUSDT["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC']) / usdt_btc_price , price = usdt_btc_price)
            #print("Oui : ",round(float(float(balanceUSDT["free"])/usdt_b_p) - float(10**(-5)),5))
            #print(" Buy BTC with USDT \n")
            # Buy ROSE with BTC
            
            #print("Buy ROSE with BTC")

            #balanceBTC = client.get_asset_balance(asset='BTC')
            #balanceUSDT = client.get_asset_balance(asset='USDT')
            #balanceROSE = client.get_asset_balance(asset='ROSE')
            #print (balanceBTC)
            #print (balanceUSDT)
            #print (balanceROSE)


            sleep(0.8)

            balanceBTC = client.get_asset_balance(asset='BTC')
            #print(balanceBTC)
            #print(math.floor(float(balanceBTC["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC']))
            client.order_limit_buy(symbol='ROSEBTC', quantity=math.floor(float(balanceBTC["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC']) / btc_rose_price, price = btc_rose_price)
            
            #print(" Buy ROSE with BTC \n")
            #balanceBTC = client.get_asset_balance(asset='BTC')
            #balanceUSDT = client.get_asset_balance(asset='USDT')
            #balanceROSE = client.get_asset_balance(asset='ROSE')
            #print (balanceBTC)
            #print (balanceUSDT)
            #print (balanceROSE)
     
            # Sell ROSE for USDT

            sleep(0.8)

            balanceROSE = client.get_asset_balance(asset='ROSE')
            #qt_Rose_Usdt = round(float(balanceROSE["free"])*usdt_r_p - float(10**(-8)),8)
            #print(float(balanceROSE["free"]))
            #print(math.floor(float(balanceROSE["free"]) * 10**1) / float(10**1))
            client.order_limit_sell(symbol='ROSEUSDT', quantity = math.floor(float(balanceROSE["free"]) * 10**1) / float(10**1), price = usdt_rose_price)
            #print("Sell ROSE for USDT")

            #balanceBTC = client.get_asset_balance(asset='BTC')
            #balanceUSDT = client.get_asset_balance(asset='USDT')
            #balanceROSE = client.get_asset_balance(asset='ROSE')
            #print (balanceBTC)
            #print (balanceUSDT)
            #print (balanceROSE)

        else:
            
            #Vars Sens 1

            balanceUSDT = client.get_asset_balance(asset='USDT')

            # Buy ROSE with USDT
            client.order_limit_buy(symbol='ROSEUSDT', quantity=math.floor(float(balanceUSDT["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC']) / usdt_rose_price, price = usdt_rose_price)
            #print("Pythoun : ", round(float(float(balanceUSDT["free"])/usdt_r_p) - float(10**(-5)),5))
            #print("Buy ROSE with USDT")
            # Sell ROSE for BTC

            #balanceBTC = client.get_asset_balance(asset='BTC')
            #balanceUSDT = client.get_asset_balance(asset='USDT')
            #balanceROSE = client.get_asset_balance(asset='ROSE')
            #print (balanceBTC)
            #print (balanceUSDT)
            #print (balanceROSE)

            sleep(0.8)

            balanceROSE = client.get_asset_balance(asset='ROSE')
            #qt_Usdt_Rose = round(float(balanceUSDT["free"])/usdt_r_p - float(10**(-5)),5)
            #print(math.floor(float(balanceROSE["free"]) * 10**1) / float(10**1))
            client.order_limit_sell(symbol='ROSEBTC', quantity=math.floor(float(balanceROSE["free"])), price = btc_rose_price)
            #print("Sell ROSE for BTC")
            # Sell BTC for USDT

            #balanceBTC = client.get_asset_balance(asset='BTC')
            #balanceUSDT = client.get_asset_balance(asset='USDT')
            #balanceROSE = client.get_asset_balance(asset='ROSE')
            #print (balanceBTC)
            #print (balanceUSDT)
            #print (balanceROSE)

            sleep(0.8)

            balanceBTC = client.get_asset_balance(asset='BTC')
            #qt_Usdt_Btc = round(float(balanceBTC["free"])*usdt_b_p - float(10**(-5)),5)
            #qt_Rose_Btc = round(float(balanceROSE["free"])*b_r_p - float(10**(-8)),8)
            client.order_limit_sell(symbol='BTCUSDT', quantity = math.floor(float(balanceBTC["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC']), price = usdt_btc_price)
            #print("Sell BTC for USDT")

            #balanceBTC = client.get_asset_balance(asset='BTC')
            #balanceUSDT = client.get_asset_balance(asset='USDT')
            #balanceROSE = client.get_asset_balance(asset='ROSE')
            #print (balanceBTC)
            #print (balanceUSDT)
            #print (balanceROSE)
        break

    print("-------------------------------------------")
"""
SENS 1 ROSE BTC
SOMME / usdtroseprice  * btcrose * usdtbtc

SENS 2 BTC ROSE
SOMME / usdtbtc / btcrose * usdtrose

GAP < 0 
    sens 1 : win 
    sens 2 : nul
GAP > 0
    sens 1 : nul
    sens 2 : win
"""


# affichage des balance
balanceBTC = client.get_asset_balance(asset='BTC')
balanceUSDT = client.get_asset_balance(asset='USDT')
balanceROSE = client.get_asset_balance(asset='ROSE')
print("-------------------------------------------")
print (balanceBTC)
print (balanceUSDT)
print (balanceROSE)