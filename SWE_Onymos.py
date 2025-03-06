import random



class Nodes:
    def __init__(self, quantity, price, next = None):
        self.price = price
        self.quantity = quantity
        self.next = next

    def add_leaf(self, quantity, price):
        print("add leaf")
        next_element = Nodes(quantity, price)
        curr = self
        while (not curr.is_leaf()):
            curr = curr.next
        curr.next = next_element

    def add_root(self, quantity, price):
        print("add leaf")
        temp = Nodes(self.quantity, self.price, self.next)
        self.quantity = quantity
        self.price = price
        self.next = temp

    def add_bottom(self, quantity, price):
        curr = self
        while curr.next:
            if curr.price >= price and price >= curr.next.price:
                next_element = Nodes(quantity, price, curr.next)
                curr.next = next_element
                return
            else:
                curr = curr.next
        curr.add_leaf(quantity, price)

    def add_node(self, quantity, price):
        if price >= self.price:
            self.add_root(quantity, price)
        else:
            self.add_bottom(quantity, price)
    
    def is_leaf(self):
        return self.next == None
    

    def __repr__(self):
        result = []
        curr = self
        while curr:
            result.append(f"[Qty: {curr.quantity}, Price: ${curr.price}]")
            curr = curr.next
        return ' -> '.join(result)

class stocks:
    def __init__(self,ticker_symbol, quantity, price):
        self.symbol = ticker_symbol
        self.index = sum( ord(ticker_symbol[i]) * (10**i) for i in range(len(ticker_symbol))) % 1024
        self.node = Nodes(quantity,price)

class type:
    def __init__(self, order_type):
        self.type = order_type
        self.list = [0] * 1024
        self.element = []
        self.count = 0









def wrapper():
    symbols = ["AAPL", "TSLA", "GOOG", "AMZN", "META", "NFLX", "NVDA", "MSFT", "BABA", "UBER"]
    orders =["sell","buy"]
    prices =[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    return[random.choice(orders), random.choice(symbols), random.randint(1,100),random.choice(prices)]
print (wrapper())