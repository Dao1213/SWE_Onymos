import random
# Class representing a stock order (buy/sell) stored as a linked list node
class stock:
    count = 0           # Global count to assign unique IDs
    symbol = ''         # Shared symbol across all instances (updated with the latest order)
    # Initialize stock order
    def __init__(self, ticker_symbol = '', quantity = 0 , price = 0, next = None):
        if ticker_symbol != '':
            stock.symbol = ticker_symbol
        self.ID = stock.count = stock.count + 1  # Assign unique ID
        self.price = price
        self.quantity = quantity
        self.next = next

    # Add a new order to the end of the list (lowest priority)
    def add_leaf(self, quantity, price):
        next_element = stock('', quantity, price)
        curr = self
        while (not curr.is_leaf()):
            curr = curr.next
        curr.next = next_element

    # Add a new order at the front (highest priority)
    def add_root(self, quantity, price):
        temp = stock('', self.quantity, self.price, self.next)
        origin_price = self.price
        self.quantity = quantity
        self.price = price
        if origin_price != 0:
            self.next = temp

    # Insert a new order into the list based on price (descending for Buy, ascending for Sell)
    def add_bottom(self, quantity, price):
        curr = self
        while curr.next:
            if curr.price >= price and price >= curr.next.price:
                next_element = stock('', quantity, price, curr.next)
                curr.next = next_element
                return
            else:
                curr = curr.next
        curr.add_leaf(quantity, price)

    def add_node(self, quantity, price):
        if price >= self.price or self.price == 0:
            self.add_root(quantity, price)
        else:
            self.add_bottom(quantity, price)

    # Check if this is the last node
    def is_leaf(self):
        return self.next == None
    
    # Remove the root node by replacing its data with the next node's data
    def remove_root(self):
        curr = self
        if curr.is_leaf():
            self.price = 0
            self.quantity = 0
        else:
            self.quantity = curr.next.quantity
            self.price = curr.next.price
            self.ID = self.next.ID
            self.next = curr.next.next
        
    # Remove a node by ID  
    def remove(self, id): 
        #remove root
        if self.ID == id:
            self.remove_root()
        else:
            curr = self
            while not curr.is_leaf():
                if curr.next.ID == id:
                    curr.next = curr.next.next
                    return
                curr = curr.next
            print("the price is not correct")
    # Format the stock list as a string
    def __repr__(self):
        result = []
        curr = self
        while curr and curr.price != 0:
            result.append(f"[{curr.symbol}, Qty: {curr.quantity}, Price: ${curr.price}, ID: {curr.ID}]")
            curr = curr.next
        return ' -> '.join(result)

# Trading system managing buy and sell order books
class Trading:      
    buy_orders = [stock() for _ in range(1024)]     # Array of linked lists for buy orders
    buy_order_index = []                            # Indices of active buy orders
    sell_orders =[stock() for _ in range(1024)]     # Array of linked lists for sell orders
    sell_order_index = []                           # Indices of active sell orders

    # Add a buy or sell order
    def addOrder(self, type, ticker_symbol, quantity, price):
        index = sum( ord(ticker_symbol[i]) * (10**i) for i in range(len(ticker_symbol))) % 1024
        if type == 'Buy':
            if Trading.buy_orders[index].price == 0:
                Trading.buy_orders[index] = stock(ticker_symbol, quantity, price)
            else:
                Trading.buy_orders[index].add_node(quantity,price)
            if index not in Trading.buy_order_index:
                Trading.buy_order_index.append(index)
        elif type == 'Sell':
            if Trading.sell_orders[index].price == 0:
                Trading.sell_orders[index] = stock(ticker_symbol, quantity, price)
            else:
                Trading.sell_orders[index].add_node(quantity,price)
            if index not in Trading.sell_order_index:
                Trading.sell_order_index.append(index)

    # Match buy and sell orders if the buy price is higher or equal to the sell price
    def matchOrder(self):
        temp = list(self.buy_order_index)
        for index in temp:
            buy_order = Trading.buy_orders[index]
            sell_order = Trading.sell_orders[index]
            while(sell_order):
                if buy_order.price >= sell_order.price and sell_order.quantity != 0 :
                    buy_order.remove(buy_order.ID)
                    sell_order.remove(sell_order.ID)
                else:
                    sell_order = sell_order.next
        # Clean up any fully matched (empty) orders
        if( Trading.buy_orders[index].price == 0):
            Trading.buy_order_index.remove(index)
        if( Trading.sell_orders[index].price == 0):
            Trading.sell_order_index.remove(index)
    # Print all active buy and sell orders
    def __repr__(self):
        result = ["\nAll Buy Orders:"]
        for index in Trading.buy_order_index:
            result.append(str(Trading.buy_orders[index]))
        result.append("\nAll Sell Orders:")
        for index in Trading.sell_order_index:
            result.append(str(Trading.sell_orders[index]))
        return '\n'.join(result)
    

# Random order generator for testing
def wrapper():
    symbols = ["AAPL", "TSLA", "GOOG", "AMZN", "META", "NFLX", "NVDA", "MSFT", "BABA", "UBER"]
    orders =["sell","buy"]
    prices =[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    return[random.choice(orders), random.choice(symbols), random.randint(1,100),random.choice(prices)]


