#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import ccxt
import time
import pandas as pd
import logging
import argparse

logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = 'YOUR API KEY HERE'
API_SECRET = 'YOUR API SECRET KEY HERE'
REFRESH_INTERVAL = 60
MAX_POSITION_SIZE = 0.1
STOP_LOSS_PERCENT = 2.0
STATE_FILE = 'bot_state.txt'

def read_bot_state():
    try:
        with open(STATE_FILE, 'r') as file:
            return file.read() == 'True'
    except FileNotFoundError:
        return False

def write_bot_state(state):
    with open(STATE_FILE, 'w') as file:
        file.write(str(state))

class TradingBot:
    def __init__(self, desired_profit):
        self.desired_profit = desired_profit
        self.exchange = self.initialize_exchange()
        self.crypto_pairs = []
        self.balances = {}
        write_bot_state(True)
        print(f"Bot Coinbase Started with a daily profit goal of ${self.desired_profit}")

    def initialize_exchange(self):
        try:
            exchange = ccxt.coinbase({
                'apiKey': API_KEY,
                'secret': API_SECRET
            })
            exchange.load_markets()
            logging.info("Exchange initialized successfully.")
            return exchange
        except Exception as e:
            logging.error(f"Failed to initialize exchange: {str(e)}")
            return None

    def fetch_crypto_pairs(self):
        try:
            balance = self.exchange.fetch_balance()
            self.balances = {currency: bal for currency, bal in balance['total'].items() if bal > 0}
            markets = self.exchange.load_markets()
            self.crypto_pairs = [pair for pair, market in markets.items() if market['active'] and self.balances.get(market['base'], 0) > 0]
            logging.info(f"Active crypto pairs with positive balance: {self.crypto_pairs}")
        except Exception as e:
            logging.error(f"Failed to fetch crypto pairs: {str(e)}")

    def execute_strategy(self):
        self.fetch_crypto_pairs()
        if not self.crypto_pairs:
            logging.info("No active trading pairs with positive balance available.")
            return

        print("Available pairs for trading with positive balance:")
        for index, pair in enumerate(self.crypto_pairs, start=1):
            base_currency = pair.split('/')[0]
            balance = self.balances.get(base_currency, 0)
            print(f"{index}. {pair} : {balance} {base_currency}")

        try:
            choice = int(input("Select the pair number you want to trade: ")) - 1
            if 0 <= choice < len(self.crypto_pairs):
                selected_pair = self.crypto_pairs[choice]
                self.trade(selected_pair)
            else:
                print("Invalid selection. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def trade(self, pair):
        ohlcv = self.exchange.fetch_ohlcv(pair, '1d')
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        df['MA30'] = df['close'].rolling(window=30).mean()
        last_price = df['close'].iloc[-1]
        ma30 = df['MA30'].iloc[-1]

        if last_price > ma30:
            base_currency = pair.split('/')[0]
            available_balance = self.balances.get(base_currency, 0)
            if available_balance > 0:
                position_size = min(available_balance * MAX_POSITION_SIZE, available_balance)
                self.place_order(pair, position_size)
            else:
                logging.info("No balance available to place order for " + base_currency)

    def place_order(self, pair, amount):
        try:
            # Determine if the pair is a fiat currency to handle fiat purchase differently
            base_currency, quote_currency = pair.split('/')
            if quote_currency in ['USD', 'EUR', 'GBP', 'USDC']:  # Common fiat and stablecoin currencies
                # This assumes amount is the total cost you want to spend in quote currency
                order = self.exchange.create_market_buy_order(pair, None, {'amount': amount})
            else:
                # For crypto to crypto, this assumes amount is the total amount of the base currency you want to buy
                order = self.exchange.create_market_buy_order(pair, amount)
            logging.info(f"Order placed for {pair}: {order}")
        except Exception as e:
            logging.error(f"Failed to place order for {pair}: {str(e)}")

def monitor():
    try:
        with open('bot.log', 'r') as file:
            print(file.read())
    except Exception as e:
        print(f"Failed to read log file: {str(e)}")

def check_status():
    if read_bot_state():
        print("The trading bot is currently active.")
    else:
        print("The trading bot is not active.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Coinbase Trading Bot')
    parser.add_argument('--start', action='store_true', help='Start the trading bot')
    parser.add_argument('--desired_profit', type=float, default=10.0, help='Desired daily profit in USD')
    parser.add_argument('--monitor', action='store_true', help='Monitor the bot activities')
    parser.add_argument('--status', action='store_true', help='Check if the bot is active')
    parser.add_argument('--stop', action='store_true', help='Stop the trading bot')
    args = parser.parse_args()

    if args.start:
        bot = TradingBot(args.desired_profit)
        bot.execute_strategy()
    elif args.monitor:
        monitor()
    elif args.status:
        check_status()
    elif args.stop:
        write_bot_state(False)
        print("Trading bot has been stopped.")
