api_key = open("apikey.txt", "r")
api_secret = open("secretkey.txt", "r")

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from time import sleep
from sys import exit
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
client = Client(api_key, api_secret)

for i in range (2):
    # Recuperation des prix
    usdt_b_p = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    usdt_r_p = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    b_r_p = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    gap = ((((500/usdt_b_p/b_r_p*usdt_r_p) - 500)/500)*100)
    print("Gap aquoitigal = ", gap)
    if (abs(gap) > 0.0):
        # recuperation des balances
        balanceBTC = client.get_asset_balance(asset='BTC')
        balanceUSDT = client.get_asset_balance(asset='USDT')
        balanceROSE = client.get_asset_balance(asset='ROSE')

        if gap > 0:

            #Vars Sens 2
            #qt_Btc_Usdt = round(float(balanceUSDT["free"])/usdt_b_p) - float(10**(-5),5)
            #qt_Btc_Rose = round(float(balanceBTC["free"])/b_r_p) - float(10**(-8),8)

            balanceUSDT = client.get_asset_balance(asset='USDT')

            # Buy BTC with USDT
            client.order_market_buy(symbol='BTCUSDT', quoteOrderQty=round(float(balanceUSDT["free"]) - float(10**(-8)) ,8))
            #print("Oui : ",round(float(float(balanceUSDT["free"])/usdt_b_p) - float(10**(-5)),5))
            #print(" Buy BTC with USDT \n")
            # Buy ROSE with BTC

            balanceBTC = client.get_asset_balance(asset='BTC')
            print(balanceBTC)
            client.order_market_buy(symbol='ROSEBTC', quoteOrderQty=round(float(balanceBTC["free"]) - float(10**(-8)) ,8))
            #print(" Buy ROSE with BTC \n")
            # Sell ROSE for USDT

            balanceROSE = client.get_asset_balance(asset='ROSE')
            qt_Rose_Usdt = round(float(balanceROSE["free"])*usdt_r_p - float(10**(-8)),8)
            print(float(balanceROSE["free"]))
            client.order_market_sell(symbol='ROSEUSDT', quantity = qt_Rose_Usdt)
            #print("Sell ROSE for USDT")
        else:
            
            #Vars Sens 1
            
            balanceUSDT = client.get_asset_balance(asset='USDT')

            # Buy ROSE with USDT
            client.order_market_buy(symbol='ROSEUSDT', quoteOrderQty=round(float(balanceUSDT["free"]) - float(10**(-8)) ,8))
            #print("Pythoun : ", round(float(float(balanceUSDT["free"])/usdt_r_p) - float(10**(-5)),5))
            #print("Buy ROSE with USDT")
            # Sell ROSE for BTC

            balanceROSE = client.get_asset_balance(asset='ROSE')
            qt_Usdt_Rose = round(float(balanceUSDT["free"])/usdt_r_p - float(10**(-5)),5)
            client.order_market_sell(symbol='ROSEBTC', quantity=qt_Usdt_Rose)
            #print("Sell ROSE for BTC")
            # Sell BTC for USDT

            balanceBTC = client.get_asset_balance(asset='BTC')
            qt_Usdt_Btc = round(float(balanceBTC["free"])*usdt_b_p - float(10**(-5)),5)
            qt_Rose_Btc = round(float(balanceROSE["free"])*b_r_p - float(10**(-8)),8)
            client.order_market_sell(symbol='BTCUSDT', quantity = qt_Rose_Btc)
            #print("Sell BTC for USDT")
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
print (balanceBTC)
print (balanceUSDT)
print (balanceROSE)