import random



class stock:
    def __init__(self, ticker_symbol, quantity, price, next = None):
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
        print("add leaf")
        temp = stock(self.symbol, self.quantity, self.price, self.next)
        self.symbol = ticker_symbol
        self.quantity = quantity
        self.price = price
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
        if price >= self.price:
            self.add_root(ticker_symbol, quantity, price)
        else:
            self.add_bottom(ticker_symbol, quantity, price)
    
    def is_leaf(self):
        return self.next == None
    

    def __repr__(self):
        result = []
        curr = self
        while curr:
            result.append(f"[{curr.symbol}, Qty: {curr.quantity}, Price: ${curr.price}, Index: {curr.index}]")
            curr = curr.next
        return ' -> '.join(result)


class order:
    def __init__(self, order_type):
        self.type = order_type
        self.list = [0] * 1024
        self.count = 0

list = [0] * 10
print (list)




def wrapper():
    symbols = ["AAPL", "TSLA", "GOOG", "AMZN", "META", "NFLX", "NVDA", "MSFT", "BABA", "UBER"]
    orders =["sell","buy"]
    prices =[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    return[random.choice(orders), random.choice(symbols), random.randint(1,100),random.choice(prices)]
print (wrapper())