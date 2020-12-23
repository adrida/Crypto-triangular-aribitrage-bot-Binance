api_key = ""
api_secret = ""

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
temoin = False
for i in range (1000):
    # Recuperation des prix
    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    # gap = (500 / (usdt_b_p * b_r_p) - 500)/500)*100)
    gap = ((((500/usdt_btc_price)/btc_rose_price*usdt_rose_price - 500)/500)*100)


    print("Un Gap silvouplé (3AFAK) = ", gap)


    if (abs(gap) > 0.34):
        # recuperation des balances

        
        if gap > 0:

            #Vars Sens 2
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            balanceUSDT = client.get_asset_balance(asset='USDT')

            # Buy BTC with USDT ( price = +0.01%)
            #price_to_buy_BTCUSDT = 1.0001*usdt_btc_price
            price_to_buy_BTCUSDT = math.floor(usdt_btc_price * 10**2) / float(10**2)
            qt_BTCUSDT_buy = math.floor(float(balanceUSDT["free"])/ price_to_buy_BTCUSDT * 10**5) / float(10**5) 
            client.order_limit_buy( 
                symbol='BTCUSDT', 
                quantity= qt_BTCUSDT_buy, 
                price = price_to_buy_BTCUSDT
            )

            while(temoin == False):
                sleep(0.1)
                balanceBTC = client.get_asset_balance(asset='BTC')
                if(float(balanceBTC["free"]) * usdt_btc_price > 8.0):
                    temoin = True
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            # ( price = +0.01%)
            if(temoin == True):
                temoin = False
                balanceBTC = client.get_asset_balance(asset='BTC')
                #price_to_buy_ROSEBTC = 1.0002*btc_rose_price
                price_to_buy_ROSEBTC = math.floor(btc_rose_price * 10**8) / float(10**8)
                qt_ROSEBTC_buy = math.floor(float(balanceBTC["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC']) / price_to_buy_ROSEBTC
                
                client.order_limit_buy(
                    symbol='ROSEBTC',
                    quantity= qt_ROSEBTC_buy,
                    price = price_to_buy_ROSEBTC
                )

            while(temoin == False):
                sleep(0.1)
                balanceROSE = client.get_asset_balance(asset='ROSE')
                if(float(balanceROSE["free"]) * usdt_rose_price > 8.0):
                    temoin = True
            
            # Sell ROSE for USDT

            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            #( price = -0.01%)
            if(temoin == True):
                temoin = False
                balanceROSE = client.get_asset_balance(asset='ROSE')
                #price_to_sell_ROSEUSDT = 0.9999 * usdt_rose_price
                price_to_sell_ROSEUSDT = math.floor(usdt_rose_price * 10**5) / float(10**5)
                qt_ROSEUSDT_sell = math.floor(float(balanceROSE["free"]) * 10**1) / float(10**1)
                
                client.order_limit_sell(
                    symbol='ROSEUSDT', 
                    quantity = qt_ROSEUSDT_sell, 
                    price = price_to_sell_ROSEUSDT
                )

            while(temoin == False):
                sleep(0.1)
                balanceROSE = client.get_asset_balance(asset='ROSE')
                if(float(balanceROSE["free"]) * usdt_rose_price < 5.0):
                    temoin = True

           
            temoin = False
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

        else:
            
            #Vars Sens 1
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            balanceUSDT = client.get_asset_balance(asset='USDT')

            # Buy ROSE with USDT #( price = +0.01%)
            #price_to_buy_ROSEUSDT = 1.0001 * usdt_rose_price
            price_to_buy_ROSEUSDT = math.floor(usdt_rose_price * 10**5) / float(10**5)
            qt_ROSEUSDT_buy = math.floor(float(balanceUSDT["free"])/ price_to_buy_ROSEUSDT * 10**1) / float(10**1) 

            client.order_limit_buy(
                symbol='ROSEUSDT', 
                quantity=qt_ROSEUSDT_buy, 
                price = price_to_buy_ROSEUSDT
            )

            while(temoin == False):
                sleep(0.1)
                balanceROSE = client.get_asset_balance(asset='ROSE')
                if(float(balanceROSE["free"]) * usdt_rose_price > 5.0):
                    temoin = True
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            #( price = -0.01%)

            if(temoin == True):
                temoin = False
                balanceROSE = client.get_asset_balance(asset='ROSE')
                #price_to_sell_ROSEBTC = 0.9998 * btc_rose_price
                price_to_sell_ROSEBTC = math.floor(btc_rose_price * 10**8) / float(10**8)
                qt_ROSEBTC_sell = math.floor(float(balanceROSE["free"]))
                client.order_limit_sell(
                    symbol='ROSEBTC', 
                    quantity=qt_ROSEBTC_sell, 
                    price = price_to_sell_ROSEBTC
                )
            
            while(temoin == False):
                sleep(0.1)
                balanceBTC = client.get_asset_balance(asset='BTC')
                if(float(balanceBTC["free"]) * usdt_btc_price > 8.0):
                    temoin = True
            
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
            #( price = -0.01%)

            if(temoin == True):
                temoin = False
                balanceBTC = client.get_asset_balance(asset='BTC')
                #price_to_sell_BTCUSDT = 0.9999 * usdt_btc_price
                price_to_sell_BTCUSDT = math.floor(usdt_btc_price * 10**2) / float(10**2)
                qt_BTCUSDT_sell = math.floor(float(balanceBTC["free"]) * 10**ticks['BTC']) / float(10**ticks['BTC'])
                client.order_limit_sell(
                    symbol='BTCUSDT', 
                    quantity = qt_BTCUSDT_sell, 
                    price = price_to_sell_BTCUSDT
                )
            
            while(temoin == False):
                sleep(0.1)
                balanceBTC = client.get_asset_balance(asset='BTC')
                if(float(balanceBTC["free"]) * usdt_btc_price < 8.0):
                    temoin = True
            
            temoin = False
            
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