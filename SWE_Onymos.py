import random

class stock:
    def __init__(self, ticker_symbol = '', quantity = 0 , price = 0, next = None):
        self.symbol = ticker_symbol
        self.price = price
        self.quantity = quantity
        self.next = next
        self.index = sum( ord(ticker_symbol[i]) * (10**i) for i in range(len(ticker_symbol))) % 1024 

    def add_leaf(self, ticker_symbol, quantity, price):
        print("add leaf")
        next_element = stock(ticker_symbol, quantity, price)
        curr = self
        while (not curr.is_leaf()):
            curr = curr.next
        curr.next = next_element

    def add_root(self, ticker_symbol, quantity, price):
        temp = stock(self.symbol, self.quantity, self.price, self.next)
        origin_price = self.price
        print("add root")
        self.symbol = ticker_symbol
        self.quantity = quantity
        self.price = price
        if origin_price != 0:
            self.next = temp

    def add_bottom(self, ticker_symbol, quantity, price):
        curr = self
        while curr.next:
            if curr.price >= price and price >= curr.next.price:
                next_element = stock(ticker_symbol, quantity, price, curr.next)
                curr.next = next_element
                return
            else:
                curr = curr.next
        curr.add_leaf(ticker_symbol, quantity, price)

    def add_node(self, ticker_symbol, quantity, price):
        if price >= self.price or self.price == 0:
            self.add_root(ticker_symbol, quantity, price)
        else:
            self.add_bottom(ticker_symbol, quantity, price)
    
    def is_leaf(self):
        return self.next == None
    
    def remove_root(self):
        curr = self
        if curr.is_leaf():
            self.symbol = ''
            self.price = 0
            self.quantity = 0
            self.index = None
        else:
            self.symbol = curr.next.symbol
            self.quantity = curr.next.quantity
            self.price = curr.next.price
            self.index = self.next.index
            self.next = curr.next.next
      
    def remove(self, price): 
        #remove root
        if self.price == price:
            self.remove_root()
        else:
            curr = self
            while not curr.is_leaf():
                if curr.next.price == price:
                    curr.next = curr.next.next
                    return
                curr = curr.next
            print("the price is not correct")

    def __repr__(self):
        result = []
        curr = self
        while curr:
            result.append(f"[{curr.symbol}, Qty: {curr.quantity}, Price: ${curr.price}, Index: {curr.index}]")
            curr = curr.next
        return ' -> '.join(result)

"""
def wrapper():
    symbols = ["AAPL", "TSLA", "GOOG", "AMZN", "META", "NFLX", "NVDA", "MSFT", "BABA", "UBER"]
    orders =["sell","buy"]
    prices =[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    return[random.choice(orders), random.choice(symbols), random.randint(1,100),random.choice(prices)]
print (wrapper())"""

buy_orders = [stock() for _ in range(1024)]
#list will store the index (ID)of the stock if it exit in buy_order 
cnt_buy_ors =[]

sell_orders =[stock() for _ in range(1024)]
#list will store the index (ID)of the stock if it exit in sell_order 
cnt_sell_ors =[]


def matchOrder(sell_orders:stock, buy_orders: stock):
    for index in cnt_buy_ors:
        buy_order = buy_orders[index]
        sell_order = sell_orders[index]
        







