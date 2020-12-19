
api_secret = ''
api_key = ''

# Program supports USDT, ROSE, and BTC markets only. No USDT.
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from time import sleep
from sys import exit
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor
client = Client(api_key, api_secret)
balance = client.get_asset_balance(asset='BAT')
status = client.get_account_status()
balance_usdt = 400

balance_rose = 0
balance_btc = 0
usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])

def buy_rose_with_usdt(amountUSDT, price):
    global balance_usdt
    global balance_rose
    global balance_btc
    balance_usdt -= amountUSDT
    amountUSDT =  (0.99925 +0.0075)*amountUSDT
    numberOfRose = amountUSDT / price
    balance_rose += numberOfRose

def buy_btc_with_usdt(amountUSDT, price):
    global balance_usdt
    global balance_rose
    global balance_btc
    balance_usdt -= amountUSDT
    amountUSDT =  (0.99925 +0.0075)*amountUSDT
    numberOfBtc = amountUSDT / price
    balance_btc += numberOfBtc

def sell_btc_get_usdt(amount, price):
    global balance_usdt
    global balance_rose
    global balance_btc
    balance_btc -= amount
    amount =  (0.99925 +0.0075)*amount
    number = amount * price
    balance_usdt += number

def sell_rose_get_usdt(amount, price):
    global balance_usdt
    global balance_rose
    global balance_btc
    balance_rose -= amount
    amount =  (0.99925 +0.0075)*amount
    number = amount * price
    balance_usdt += number

def give_rose_get_btc(amount, price):
    global balance_usdt
    global balance_rose
    global balance_btc
    balance_rose-= amount
    amount =  (0.99925 +0.0075)*amount  
    number = amount * price
    balance_btc += number
    pass

def give_btc_get_rose(amount, price):
    global balance_usdt
    global balance_rose
    global balance_btc    
    balance_btc -= amount
    amount = (0.99925 +0.0075)*amount
    number = amount / price
    balance_rose += number   
    pass

def print_balance():
    global balance_usdt
    global balance_rose
    global balance_btc 
    print("balance_usdt : ", balance_usdt)
    print("balance_rose : ", balance_rose)
    print("balance_btc : ", balance_btc)
    print("--------------------------------------")

def traydorEB(amountUSDT):
    #USDT INTO BTC INTO ROSE INTO USDT
    global balance_usdt
    global balance_rose
    global balance_btc
    sleep(1)
    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    #buying btc with Usdt
    #print_balance() 

    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    buy_btc_with_usdt(balance_usdt, usdt_btc_price)
    #print_balance()

    #Buying btc with rose
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    give_btc_get_rose(balance_btc, btc_rose_price)
    print("ici rose se rempli")
    #print_balance()
    #buying usdt with rose
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    sell_rose_get_usdt(balance_rose, usdt_rose_price)
    print_balance()
    pass

def traydorBE(amountUSDT):
    #USDT INTO ROSE INTO BTC INTO USDT
    global balance_usdt
    global balance_rose
    global balance_btc 
    sleep(1)
    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    #print_balance()
    #buying Btc with Usdt
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    buy_rose_with_usdt(balance_usdt, usdt_rose_price)
   # print_balance()
    #Buying btc with rose
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    give_rose_get_btc(balance_rose, btc_rose_price)
    #buying usdt with btc
   # print_balance()
    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    sell_btc_get_usdt(balance_btc, usdt_btc_price)
    print_balance()
    pass

def isworthit(usdt_btc_price, btc_rose_price, usdt_rose_price, amount):
    """
    gapA = (((amount/usdt_btc_price*btc_rose_price*usdt_rose_price) - amount)/amount)*100
    print ("GapA = ", gapA)
    gapB = (((amount/usdt_rose_price/btc_rose_price*usdt_btc_price) - amount)/amount)*100
    print ("Gap = ", gapB)
    """
    #gapA = ((((amount/usdt_btc_price/btc_rose_price*usdt_rose_price) - amount)/amount)*100)-0.225337922
    gapA = ((((amount/usdt_btc_price/btc_rose_price*usdt_rose_price) - amount)/amount)*100)
    print ("Gap = ", gapA)
    #gapB = ((((amount/usdt_rose_price*btc_rose_price*usdt_btc_price) - amount)/amount)*100)-0.225337922
    gapB = ((((amount/usdt_rose_price*btc_rose_price*usdt_btc_price) - amount)/amount)*100)
    print ("Gap = ", gapB)
    return(abs(gapA))


#BTC - USDT
#BTC - ROSE
#USDT - ROSE
print_balance()

from datetime import datetime

print("Debut")
import time
j=0
start = datetime.now()
amount = 500
import numpy as np
values = np.array([])
for i in range (1000) :
    usdt_btc_price = float((client.get_avg_price(symbol='BTCUSDT'))["price"])
    usdt_rose_price = float(client.get_avg_price(symbol='ROSEUSDT')["price"])
    btc_rose_price = float((client.get_avg_price(symbol='ROSEBTC'))["price"])
    alll = isworthit(usdt_btc_price, btc_rose_price, usdt_rose_price, amount)
    if (alll > 0.2):
        values =  np.append(values,(alll))
        j = j+1
        #traydorBE(balance_usdt)
        #traydorEB(balance_usdt)
        print("SiSI")
    print ("usdt_btc_price : ", usdt_btc_price)
    print ("usdt_rose_price : ", usdt_rose_price)
    print ("btc_rose_price : ", btc_rose_price)
    #print("Rapport deux pairs BTC/ROSE : ", float(usdt_rose_price)/float(usdt_btc_price))
    print("------------------")
    print("nombre : ", i)
    print("number of sisis : ",j)
    print("========================================")

difference = datetime.now() - start
print("time = ", difference)
print("number of sisi :", j)
print("values ", values)
print("average of sisis : ", np.mean(values))
print ("Fee btc USDT ", client.get_trade_fee(symbol='BTCUSDT'))
print ("Fee Rose USDT ", client.get_trade_fee(symbol='ROSEUSDT'))
print ("Fee Rose btc ", client.get_trade_fee(symbol='ROSEBTC'))
#print ("Fee btc USDT ", client.get_trade_fee(symbol='BTCUSDT')['maker'])
#print ("Fee Rose USDT ", client.get_trade_fee(symbol='ROSEUSDT')['maker'])
#print ("Fee Rose btc ", client.get_trade_fee(symbol='ROSEBTC')['maker'])
# print("Trades : ", i)
#print_balance()
#klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "26 Nov, 2020", "27 Nov, 2020")
#print(klines)
#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_30MINUTE)
#print(candles)
"""
print ("usdt_btc_price : ", usdt_btc_price)
print ("usdt_rose_price : ", usdt_rose_price)
print ("btc_rose_price : ", btc_rose_price)
print("-------BTC SUR ROSE--------")
print("Rapport deux pairs BTC/ROSE : ", float(usdt_btc_price)/float(usdt_rose_price))
print("delta E/B en prenant en compte les coms : ", 197*float(usdt_btc_price)/float(usdt_rose_price) - float(btc_rose_price) )
print("------------------------------")
"""
"""
#Tests
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("buying 200 usdt worth of btc")
buy_btc_with_usdt(2000, usdt_btc_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("give all _btc_get_rose")
give_btc_get_rose(balance_btc, btc_rose_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("give all give_rose_get_btc")
give_rose_get_btc(balance_rose, btc_rose_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("selling 0.3 btc ")
sell_btc_get_usdt(0.3, usdt_btc_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("buying 1000 usdt worth of rose")
buy_rose_with_usdt(1000, usdt_rose_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("selling all bitcoins ")
sell_rose_get_usdt(balance_rose, usdt_btc_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print("--------------------------------------")
print("selling all btc ")
sell_btc_get_usdt(balance_btc, usdt_btc_price)
print("balance_usdt : ", balance_usdt)
print("balance_rose : ", balance_rose)
print("balance_btc : ", balance_btc)
print ("usdt_btc_price : ", usdt_btc_price)
print ("usdt_rose_price : ", usdt_rose_price)
print ("btc_rose_price : ", btc_rose_price)
print("-------BTC SUR ROSE--------")
print("Rapport deux pairs BTC/ROSE : ", float(usdt_btc_price)/float(usdt_rose_price))
print("delta E/B en prenant en compte les coms : ", 197*float(usdt_btc_price)/float(usdt_rose_price) - float(btc_rose_price) )
print("------------------------------")
print("bien ou quoi : ", status)
"""
